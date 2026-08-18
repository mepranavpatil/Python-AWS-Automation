import boto3

# Create EC2 client
ec2 = boto3.client("ec2")

# Fetch EC2 information
response = ec2.describe_instances()

print(response)