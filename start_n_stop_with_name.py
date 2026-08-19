import boto3
from botocore.exceptions import ClientError

try:

    ec2 = boto3.client("ec2")

    action = input("Choose action (start/stop): ").lower()
    instance_name = input("Enter EC2 Name: ")

    if action == "start":

        response = ec2.describe_instances(
            Filters=[
                {
                    "Name": "tag:Name",
                    "Values": [instance_name]
                },
                {
                    "Name": "instance-state-name",
                    "Values": ["stopped"]
                }
            ]
        )

    elif action == "stop":

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

    else:

        print("Invalid action")
        exit()

    instance_ids = []

    for reservation in response["Reservations"]:

        for instance in reservation["Instances"]:

            instance_ids.append(
                instance["InstanceId"]
            )

    if not instance_ids:

        print(
            f"No matching instances found for '{instance_name}'"
        )
        exit()

    if action == "start":

        ec2.start_instances(
            InstanceIds=instance_ids
        )

        print(
            f"Successfully started '{instance_name}'"
        )

    elif action == "stop":

        ec2.stop_instances(
            InstanceIds=instance_ids
        )

        print(
            f"Successfully stopped '{instance_name}'"
        )

except ClientError as e:

    print("AWS Error:", e)

except Exception as e:

    print("Unexpected Error:", e)