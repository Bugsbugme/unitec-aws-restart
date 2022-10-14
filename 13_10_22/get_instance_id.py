# This script gets the ec2 instance id's for all running instances
# Gracie 2022/10/13
import boto3

# Creating a client object that is used to interact with the AWS API.
ec2 = boto3.client("ec2")

# Getting the instance id's of the running ec2 instances.
response = ec2.describe_instances(
    Filters=[{"Name": "instance-state-name", "Values": ["running"]}]
)
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        print(instance["InstanceId"])
