from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

# FIXME 
CSRF_TRUSTED_ORIGINS = [
    'http://<YOUR-DOMAIN.COM>',
    'https://<YOUR-DOMAIN.COM>',
    'https://<YOUR.IP.ADDRESS>',
    'http://<YOUR.IP.ADDRESS>',
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
