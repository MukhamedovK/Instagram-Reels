import uuid
import boto3
from botocore.client import Config
from environs import Env

from .models import Like

env = Env()
env.read_env()

AWS_ACCESS_KEY_ID = env.str("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env.str("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = env.str("AWS_STORAGE_BUCKET_NAME")
AWS_S3_REGION_NAME = env.str("REGION_NAME")
AWS_S3_ENDPOINT_URL = env.str("ENDPOINT_URL")


class TimewebS3:
    def __init__(self):
        self.client = boto3.client(
            "s3",
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            endpoint_url=AWS_S3_ENDPOINT_URL,
            region_name=AWS_S3_REGION_NAME,
            config=Config(s3={'addressing_style': 'path'}),
        )


def like_status(serializer, user):
    for data in serializer.data:
        data['you_liked'] = Like.objects.filter(user=user, liked_video__id=data['id']).exists()
    
    return serializer

