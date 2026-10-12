import os
import boto3
from dotenv import load_dotenv

def test_aws_connection():

    load_dotenv()

    access_key = os.getenv("AWS_ACCESS_KEY_ID")
    secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
    region = os.getenv("AWS_DEFAULT_REGION")
    bucket_name = os.getenv("AWS_S3_BUCKET_NAME")

    print("Testing AWS Connection")
    print(f"region: {region}")
    print(f"Bucket: {bucket_name}")

    try:
        # Create S3 client
        s3 = boto3.client(
            "s3", 
            aws_access_key = access_key,
            aws_secret_key = secret_key,
            region_name = region
        )

        # List you buckets
        buckets = s3.list_bucket()
        print(f"Connected! you have {len(buckets["Buckets"])} S3 buckets")

        return True
    except Exception as w:
        print(f"Connection Failed: {e}")
        print("Check you .env file and aws credentials")

        return False

if __name__ == "__main__":
    test_aws_connection()