DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                }
            }
ROOT_URLCONF = 'djangobb_forum.urls'
INSTALLED_APPS = ('django.contrib.auth',
                  'django.contrib.contenttypes',
                  'django.contrib.sessions',
                  'django.contrib.admin',
                  'djangobb_forum')
SECRET_KEY = 'secret'
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}