from base import *  # noqa

ALLOWED_HOSTS = ['localhost', '.execute-api.ap-southeast-1.amazonaws.com']

AWS_QUERYSTRING_AUTH = False
AWS_ACCESS_KEY_ID = 'AKIAIAXGGQ5APIHMBKFA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_S3_HOST = 's3-ap-southeast-1.amazonaws.com'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_STORAGE_BUCKET_NAME = 'zappa-lambda-assets'
AWS_LOCATION = 'admin-staging'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'lambdazappa',
        'USER': 'root',
        'PASSWORD': 'qazqaz123',
        'HOST': 'lambda-zappa.csp92n8eqf6a.ap-southeast-1.rds.amazonaws.com',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"',
        }
    }
}
