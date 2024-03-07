from fastapi import UploadFile
import boto3
import logging
from botocore.exceptions import ClientError
from .config import settings

s3 = boto3.resource('s3')
    
def get_all_buckets():
    
    return [bucket.name for bucket in s3.buckets.all()  ]

def bucket_exist():
    if settings.BUCKET_NAME in get_all_buckets():
        return True
    return False
    
    
    
    

def create_bucket(bucket_name, region=None):
    """ Create a bucket, region defaults to us-east-1"""
    # Create bucket
    if bucket_exist():
        print("Bucket Exists")
        return False
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True


    


# print('List all buckets: ', get_all_buckets())
# if BUCKET_NAME not in get_all_buckets():
#     created_bucket = create_bucket(BUCKET_NAME)
# else:
#     print(f'{BUCKET_NAME} already bucket_exist')

    
    






