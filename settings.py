import os
import sys
sys.path.insert(
    0,
    os.path.join(
        os.path.dirname(__file__),
        "lib"
    )
)

# Initialize App Engine and import the default settings (DB backend, etc.).
# If you want to use a different backend you have to remove all occurences
# of "djangoappengine" from this file.
from djangoappengine.settings_base import *

# Activate django-dbindexer for the default database
DATABASES['native'] = DATABASES['default']
DATABASES['default'] = {'ENGINE': 'dbindexer', 'TARGET': 'native'}
AUTOLOAD_SITECONF = 'indexes'

SECRET_KEY = '=r-$b*8hglm+858&9t043hlm6-&6-3d3vfc4((7yd0dbrakhvi'

SITE_ID = '76'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.comments',
    'django.contrib.sites',
    'debug_toolbar',
    'djangotoolbox',
    'autoload',
    'dbindexer',

    'socialregistration',
    'socialregistration.contrib.facebook',
    'blog',

    # djangoappengine should come last, so it can override a few manage.py commands
    'djangoappengine',
)

MIDDLEWARE_CLASSES = (
    # This loads the index definitions, so it has to come first
    'autoload.middleware.AutoloadMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
)

GAE_SETTINGS_MODULES = (
    'gae_db_field_settings',
)

AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',
        'socialregistration.contrib.facebook.auth.FacebookAuth',        
)

FACEBOOK_APP_ID = '283539771683468'
FACEBOOK_SECRET_KEY = '9b1c4bdfafda6c90db458411fc8d4412'
FACEBOOK_REQUEST_PERMISSIONS = ''

SOCIALREGISTRATION_GENERATE_USERNAME = True
SOCIALREGISTRATION_GENERATE_USERNAME_FUNCTION = 'utils.socregUserCreate'

AUTH_PROFILE_MODULE = "blog.UserProfile"

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False
}

# This test runner captures stdout and associates tracebacks with their
# corresponding output. Helps a lot with print-debugging.
TEST_RUNNER = 'djangotoolbox.test.CapturingTestSuiteRunner'

ADMIN_MEDIA_PREFIX = '/media/admin/'
TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), 'blog/templates'),)

ROOT_URLCONF = 'blog.urls'
