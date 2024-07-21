---
title: 'You''re getting &quot;Invalid request provided: AWS::CloudFront::PublicKey&quot; because CloudFront Public Keys are immutable'
modified: 2022-02-11T22:01:06-05:00
categories:
- Raw Technology
tags:
- Amazon Web Services
---

This is the web page I wish I had found when I spent the afternoon sorting through why AWS CloudFormation kept telling me:

> Resource handler returned message: "Invalid request provided: AWS::CloudFront::PublicKey"

Like me, you might be working on a Serverless.com stack and are trying to restrict access to items in an S3 bucket through CloudFront. 
You might even be putting the public key text block into a YAML multiline string in an external configuration file and pulling that into your `serverless.yml` file. 
And you are pulling your hair out because when you run updates on your stack, you get this error. 
So in frustration, you blow away the stack and recreate it.
It works fine at first, but soon you are back at that same error above. 
Do you want to know why?

_An **AWS::CloudFront::PublicKey** resource is immutable, you idiot._  (Me idiot, actually.  Hopefully you are fortunate in finding this page early in your quest to solve the problem.)

The clue came from {% include robustlink.html href="https://github.com/aws-cloudformation/cloudformation-coverage-roadmap/issues/924" versionurl="https://web.archive.org/web/20220212021021/https://github.com/aws-cloudformation/cloudformation-coverage-roadmap/issues/924" versiondate="2022-02-11" title="Updating AWS::CloudFront::PublicKey results in BadRequest error |  aws-cloudformation/cloudformation-coverage-roadmap" anchor="this issue report in the CloudFormation coverage roadmap page" %}:

> As mentioned in the API documentation : [UpdatePublicKey](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_UpdatePublicKey.html)  
UpdatePublicKey action lets you update just the **Comment** field. The values **EncodedKey** and **Name** are immutable, and cannot be updated once created. To update the Key or the Name, a new PublicKey must be created using CreatePublicKey and use it. 

The resources section of my `serverless.yml` file looks like this:

{% highlight yaml linenos %}
    WebsiteDistributionPublicKey:
      Type: AWS::CloudFront::PublicKey
      Properties:
        PublicKeyConfig:
          Name: ${self:custom.stack_name}
          CallerReference: ${self:custom.config.PUBLIC_KEY_CALLER_REFERENCE}
          EncodedKey: ${self:custom.config.PUBLIC_KEY_ENCODED}
{% endhighlight %}

I'm using {% include robustlink.html href="https://www.richdevelops.dev/blog/keeping-secrets-out-of-git" versionurl="https://web.archive.org/web/20220212021821/https://www.richdevelops.dev/blog/keeping-secrets-out-of-git" versiondate="2022-02-11" title="Keeping secrets out of Git" anchor="Rich Buggy's 'Keeping secrets out of Git' technique" %} to store secrets outside of the `serverless.yml` file, so I have a custom section that looks like this:

{% highlight yaml linenos %}
custom:
  default_stage: dev
  stage: ${opt:stage, self:custom.default_stage}
  stack_name: ${self:service}-${self:custom.stage}
  config: ${file(config.yml):${self:custom.stage}}
{% endhighlight %}

... which reads in this file:

{% highlight yaml linenos %}
default: &default
  <<: *default
  PUBLIC_KEY_CALLER_REFERENCE: SomeRandomString
  PUBLIC_KEY_ENCODED: |
    -----BEGIN PUBLIC KEY-----
    MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwU37058NQTUqEHBor95x
    VZ1iezIzZB7MWoYHt4KCRDVw5G3h/pzDKLu2NKo+rVOBztgQ+cefdqBNWa2Mf4Tl
    YQxOP9m978C2f4H9tc8c2px9Lxdkh27Vd8xZx/JHPvnqTUYP/p6WNa+jLVm6TV7a
    mL5QqrURd9OpOoyrfKmzhkJwrBxhT8WlchKmnd3S+dotAFdOgb8aABtdIEoCvKYq
    +MeAeBrsE1UhennDU/yWfNl2deGUCUnhkWPHDmLgObr/iYGZamdnp6InjUX2PLsC
    leQuc1M13904QKX+0wfUNin6IK9Pn+UmLupQSg0ou533Nxkw69KLZRAvoOHJlZJW
    BwIDAQAB
    -----END PUBLIC KEY-----
{% endhighlight %}

... and populates the variables you saw in the fragment at the top. 
(If you've read this far and are interested in how I set up serverless.com projects, check out the [blog post I wrote earlier this week]({% post_url 2022-02-06-starting-python-serverless-project %}) on the topic.)

The practical upshot is if any three of those properties need to change—`Name`, `CallerReference`, or `EncodedKey`—what you must do is either:

1. Change the name of the resource—`WebsiteDistributionPublicKey` at line 1 in the YAML at the top—in some way (add a letter to the name, remove a letter, etc.) in addition to updating the resource properties, or
2. Comment out the entire `AWS::CloudFront::PublicKey` resource, deploy (to delete it), uncomment and modify, then deploy again.

As the [commenter on the issue mentioned above said](https://github.com/aws-cloudformation/cloudformation-coverage-roadmap/issues/924#issuecomment-957685979), this is not common behavior for other AWS services in CloudFormation. 
Hopefully, AWS will give us a CloudFormation path that is cleaner than the above two options.