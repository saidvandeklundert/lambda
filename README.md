# Serverless in AWS

## Intro

Serverless: you do not have to manage the servers (of )
Number of services that can be leveraged in a 'serverless' fashion:
- Lambda
- API Gateway
- S3
- SNS
- SQS
- DynamoDB
- Cognito
- Step functions
- CloudWatch Events / Logs
- Kinesis


Lambda can act as the nexus of serverless, tying everything together.

There are 'native' integrations between AWS services and Lambda. With native, I mean you can combine the features of certain products together with Lambda. 

In addition to this, many other integrations can be done through code. Either the SDK or, if you are using Python, boto3.

## Lamdba

Functions that can run on demand and no servers to tend to.

Functions are executed inside a container.

## Deploying Lambda

Can be done using:
- AWS console
- CloudFormation
- SAM
- Serveless framework


## Logging from your Lambda

Your Lambda comes with a CloudWatch Logs group out of the box. Everything that is written to `stdout` or `stderr` will be sent to CloudWatch.

Log groups: arbitrary name, usually representing an application
Log stream: instances within application / log file / container



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
sls create --template aws-python3 --path sls_hello_world

# Do some work on the code, and then deploy it (will read requirements.txt):
sls deploy --verbose

# deploy new function version:
sls deploy function -f hello

# call func from CLI:
sls invoke -f hello -l

# tailing the log:
sls logs -f hello -t

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

# alternatively, use guided. This will ask for confirmation:
sam deploy --guided

# alternatively:
aws cloudformation deploy

# invoke the lambda using AWS cli:
aws lambda invoke --function-name klundert-lambda-sam-helloworldpython3-6BxLjAQrMYOi output.txt

# cleaning up:
klundert-lambda-sam
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
# Links

[serverless examples](https://github.com/serverless/examples)
[serverless community examples](https://github.com/serverless/examples#community-examples)
[Lambda pricing](https://aws.amazon.com/lambda/pricing/)
[Lambda logging](https://docs.aws.amazon.com/lambda/latest/dg/python-logging.html)

# Handy



Create a user called serverless-admin with required privileges. Only needs access-key and secret access-key.



Note for windows:
https://stackoverflow.com/questions/43302843/serverless-framework-sls-conflicts-with-powershell-sls-select-string

Create a powershell profile and remove the default (conflicting) sls alias:
```
notepad $profile
remove-item alias:sls
```


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


