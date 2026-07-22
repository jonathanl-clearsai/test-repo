class SSMService:
    def __init__(self, region: str = None):
      self.region = region or settings.aws_region
      self.ssm = boto3.client("ssm", region_name=self.region)
      self._cache: dict = {}
