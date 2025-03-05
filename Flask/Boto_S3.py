from flask import Flask, request, jsonify
import boto3
import os

app = Flask(__name__)

#AWS S3 configuration
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
AWS_REGION = "us-east-1"
S3_BUCKET = "BUCKET_NAME"

#Intiliaze S3 client
S3_client = boto3.client(
    "s3",
    aws_access_key_id = AWS_ACCESS_KEY,
    aws_secret_access_key = AWS_SECRET_KEY,
    region_name = AWS_REGION
)

@app.route("/list-logs", methods=["GET"])
def list_logs():
    """Fetch list of logs from s3 bucket"""
    try:
        objects = S3_client.list_objects_v2(Bucket = S3_BUCKET)
        if "Contents" in objects:
            files = [obj["key"] for obj in objects["Contents"]]