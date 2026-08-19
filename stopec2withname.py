import boto3
from botocore.exceptions import ClientError

try:

    ec2 = boto3.client("ec2")

    instance_name = input("Enter EC2 Name to Stop: ")

    response = ec2.describe_instances(
        Filters=[
            {
                "Name": "tag:Name",
                "Values": [instance_name]
            },
            {
                "Name": "instance-state-name",
                "Values": ["running"]
            }
        ]
    )

    instance_ids = []

    for reservation in response["Reservations"]:

        for instance in reservation["Instances"]:

            instance_ids.append(
                instance["InstanceId"]
            )

    if instance_ids:

        ec2.stop_instances(
            InstanceIds=instance_ids
        )

        print(f"\nStopped instance: {instance_name}")

    else:

        print(
            f"\nNo running instance found with name: {instance_name}"
        )

except ClientError as e:

    print("AWS Error:", e)

except Exception as e:

    print("Unexpected Error:", e)