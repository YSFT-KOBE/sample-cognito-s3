import boto3

class S3:
    def __init__(self, acskey, scretkey, ssntokn):
        self.s3 = boto3.client('s3',
                aws_access_key_id=acskey,
                aws_secret_access_key=scretkey,
                aws_session_token = ssntokn,
                region_name='<<Region>>'
        )

    def upload(self, filename, bucket, key):
        self.s3.upload_file(filename, bucket, key)