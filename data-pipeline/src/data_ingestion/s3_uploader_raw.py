
import os
import boto3
from pathlib import Path
from dotenv import load_dotenv

def upload_data_to_s3():
    """Upload data from data/raw/ to S3 bucket"""
    
    print("Starting data upload to S3...")
    
    # Load environment variables
    load_dotenv()
    
    # Get AWS credentials from .env file
    bucket_name = os.getenv('AWS_S3_BUCKET_NAME')
    region = os.getenv('AWS_DEFAULT_REGION', 'us-east-1')
    
    if not bucket_name:
        print("ERROR: AWS_S3_BUCKET_NAME not found in .env file!")
        return False
    
    print(f"Bucket: {bucket_name}")
    print(f"Region: {region}")
    
    try:
        # Create S3 client
        s3 = boto3.client('s3', region_name=region)
        
        # Create bucket if it doesn't exist
        try:
            s3.head_bucket(Bucket=bucket_name)
            print(f"Bucket '{bucket_name}' exists")
        except:
            print(f"Creating bucket '{bucket_name}'...")
            if region == 'us-east-1':
                s3.create_bucket(Bucket=bucket_name)
            else:
                s3.create_bucket(
                    Bucket=bucket_name,
                    CreateBucketConfiguration={'LocationConstraint': region}
                )
            print(f"Bucket created!")

        
        # Find CSV files in data/raw/
        data_folder = Path("../../data/raw")

        if not data_folder.exists():
            data_folder = Path("data/raw")

        if not data_folder.exists():
            print("ERROR: Data folder not found!")
            print("Make sure you have data/raw CSV files")
            return False
        
        # Get list of CSV files
        csv_files = list(data_folder.glob("*.csv"))
 

        # Upload each file

 

        # Verification

     

if __name__ == "__main__":
    # Run upload
    success = upload_data_to_s3()
    
    # Verify if upload was successful
    if success:
        verify_upload()
    
    print("\nNext step: Data processing and transformation!")
