from base import *  # noqa

ALLOWED_HOSTS = ['localhost', '.execute-api.us-east-1.amazonaws.com']

AWS_QUERYSTRING_AUTH = False
AWS_ACCESS_KEY_ID = 'AKIAIAXGGQ5APIHMBKFA'
AWS_SECRET_ACCESS_KEY = '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'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_STORAGE_BUCKET_NAME = 'zappa-lambda-static'
AWS_LOCATION = 'admin-staging'
