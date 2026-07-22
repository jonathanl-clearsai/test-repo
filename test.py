import boto3

class SSMService:
    def __init__(self, region: str = None):
      self.region = region or settings.aws_region
      self.ssm = boto3.client("ssm", region_name=self.region)
      self._cache: dict = {}
        
    def _get_parameter(self, path: str, decrypt: bool = True, skip_cache: bool = False) -> Optional[str]:
        if not skip_cache and path in self._cache:
            return self._cache[path]

        try:
            response = self.ssm.get_parameter(
                Name=path,
                WithDecryption=decrypt,
            )
            value = response["Parameter"]["Value"]
            if not skip_cache:
                self._cache[path] = value
            return value

        except self.ssm.exceptions.ParameterNotFound:
            logger.warning("SSM parameter not found", path=path)
            return None

        except Exception as e:
            logger.exception("Error fetching SSM parameter", path=path, error=str(e))
            return None
