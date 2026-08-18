import boto3
from botocore.exceptions import ClientError
from tabulate import tabulate

try:

    ec2 = boto3.client("ec2")

    response = ec2.describe_instances()

    table_data = []

    for reservation in response["Reservations"]:

        for instance in reservation["Instances"]:

            name = "N/A"

            if "Tags" in instance:

                for tag in instance["Tags"]:

                    if tag["Key"] == "Name":
                        name = tag["Value"]

            table_data.append([
                instance["InstanceId"],
                instance["State"]["Name"],
                instance["InstanceType"],
                name
            ])

    print("\nEC2 INVENTORY REPORT\n")

    print(
        tabulate(
            table_data,
            headers=[
                "Instance ID",
                "State",
                "Type",
                "Name"
            ],
            tablefmt="grid"
        )
    )

except ClientError as e:
    print("AWS Error:", e)

except Exception as e:
    print("Unexpected Error:", e)