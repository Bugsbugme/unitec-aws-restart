# This script will create a new ec2 instance in the AWS cloud
from ec2_setup import create_instance

create_instance("ami-08e2d37b6a0129927", "t3.micro", "vockey")
print("New ec2 instance has been created.")
