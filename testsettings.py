DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}
ROOT_URLCONF = 'djangobb_forum.tests.urls'
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pagination',
    'djangobb_forum')
MIDDLEWARE_CLASSES = (
    # Django Defaults
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    # Required by DjangoBB
    'pagination.middleware.PaginationMiddleware')
TEMPLATE_CONTEXT_PROCESSORS = (
    # Django Defaults
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",

    # Required by DjangoBB
    "django.core.context_processors.request",
    "djangobb_forum.context_processors.forum_settings")
SECRET_KEY = 'secret'
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}
STATIC_URL = '/static/'
DEBUG = True

