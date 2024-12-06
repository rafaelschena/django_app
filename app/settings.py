import os
from urllib.parse import urlparse

DATABASE_URL = os.environ.get("DATABASE_URL")
parsed_db_url = urlparse(DATABASE_URL)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': parsed_db_url.path[1:],
        'USER': parsed_db_url.username,
        'PASSWORD': parsed_db_url.password,
        'HOST': parsed_db_url.hostname,
        'PORT': parsed_db_url.port,
    }
}
