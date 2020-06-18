class S3Connector:
    def __init__(self, user_id, user_pass, host, bucket):
        self.user_id = user_id
        self.user_pass = user_pass
        self.host = host
        self.bucket = bucket
