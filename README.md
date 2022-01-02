## What is this?

/src contains source code that can be deployed as a Lambda using SAM.

The /serverless* dirs contain source code that can be deployed as Lambda using serverless.


# Serverless lazydog:

Install and configure:

```
# install serverless
npm install -g serverless

# configure serverless
serverless config credentials --provider aws --key XXX --secret XXX --profile serverless-admin
```

Using serverless:

```
# create new project:
sls create --template aws-python3 --path serverless_deployment

# Deploy the code (from the source directory):
sls deploy --verbose

# to enable the installation from requirements.txt
serverless plugin install -n serverless-python-requirements

# deploy new function version:
sls deploy function -f hello

# call func from CLI:
sls invoke -f serverless -l

# tailing the log:
sls logs -f serverless -t

# remove the function (from the source dir):
sls remove
```

# SAM lazydog:

This repo contains a `template.yaml` and a `samconfig.toml`, both of which will be used when building/deploying:

```
sam build
sam build --config-file samconfig.toml

sam package
sam deploy


# alternatively:
aws cloudformation deploy

# invoke the lambda using AWS cli:
aws lambda invoke --function-name klundert-lambda-sam-helloworldpython3-6BxLjAQrMYOi output.txt

```

Deployment log:

```
PS C:\dev-container\lambda> sam build 
Building codeuri: C:\dev-container\lambda\src runtime: python3.9 metadata: {} architecture: x86_64 functions: ['helloworldpython3']
Running PythonPipBuilder:ResolveDependencies
Running PythonPipBuilder:CopySource

Build Succeeded

Built Artifacts  : .aws-sam\build
Built Template   : .aws-sam\build\template.yaml

=========================
[*] Invoke Function: sam local invoke
[*] Test Function in the Cloud: sam sync --stack-name {stack-name} --watch
[*] Deploy: sam deploy --guided

PS C:\dev-container\lambda> sam deploy
Uploading to klundert-lambda-sam/3ea69bc99e8367dc3b93f73de991a830  636792 / 636792  (100.00%)

        Deploying with following values
        ===============================
        Stack name                   : klundert-lambda-sam
        Region                       : eu-central-1
        Confirm changeset            : True
        Disable rollback             : True
        Deployment s3 bucket         : aws-sam-cli-managed-default-samclisourcebucket-ezr5g6jw5nlo
        Capabilities                 : ["CAPABILITY_IAM"]
        Parameter overrides          : {}
        Signing Profiles             : {}

Initiating deployment
=====================
Uploading to klundert-lambda-sam/61303e4423a1b72e97f05d1862c321dd.template  919 / 919  (100.00%)

Waiting for changeset to be created..

CloudFormation stack changeset
-------------------------------------------------------------------------------------------------------------------------------------------------
Operation                            LogicalResourceId                    ResourceType                         Replacement
-------------------------------------------------------------------------------------------------------------------------------------------------   
* Modify                             helloworldpython3                    AWS::Lambda::Function                False
-------------------------------------------------------------------------------------------------------------------------------------------------

Changeset created successfully. arn:aws:cloudformation:eu-central-1:717687450252:changeSet/samcli-deploy1640932913/98fd6787-97c2-4df6-a2cc-613bc2be2d34


Previewing CloudFormation changeset before deployment
======================================================
Deploy this changeset? [y/N]: y

2021-12-31 07:42:08 - Waiting for stack create/update to complete

CloudFormation events from stack operations
-------------------------------------------------------------------------------------------------------------------------------------------------
ResourceStatus                       ResourceType                         LogicalResourceId                    ResourceStatusReason
-------------------------------------------------------------------------------------------------------------------------------------------------   
UPDATE_IN_PROGRESS                   AWS::Lambda::Function                helloworldpython3                    -
UPDATE_COMPLETE                      AWS::Lambda::Function                helloworldpython3                    -
UPDATE_COMPLETE_CLEANUP_IN_PROGRES   AWS::CloudFormation::Stack           klundert-lambda-sam                  -
S
UPDATE_COMPLETE                      AWS::CloudFormation::Stack           klundert-lambda-sam                  -
-------------------------------------------------------------------------------------------------------------------------------------------------   

Successfully created/updated stack - klundert-lambda-sam in eu-central-1
```

# Serverless

Install nodejs, then:
```
npm install -g serverless
```

Setup serverless:
```
serverless config credentials --provider aws --key XXX --secret XXX --profile serverless-admin
```

Create a new project:
```
sls create --template aws-python3 --path sls_hello_world
```

Do some work on the code, and then:
```
sls deploy --verbose
```

On AWS, the output ends with something like this:

```
Serverless: Stack update finished...
Service Information       
service: sls-hello-world  
stage: dev
region: eu-central-1      
stack: sls-hello-world-dev
resources: 6
api keys:
  None
endpoints:
functions:
  hello: sls-hello-world-dev-hello
layers:
  None

Stack Outputs
HelloLambdaFunctionQualifiedArn: arn:aws:lambda:eu-central-1:717687450252:function:sls-hello-world-dev-hello:1
ServerlessDeploymentBucketName: sls-hello-world-dev-serverlessdeploymentbucket-77tgtks5cf10
```

After this, you can invoke the function from the CLI:

```
PS C:\dev-container\aws\LAMBDA\sls_hello_world> sls invoke -f hello -l
{
    "statusCode": 200,
    "body": "{\"message\": \"Go Serverless v1.0! Your function executed successfully!\", \"input\": {}}" 
}
--------------------------------------------------------------------
START RequestId: 55a0e327-4e39-4aeb-a020-62849f5a8575 Version: $LATEST
END RequestId: 55a0e327-4e39-4aeb-a020-62849f5a8575
REPORT RequestId: 55a0e327-4e39-4aeb-a020-62849f5a8575  Duration: 0.93 ms       Billed Duration: 1 ms   Memory Size: 1024 MB     Max Memory Used: 37 MB
```

For minor updates to the function after the initial deployment, you can use:
```
sls deploy function -f hello
```

# Links

[serverless examples](https://github.com/serverless/examples)
[serverless community examples](https://github.com/serverless/examples#community-examples)