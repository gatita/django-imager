from settings import *

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['ec2-52-24-124-230.us-west-2.compute.amazonaws.com',
                 'localhost']
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Email Settings
EMAIL_BACKEND = os.environ.get('IMAGER_EMAIL_BACKEND')
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get('IMAGER_EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('IMAGER_EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = os.environ.get('IMAGER_EMAIL_HOST_USER')
