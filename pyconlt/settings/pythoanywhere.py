from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'pyconlt',  # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'pyconlt',
        'PASSWORD': 'pythonyrajega',
        'HOST': 'marsaeigis-617.postgres.pythonanywhere-services.com',
        # Empty for localhost through domain sockets or
        #  '127.0.0.1' for localhost through TCP.
        'PORT': '10617',  # Set to empty string for default.
    }
}

SECRET_KEY = '8lu*6g0kdsjhiodshgfdsjkfgjkdsjgkhs2shmi1jcgihb*'

ALLOWED_HOSTS = ['127.0.0.1', 'marsaeigis.pythonanywhere.com', 'pycon.lt']
