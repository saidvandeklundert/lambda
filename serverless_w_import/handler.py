import json
import requests


def hello(event, context):
    resp = requests.get("https://whatismyipaddress.com/")
    what_is_my_ipaddress = ""
    for line in resp.text.splitlines():
        if "your ip address" in line.lower():
            what_is_my_ipaddress = line
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event,
        "whatismyipaddress": what_is_my_ipaddress,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
