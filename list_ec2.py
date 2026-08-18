import boto3
from botocore.exceptions import ClientError

try:
    ec2 = boto3.client("ec2")

    response = ec2.describe_instances()

    print("Connection Successful")
    print("Reservations Found:", len(response["Reservations"]))

except ClientError as e:
    print("AWS Error:", e)

except Exception as e:
    print("Unexpected Error:", e)