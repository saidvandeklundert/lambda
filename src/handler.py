import json
import boto3
import os
import logging

logger = logging.getLogger()

logger.setLevel(logging.INFO)
ssm = boto3.client("ssm")
PARAMETER = ssm.get_parameter(
    Name="/passwords/infrastructure/ssot_token", WithDecryption=True
)
PASSWORD = PARAMETER["Parameter"]["Value"]


def hello(event, context):
    client = boto3.client("lambda")
    response = client.list_functions()

    # Display the environment variable:
    logger.info(f"## ENVIRONMENT ENV_VAR_EXAMPLE_1: {os.environ['ENV_VAR_EXAMPLE_1']}")
    # Display all environment variables:
    logger.info("## ENVIRONMENT VARIABLES:")
    logger.info(os.environ)
    logger.warn("## WARNING")
    logger.error("## ERROR")

    logger.info(f"## SSM Parameter Store value: {PASSWORD}")

    # logging an exception:
    some_dict = {"some_key": "some_value"}
    try:
        some_dict["this_key_does_not_exist"]
    except KeyError as error:
        logger.error(f"KeyError: {error}")

    # make the lambda return something:
    body = {
        "message": "Your function executed successfully!",
        "event": event,
    }
    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
