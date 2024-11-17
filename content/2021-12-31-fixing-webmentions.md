---
title: 'Refactoring DLTJ, Winter 2021 Part 2.5: Fixing the Webmentions Cache'
modified: '2022-02-19T18:17:49-05:00'
category: Raw Technology
categories:
- Meta Category
tags:
- webmention
- AWS CodeBuild
- jekyll
- static website
---
Okay, a half-step backward to fix something I broke yesterday. 
As I [described earlier this year](https://dltj.org/article/dltj-with-webmention/), this static website blog uses the {{ robustlink(href="https://www.w3.org/TR/webmention/", versionurl="https://web.archive.org/web/20210711010105/https://www.w3.org/TR/webmention/", versiondate="2021-07-11", title="Webmention, a W3C Recommendation", anchor="Webmention protocol") }} to notify others when I link to their content and receive notifications from others. 
Behind the scenes, I'm using the Jekyll plugin called {{ robustlink(href="https://github.com/aarongustafson/jekyll-webmention_io/", versionurl="https://web.archive.org/web/20210712020229/https://github.com/aarongustafson/jekyll-webmention_io/", versiondate="2021-07-11", title="Jekyll-webmention_io project homepage", anchor="jekyll-webmention_io") }} to integrate Webmention data into my blog's content. 
Each time the contents of this site is built, that plug-in contacts the {{ robustlink(href="https://webmention.io/", versionurl="https://web.archive.org/web/20210707082122/https://webmention.io/", versiondate="2021-07-11", title="webmention.io homepage", anchor="Webmention.IO service") }} to receive its Webmention data. 
(Webmention.IO holds onto it between Jekyll builds since there is no always-on "dltj.org" server to receive notifications from others.) 
The plug-in caches that information to ease the burden on the Webmention.IO service.

The previous CloudFormation-based process was using AWS CodeBuild natively, and the Webmention cache was stored in {{ robustlink(href="https://aws.amazon.com/blogs/devops/how-to-enable-caching-for-aws-codebuild/", versionurl="https://web.archive.org/web/20191223063653/https://aws.amazon.com/blogs/devops/how-to-enable-caching-for-aws-codebuild/", versiondate="2021-12-31", title="How to Enable Caching for AWS CodeBuild | AWS DevOps Blog", anchor="CodeBuild's caching function") }}.
CodeBuild automatically downloads the previous cache into the working directory for each build iteration and then automatically uploads the cache as the build is completed. 
Handy, right?

Well, AWS Amplify simplifies some of the setup of working with the underlying CodeBuild tool. 
One of the configuration options that is no longer available is the ability to specify which S3 bucket to use as the CodeBuild cache; so I couldn't point it at the previous cache files and all of the previous Webmention entries no longer appeared on the blog pages. 
Fortunately, I hadn't decommissioned the CloudFormation stuff, so I still had access to the old cache; I was able to extract the four webmention files (but see below for a discussion about that).

Since Amplify doesn't allow me to have direct access to the CodeBuild cache, I decided it was high time to use a dedicated cache location for these webmention files. 
To do that took three steps:
1. Create the S3 bucket (with no public access)
2. Add read/write policy for that bucket to the AWS role assigned to the Amplify app
3. Add lines to the `amplify.yml` file to copy files from the S3 bucket into and out of the working directory

For step 2, the IAM policy for the Amplify role:
```yaml
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "s3:DeleteObject",
                "s3:PutObject",
                "s3:GetObject",
                "s3:ListBucket"
            ],
            "Resource": "arn:aws:s3:::org.dltj.webmentions-cache"
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": [
                "s3:ListAllMyBuckets"
            ],
            "Resource": "*"
        }
    ]
}
```

For the `amplify.yml` file:

```yaml
version: 1
frontend:
  phases:
    preBuild:
      commands:
        - aws s3 cp s3://org.dltj.webmentions-cache webmentions-cache --recursive
        - rvm use $VERSION_RUBY_2_6
        - bundle install --path vendor/bundle
    build:
      commands:
        - rvm use $VERSION_RUBY_2_6
        - bundle exec jekyll build --trace
    postBuild:
      commands:
        - aws s3 cp webmentions-cache s3://org.dltj.webmentions-cache --recursive
  artifacts:
    baseDirectory: _site
    files:
      - '**/*'
  cache:
    paths:
      - 'vendor/**/*'
```

And the webmentions part of the Jekyll `_config.yml` file:

```yaml
webmentions:
  cache_folder: webmentions-cache
```

## Contents of the AWS CodeBuild Cache File
Can we do a quick sidebar on the AWS CodeBuild caching mechanism? 
Because I was not expecting what I saw.
The CodeBuild cache S3 bucket contains one file with a {{ robustlink(href="https://en.wikipedia.org/wiki/Universally_unique_identifier", versionurl="https://archive.li/wip/Q7RhL", versiondate="2021-12-31", title="Universally unique identifier | Wikipedia", anchor="UUID") }} as its name. 
That file is a tar-gzip'd archive of a flat directory containing sequentially numbered files (`0` through `8099` in my case) and a `codebuild.json` table of contents:

```json
{
  "version": "1.0",
  "content": {
    "files": [
      {
        "path": "vendor/s3deploy.tar.gz",
        "rel": "src"
      },
      {
        "path": "vendor/s3deploy",
        "rel": "src"
      },
      {
        "path": "vendor/LICENSE",
        "rel": "src"
      },
      {
        "path": "vendor/README.md",
        "rel": "src"
      },
      {
        "path": "vendor/webmentions",
        "rel": "src"
      },
      {
        "path": "vendor/webmentions/received.yml",
        "rel": "src"
      },
      {
        "path": "vendor/webmentions/lookups.yml",
        "rel": "src"
      },
      {
        "path": "vendor/webmentions/bad_uris.yml",
        "rel": "src"
      },
      {
        "path": "vendor/webmentions/outgoing.yml",
        "rel": "src"
      },
    ...
```

Each item in the `files` array corresponded to the numbered filename in the directory. 
(In the case of the 4th item in the array—a directory—there was no corresponding file in the tar-gzip archive.) 
Fortunately, the four files I was looking for were near the top of the list and I didn't have to go hunting through all eight-thousand-some-odd files to find them.
(The [s3deploy](https://github.com/dltj/s3deploy) program is one that I found to intelligently copy modified files from the CodeBuild working directory to the S3 static website bucket.)

I'm really wondering about the engineering requirements for all of this overhead. 
Why not just use a native tar-gzip archive without the process of parsing the table of contents and renaming the files?