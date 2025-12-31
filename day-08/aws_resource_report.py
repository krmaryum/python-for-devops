# Imports (tools we need)
import json  # to convert Python data into JSON format
from datetime import datetime, timezone   # to add the current time to the report

import boto3  # AWS SDK for Python (used to talk to AWS)
from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError, PartialCredentialsError # used to catch errors (like missing credentials)

# The AWSUtils class
class AWSUtils: # A class is a blueprint. This class groups all AWS-related methods (functions) together.
    # __init__ – setup AWS connection
    def __init__(self):
        # Prefer a Session so we can easily get regions and identity consistently
        self.session = boto3.session.Session()   # reads AWS credentials & config
        self.s3 = self.session.client("s3")      # creates an S3 client
    # get_connection() – generic AWS client creator [Create a client for any AWS service e.g. EC2, S3, STS, etc.]
    def get_connection(self, service, region_name=None):
        return self.session.client(service, region_name=region_name)

    # Lists all S3 buckets
    def list_buckets(self):
        response = self.s3.list_buckets() # Calls AWS and gets all buckets
        buckets = []                      # list into variable "buckets"
        for bucket in response.get("Buckets", []): # Extracts only bucket names, Stores them in a list
            buckets.append(bucket.get("Name"))
        return buckets   # e.g. ["my-bucket-1", "logs-bucket", "backup-bucket"]

    # Listing EC2 instances across ALL regions
    def list_ec2_instances_all_regions(self):
        # Use one “known good” region to ask AWS which regions are enabled for this account, This asks AWS: which regions are enabled for me?
        ec2_home = self.get_connection("ec2", region_name=self.session.region_name or "us-east-2")
        enabled = ec2_home.describe_regions(AllRegions=False)["Regions"]
        regions = [r["RegionName"] for r in enabled]  # Create EC2 client

        results = {}

        for region in regions:
            ec2 = self.get_connection("ec2", region_name=region)
            instances = []

            try:
                paginator = ec2.get_paginator("describe_instances")
                for page in paginator.paginate():
                    for reservation in page.get("Reservations", []):
                        for inst in reservation.get("Instances", []):
                            instances.append({
                                "instance_id": inst.get("InstanceId"),
                                "state": (inst.get("State") or {}).get("Name"),
                            })

                # include region even if empty (optional)
                results[region] = instances

            except (ClientError, BotoCoreError) as e:
                results[region] = [{"error": str(e)}]

        return results

    def get_identity(self):
        sts = self.session.client("sts")
        ident = sts.get_caller_identity()
        return {
            "account": ident.get("Account"),
            "arn": ident.get("Arn"),
            "user_id": ident.get("UserId"),
        }

    # Generate full report{Combines everything:[Current time, Identity, S3 buckets, EC2 instances]}
    def generate_report(self):
        return {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "identity": self.get_identity(),
            "s3_buckets": self.list_buckets(),
            "ec2_instances": self.list_ec2_instances_all_regions(),
        }

    def save_report_json(self, report, filename="aws_report.json"):
        with open(filename, "w",) as f:
            json.dump(report, f, indent=2) # indent=2 -> makes it human-readable

        return filename


if __name__ == "__main__": # This runs only when you run the file directly
    try:
        aws = AWSUtils()  # Create AWSUtils object(aws)

        report = aws.generate_report()  # Generate report

        # Terminal output
        print(json.dumps(report, indent=2))  #

        # JSON file output
        output_file = aws.save_report_json(report, "aws_report.json")  # Save report
        print(f"\nSaved report to: {output_file}")

    except (NoCredentialsError, PartialCredentialsError):
        print(
            "ERROR: AWS credentials not found or incomplete.\n"
            "Run: aws configure\n"
            "Or set env vars AWS_ACCESS_KEY_ID/AWS_SECRET_ACCESS_KEY (+AWS_SESSION_TOKEN if needed)."
        )
    except (ClientError, BotoCoreError) as e:
        print(f"ERROR: AWS API call failed: {e}")
