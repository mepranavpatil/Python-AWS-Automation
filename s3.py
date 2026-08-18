import boto3
from botocore.exceptions import ClientError

try:
    s3 = boto3.client("s3")

    response = s3.list_buckets()

    print("Connection Successful")
    print("Buckets Found:", len(response["Buckets"]))

except ClientError as e:
    print("AWS Error:", e)

except Exception as e:
    print("Unexpected Error:", e)