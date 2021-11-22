import os
import boto3
from boto3.s3.transfer import S3Transfer
from dotenv import load_dotenv

load_dotenv()


def get_s3_client():
    credentials = {
        "aws_access_key_id": os.getenv("ACCOUNT_ID"),
        "aws_secret_access_key": os.getenv("ACCESS_KEY"),
    }
    client = boto3.client("s3", "ap-southeast-1", **credentials)
    return client


def upload_file(client, file_path, key_file):
    transfer = S3Transfer(client)
    transfer.upload_file(
        file_path, os.getenv("BUCKET_NAME"), key_file, extra_args={"ACL": "public-read"}
    )
    os.remove(file_path)


def get_public_url(client, key_file):
    file_url = "%s/%s/%s" % (client.meta.endpoint_url, os.getenv("BUCKET_NAME"), key_file)
    return file_url


def download_file(bucket, file_name, file_path):
    bucket.download_file(file_name, file_path)
