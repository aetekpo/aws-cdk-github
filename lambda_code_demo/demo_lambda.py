import json

def lambda_handler(event, context):
    print("Event received:", event)

    return {
        "statusCode": 200,
        "body": json.dumps("Hello from Lambda powered by CDK-GitHub!")
    }

