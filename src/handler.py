import json
import boto3
import os
import logging

logger = logging.getLogger()

logger.setLevel(logging.INFO)
ssm = boto3.client("ssm")
PARAMETER = ssm.get_parameter(
    Name="/passwords/infrastructure/switch-password", WithDecryption=True
)
PASSWORD = PARAMETER["Parameter"]["Value"]


def hello(event, context):
    client = boto3.client("lambda")
    response = client.list_functions()

    logger.info("## ENVIRONMENT VARIABLES:")
    logger.info(os.environ)
    logger.info("## ENVIRONMENT ENV_VAR_EXAMPLE_1:")
    example_env_var = os.environ["ENV_VAR_EXAMPLE_1"]
    logger.info("## EVENT")
    logger.info(event)
    logger.info("## PARAMETER:")
    logger.info(PASSWORD)
    body = {
        "message": "Your function executed successfully!",
        "event": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}
    # pprint(body)
    return response
