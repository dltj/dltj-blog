# DLTJ Blog with Jekyll on AWS CodeBuild/ECR/S2/CloudFront

## Build the Docker image 

docker build -t dltj-jekyll-runner:latest .


## Local blog generation

docker run --rm \
    -v ${PWD}:/srv/jekyll \
    -p 4000:4000 \
    {aws_acct_id}.dkr.ecr.us-east-1.amazonaws.com/codebuild/dltj-jekyll-runner:latest serve --host 0.0.0.0


## Upload the CodeBuild custom build environment image

aws --profile dltj-admin ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin {aws_acct_id}.dkr.ecr.us-east-1.amazonaws.com

docker tag dltj-jekyll-runner:latest {aws_acct_id}.dkr.ecr.us-east-1.amazonaws.com/codebuild/dltj-jekyll-runner:latest

docker push {aws_acct_id}.dkr.ecr.us-east-1.amazonaws.com/codebuild/dltj-jekyll-runner:latest