---
title: Starting a Python-oriented Serverless-dot-com Project
modified: 2022-02-06T11:56:25-05:00
categories:
- Raw Technology
tags:
- Serverless computing
- Python programming language
- Node programming language
- Amazon Web Services
---

In the past few months, I've created about a half-dozen projects using "serverless" infrastructure on Amazon Web Services (AWS). 
(And I'm about to start another one.)
Over the course of these projects, I've refined my development environment into something that I think is useful to share, so read on for how to make Python, Node, and Serverless.com work together and work independently from your other projects. 

## About "Serverless"
"Serverless" is both a term for a kind of computing environment and the name of a framework that helps manage such environments. 
As a computing environment, "serverless" abstracts away the needs to manage the servers and underlying operating systems from the task of writing and running code. 
If you assume that a fully-patched server at the required capacity is ready and waiting to run your code, then a serverless environment allows the developer to focus on just running the code. 
Someone else will deal with the other parts. 
AWS' {% include robustlink.html href="https://aws.amazon.com/lambda/" versionurl="https://web.archive.org/web/20220203233402/https://aws.amazon.com/lambda/" versiondate="2022-02-06" title="AWS Lambda home" anchor="Lambda" %}  is probably the best known, but other major cloud computing environments ({% include robustlink.html href="https://azure.microsoft.com/en-us/solutions/serverless/" versionurl="https://web.archive.org/web/20220130081538/https://azure.microsoft.com/en-us/solutions/serverless/" versiondate="2022-02-06" title="Microsoft Azure serverless home" anchor="Microsoft Azure" %}, {% include robustlink.html href="https://cloud.google.com/serverless" versionurl="https://web.archive.org/web/20220130081537/https://cloud.google.com/serverless" versiondate="2022-02-06" title="Google Cloud Serverless Computing home" anchor="Google Cloud Services" %}, {% include robustlink.html href="https://workers.cloudflare.com/" versionurl="https://web.archive.org/web/20220205042656/https://workers.cloudflare.com/" versiondate="2022-02-06" title="Cloudflare Workers home" anchor="Cloudflare Workers" %}) and datacenter tools ({% include robustlink.html href="https://openwhisk.apache.org/" versionurl="https://web.archive.org/web/20220131231901/https://openwhisk.apache.org/" versiondate="2022-02-06" title="Apache OpenWhisk home" anchor="Apache OpenWhisk" %}, {% include robustlink.html href="https://github.com/vmware-archive/kubeless" versionurl="https://web.archive.org/web/20220120222512/https://github.com/vmware-archive/kubeless" versiondate="2022-02-06" title="Kubeless home" anchor="Kubeless" %}) have the same thing.

"{% include robustlink.html href="https://www.serverless.com/" versionurl="https://web.archive.org/web/20220205182227/https://www.serverless.com/" versiondate="2022-02-06" title="Serverless home" anchor="serverless.com" %} " is also the name of a specific framework that helps developers manage serverless environments. 
It takes care of the tasks of bundling up code, setting up the appropriate triggers (web APIs, message queues, etc.), managing versions, and similar tasks. 
To make matters even more confusing, "Serverless.com" is also a service for managing workloads in serverless environments...so hopefully you can see that talking about "serverless" quickly gets one to "what 'serverless' are you talking about?" 
As far as understanding serverless-the-framework, I recommend skipping the homepage and going right to the {% include robustlink.html href="https://www.serverless.com//framework/docs" versionurl="https://web.archive.org/web/20220201150300/https://www.serverless.com//framework/docs" versiondate="2022-02-06" title="Serverless Framework documentation" anchor="framework documentation" %}.

## Building Up the Environment
There is one globally-installed prerequisite that I use: _pipenv_. 
Pipenv creates isolated Python environments...the python executable and installed modules for the project are separated from those of the underlying operating system. 
There are many isolated Python environment tools—{% include robustlink.html href="https://pipenv.pypa.io/en/latest/" versionurl="https://web.archive.org/web/20220205152150/https://pipenv.pypa.io/en/latest/" versiondate="2022-02-06" title="Pipenv home" anchor="pipenv" %}, {% include robustlink.html href="https://virtualenv.pypa.io/en/latest/" versionurl="https://web.archive.org/web/20220205151122/https://virtualenv.pypa.io/en/latest/" versiondate="2022-02-06" title="Virtualenv home" anchor="virtualenv" %}, {% include robustlink.html href="https://python-poetry.org/" versionurl="https://web.archive.org/web/20220206014227/https://python-poetry.org/" versiondate="2022-02-06" title="Poetry home" anchor="poetry" %}—but I've used pipenv for a long time and it has the advantage of working with Eugene Kalinin's {% include robustlink.html href="https://ekalinin.github.io/nodeenv/" versionurl="https://web.archive.org/web/20200909224018/https://ekalinin.github.io/nodeenv/" versiondate="2022-02-06" title="Nodeenv homepage" anchor="nodeenv" %} project: a Node isolation tool that integrates with pipenv. 
In other words, in one directory I'm getting both Python isolation and Node isolation.

The numbered steps below are the sequence of commands to set this up. If you want to see what an empty shell looks like—along with some strong opinions about how I like to set up Serverless for myself—check out this GitHub repository: [dltj/serverless-template](https://github.com/dltj/serverless-template).

1. `mkdir serverless_project && cd serverless_project` — create an empty directory and change into it
1. `PIPENV_VENV_IN_PROJECT=1 pipenv install` — create an isolated installation of Python in this environment _[note 1]_
1. `pipenv install --dev nodeenv` — install the 'nodeenv' package in the isolated Python environment
1. `pipenv shell` — enter the isolated Python environment
1. `nodeenv -p` — install node in the isolated Python environment and hook into the pipenv script
1. `npm install serverless` — install Serverless into the node environment and pin version in `package.json` _[note 2]_
1. `exit` — For serverless to install correctly in the environment...
1. `pipenv shell` — ...we need to exit out and re-enter the environment
1. `npm install -g serverless` — add the Serverless commands into the Python environment (`.venv/bin`) _[note 3]_
1. `npm install --include=dev serverless-python-requirements` — we're probably going to want to use the {% include robustlink.html href="https://www.serverless.com/plugins/serverless-python-requirements/" versionurl="https://web.archive.org/web/20210506102713/https://www.serverless.com/plugins/serverless-python-requirements/" versiondate="2022-02-06" title="Serverless Python Requirements plugin" anchor="serverless-python-requirements" %}  plug-in since we are developing the AWS Lambdas in Python

You are then ready to start your serverless framework development using the `serverless` command to build an empty shell.

_Note 1_: I also have a stong preference for putting the Python virtual environment in the directory where the code lives, hence the `PIPENV_VENV_IN_PROJECT=1` environment variable fed into the `pipenv` command.

_Note 2_: At this point, you can also specify a version of the Serverless framework. As I'm writing this, Serverless jumped to a 3.x.x version but I'm waiting for that major release to settle down. So I use `npm install serverless@2.72.2`

_Note 3_: Although the `-g` global flag is being used, we are inside the Python environment at this point so the Serverless install is in the Python/Node environment. Note, too, that this command "globally" installs the version pinned in `package.json` from the earlier `npm install` command.

## How Others Use Your Environment
With the versions of commands and dependencies pinned in their respective Python and Node package files, someone can reproduce the same isolated Python/Node environment with these commands.
Add these instructions to your README file:

> 1. `git clone serverless_project && cd serverless_project`
> 2. `PIPENV_VENV_IN_PROJECT=1 pipenv install` # create an isolated installation of Python in this environment
> 3. `pipenv shell` 
> 4. `nodeenv -p` # Installs Node environment inside Python environment
> 5. `npm install --include=dev` # Installs Node packages inside combined Python/Node environment
> 6. `exit` # For serverless to install correctly in the environment...
> 7. `pipenv shell` # ...we need to exit out and re-enter the environment
> 8. `npm install -g serverless` # Although the '-g' global flag is being used, Serverless install is in the Python/Node environment
