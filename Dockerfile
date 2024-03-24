# Ruby image to use, change with [--build-arg RUBY_VERSION="3.3.0"]
ARG RUBY_VERSION="3.3.0"
# Alpine image to use, change with [--build-arg ALPINE_VERSION="3.19"]
ARG ALPINE_VERSION="3.19"
# s3deploy version to use
ARG S3DEPLOY_VERSION="2.11.0"


FROM ruby:${RUBY_VERSION}-alpine${ALPINE_VERSION} AS dltj-jekyll-builder

# Install build dependencies
RUN set -eux; \
  apk add --no-cache --virtual build-deps \
  build-base \
  zlib-dev \
  git 

# Install Bundler
RUN set -eux; gem install bundler

COPY Gemfile-docker ./Gemfile

ENV BUNDLE_HOME=/usr/local/bundle \
  BUNDLE_APP_CONFIG=/usr/local/bundle \
  BUNDLE_DISABLE_PLATFORM_WARNINGS=true \
  BUNDLE_BIN=/usr/local/bundle/bin

# Install gems from `Gemfile` via Bundler
RUN set -eux; \
  bundler install


FROM ruby:${RUBY_VERSION}-alpine${ALPINE_VERSION} AS dltj-jekyll-runner
# Repeat ARG here because [Docker is stupid](https://docs.docker.com/reference/dockerfile/#understand-how-arg-and-from-interact)
ARG S3DEPLOY_VERSION

# `git` is needed by the last-modified-at plugin
# `nodejs` is needed by one of the gems
# `jemalloc` is the malloc replacement
RUN set -eux; \
  apk add --no-cache --virtual runner-deps \
  git \
  nodejs \
  jemalloc \
  aws-cli \
  curl \
  jq

RUN set -eux; \
  curl -s -S -L -f https://github.com/bep/s3deploy/releases/download/v${S3DEPLOY_VERSION}/s3deploy_${S3DEPLOY_VERSION}_linux-amd64.tar.gz  -o /tmp/s3deploy.tar.gz; \
  tar -xzf /tmp/s3deploy.tar.gz --directory /usr/local/bin s3deploy; \
  rm /tmp/s3deploy.tar.gz

# Install jemalloc — see https://github.com/jemalloc/jemalloc/issues/1443#issuecomment-1895891270
RUN set -eux; \ 
  apk add --no-cache patchelf; \
  patchelf --add-needed libjemalloc.so.2 /usr/local/bin/ruby; \
  apk del patchelf

ENV RUBY_YJIT_ENABLE=1 \
  MALLOC_CONF="background_thread:true,metadata_thp:auto,dirty_decay_ms:500,muzzy_decay_ms:5000,narenas:2"

COPY --from=dltj-jekyll-builder /usr/local/bundle /usr/local/bundle
COPY --from=dltj-jekyll-builder /Gemfile* /

# Clean up
WORKDIR /srv/jekyll

EXPOSE 4000
ENTRYPOINT ["bundler", "exec", "jekyll"]
CMD ["--version"]
