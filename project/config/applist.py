
# Application definition

DJANDO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LOCAL_APPS = []

THRID_PART_APPS = [
    'corsheaders',
    'rest_framework',
    'django_filters',
]

INSTALLED_APPS = DJANDO_APPS + LOCAL_APPS + THRID_PART_APPS
