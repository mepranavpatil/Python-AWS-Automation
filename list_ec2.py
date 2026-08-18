import boto3
from botocore.exceptions import ClientError

try:
    # Connect to EC2
    ec2 = boto3.client("ec2")

    # Retrieve EC2 information
    response = ec2.describe_instances()

    print("===================================")
    print("AWS EC2 CONNECTION SUCCESSFUL")
    print("===================================")

    print(f"Reservations Found: {len(response['Reservations'])}")

except ClientError as e:
    print("AWS Error:", e)

except Exception as e:
    print("Unexpected Error:", e)