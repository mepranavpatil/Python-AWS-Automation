import boto3
from botocore.exceptions import ClientError

try:

    ec2 = boto3.client("ec2")

    response = ec2.describe_instances(
        Filters=[
            {
                "Name": "instance-state-name",
                "Values": ["stopped"]
            }
        ]
    )

    instance_ids = []

    for reservation in response["Reservations"]:

        for instance in reservation["Instances"]:

            instance_ids.append(
                instance["InstanceId"]
            )

    print("\nSTOPPED INSTANCES\n")

    if instance_ids:

        for instance_id in instance_ids:
            print(instance_id)

        ec2.start_instances(
            InstanceIds=instance_ids
        )

        print("\nInstances Started Successfully")

    else:

        print("No stopped instances found")

except ClientError as e:

    print("AWS Error:", e)

except Exception as e:

    print("Unexpected Error:", e)