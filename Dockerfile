# Use Python as the base image
FROM python:3.12.7-slim

# s3deploy version to use
ARG S3DEPLOY_VERSION="2.12.1"

# Set the working directory
WORKDIR /app

# Install necessary system dependencies and PDM
RUN apt-get update && apt-get install -y \
  git \
  curl \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
  # Install PDM
  && curl -sSL https://raw.githubusercontent.com/pdm-project/pdm/main/install-pdm.py | python3 -

# Ensure /root/.local/bin is in PATH
ENV PATH="/root/.local/bin:$PATH"

# Get the `s3deploy` program
RUN set -eux; \
  curl -s -S -L -f https://github.com/bep/s3deploy/releases/download/v${S3DEPLOY_VERSION}/s3deploy_${S3DEPLOY_VERSION}_linux-amd64.tar.gz  -o /tmp/s3deploy.tar.gz; \
  tar -xzf /tmp/s3deploy.tar.gz --directory /usr/local/bin s3deploy; \
  rm /tmp/s3deploy.tar.gz

# Copy the pyproject.toml and pdm.lock files
COPY pyproject.toml pdm.lock* util /app/

# Install the dependencies
RUN pdm install --prod --no-self

# Clone the specified Pelican source repository
RUN git clone https://github.com/dltj/pelican.git /app/pelican

# Clone the specified theme repository
RUN git clone https://github.com/dltj/pelican-hyde.git /app/pelican-themes/pelican-hyde

# Install Pelican from the cloned source
RUN pip install /app/pelican

# Copy your Pelican configuration files to the container
COPY pelicanconf.py /app/pelicanconf.py
COPY publishconf.py /app/publishconf.py

# Expose port 8000 for serving
EXPOSE 8000

# Let's get into it!
ENTRYPOINT ["pdm", "run", "pelican"]
CMD ["--version"]