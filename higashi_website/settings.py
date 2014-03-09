import os
from selvbetjening.settings_base import *

DIRNAME = os.path.abspath(os.path.dirname(__file__))

# email
DEFAULT_FROM_EMAIL = 'noreply@anime-higashi.dk'
SERVER_EMAIL = 'noreply@anime-higashi.dk'

# various settings
ROOT_URLCONF = 'higashi_website.urls'

ADMINS = (
    # ('name', 'email')
)

# template directories
TEMPLATE_DIRS = [os.path.join(DIRNAME, 'templates')] + TEMPLATE_DIRS

# installed applications
INSTALLED_APPS.extend([
    'selvbetjening.viewbase.forms',
    'selvbetjening.viewbase.googleanalytics',
    'selvbetjening.viewbase.copyright',
    'selvbetjening.viewbase.branding',

    'selvbetjening.portal.quickregistration',
    'selvbetjening.portal.profile',
    'selvbetjening.portal.eventregistration',

    'selvbetjening.sadmin.base',
    'selvbetjening.sadmin.members',
    'selvbetjening.sadmin.events',
    'selvbetjening.sadmin.mailcenter',

    'higashi_website.apps.design'
])

POLICY['PORTAL.EVENTREGISTRATION.SKIP_CONFIRMATION_ON_EMPTY_OPTIONS'] = True

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'

# import localsettings, a per deployment configuration file
try:
    from settings_local import *
except ImportError:
    pass
