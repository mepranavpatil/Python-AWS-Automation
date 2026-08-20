import boto3
import csv
from botocore.exceptions import ClientError

try:

    ec2 = boto3.client("ec2")

    response = ec2.describe_instances()

    with open(
        "reports/ec2_inventory.csv",
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "Instance ID",
            "Name",
            "State",
            "Type",
            "Public IP"
        ])

        for reservation in response["Reservations"]:

            for instance in reservation["Instances"]:

                name = "N/A"

                if "Tags" in instance:

                    for tag in instance["Tags"]:

                        if tag["Key"] == "Name":

                            name = tag["Value"]

                instance_id = instance["InstanceId"]

                state = instance["State"]["Name"]

                instance_type = instance["InstanceType"]

                public_ip = instance.get(
                    "PublicIpAddress",
                    "N/A"
                )

                writer.writerow([
                    instance_id,
                    name,
                    state,
                    instance_type,
                    public_ip
                ])

    print(
        "Report generated successfully:"
    )
    print(
        "reports/ec2_inventory.csv"
    )

except ClientError as e:

    print("AWS Error:", e)

except Exception as e:

    print("Unexpected Error:", e)