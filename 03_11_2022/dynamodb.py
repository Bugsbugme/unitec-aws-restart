import boto3

client = boto3.client("dynamodb")

response = client.get_item(TableName="discord_messages", Key={"pk": {"S": "message#1"}})

print(response["Item"])
