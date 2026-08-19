import boto3

ec2 = boto3.client("ec2")

instance_name = input("Enter EC2 Name: ")

response = ec2.describe_instances()

for reservation in response["Reservations"]:

    for instance in reservation["Instances"]:

        if "Tags" in instance:

            for tag in instance["Tags"]:

                if (
                    tag["Key"] == "Name"
                    and tag["Value"] == instance_name
                ):

                    instance_id = instance["InstanceId"]

                    ec2.start_instances(
                        InstanceIds=[instance_id]
                    )

                    print(
                        f"Started {instance_name} ({instance_id})"
                    )