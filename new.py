import os
from unittest.mock import patch

os.environ.setdefault('AWS_DEFAULT_REGION', 'us-east-2')
os.environ.setdefault('AWS_ACCESS_KEY_ID', 'testing')
os.environ.setdefault('AWS_SECRET_ACCESS_KEY', 'testing')


def mock_get_ssm_parameter(param_name):
    defaults = {
        '/cognito/user-pool-id': 'us-east-2_test',
        '/cognito/client-id': 'test-client-id',
        '/opensearch/host': 'localhost',
        '/opensearch/port': '9200',
        '/opensearch/username': 'admin',
        '/opensearch/password': 'admin',
        '/jira/url': None,
        '/jira/token': None,
        '/jira/username': None,
    }
    if '/port' in param_name:
        return defaults.get(param_name, '3306')
    return defaults.get(param_name, 'test_value')


_ssm_patcher = patch('app.core.aws.ssm.get_ssm_parameter', side_effect=mock_get_ssm_parameter)
_ssm_patcher.start()
