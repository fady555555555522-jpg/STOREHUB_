from pathlib import Path
import os
from django.contrib.messages import constants as message_constants

BASE_DIR = Path(__file__).resolve().parent.parent

APPEND_SLASH = True

# =========================
# SECURITY & DEBUG SETTINGS
# =========================
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", 'django-insecure-6y!svxc#ynh52$al4&y^ql$u0kyob#s08+033t%oj)7ufui8w)')
DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    'local.test',
    'storehub-production.up.railway.app'
]

CSRF_TRUSTED_ORIGINS = [
    'https://storehub-production.up.railway.app'
]

SECURE_SSL_REDIRECT = not DEBUG
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True

# ====================
# APPLICATION SETTINGS
# ====================
INSTALLED_APPS = [
    'channels',
    'jazzmin',
    'pages.apps.PagesConfig',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    'rest_framework',
    'rest_framework.authtoken',
]

SITE_ID = 1

# ==========
# MIDDLEWARE
# ==========
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

# =========
# TEMPLATES
# =========
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'pages/templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'builtins': ['django.templatetags.static'],
        },
    },
]

# ===============
# URL / ASGI / WSGI
# ===============
ROOT_URLCONF = 'project.urls'
WSGI_APPLICATION = 'project.wsgi.application'
ASGI_APPLICATION = 'project.asgi.application'

# =========
# DATABASES
# =========
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ======================
# PASSWORD VALIDATION
# ======================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ==================
# INTERNATIONALIZATION
# ==================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ============
# STATIC/MEDIA
# ============
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'project/static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# ===============
# AUTHENTICATION
# ===============
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

LOGIN_REDIRECT_URL = 'custom_redirect'
LOGOUT_REDIRECT_URL = 'login'
LOGIN_URL = 'login'
ACCOUNT_SIGNUP_REDIRECT_URL = '/select-role/'
SOCIALACCOUNT_SIGNUP_REDIRECT_URL = '/select-role/'
DEFAULT_REDIRECT_URL = 'custom_redirect'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_EMAIL_SUBJECT_PREFIX = '[StoreHub] '
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True
ACCOUNT_PASSWORD_MIN_LENGTH = 8
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_MIN_LENGTH = 4
ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = True

SOCIALACCOUNT_AUTO_SIGNUP = False

# ================
# GOOGLE OAUTH
# ================
REDIRECT_URI = 'https://storehub-production.up.railway.app/accounts/google/login/callback/'
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {'access_type': 'online'},
        'APP': {
            'client_id': '1082526950831-pp90ki66g5dmodn72rlkfeapdgfpjgtb.apps.googleusercontent.com',
            'secret': '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',
            'key': ''
        },
        'OAUTH_PKCE_ENABLED': True,
    }
}

# ====================
# DJANGO MESSAGES TAGS
# ====================
MESSAGE_TAGS = {
    message_constants.DEBUG: 'alert-info',
    message_constants.INFO: 'alert-info',
    message_constants.SUCCESS: 'alert-success',
    message_constants.WARNING: 'alert-warning',
    message_constants.ERROR: 'alert-danger',
}

# ===========
# JAZZMIN ADMIN
# ===========
JAZZMIN_SETTINGS = {
    'copyright': 'FADY ASHRAF',
    'site_title': "STOREHUB",
    'site_header': "STOREHUB",
    'site_brand': "STOREHUB",
    'site_icon': 'images/LOGO1.png',
    'site_logo': 'images/LOGO1.png',
    'login_logo': 'images/LOGO1.png',
    'login_logo_dark': 'images/LOGO1.png',
    'login_logo_light': 'images/LOGO1.png',
    'login_logo_small': 'images/LOGO1.png',
    'login_logo_small_dark': 'images/LOGO1.png',
    'login_logo_small_light': 'images/LOGO1.png',
    'login_logo_small_alt': 'images/LOGO1.png',
    "welcome_sign": "Welcome to STOREHUB Admin Panel",
    "show_sidebar": True,
    "navigation_expanded": True,
    "theme": "dark",
    "costmize_botton": True,
    "show_ui_builder": True,
    "changeform_format": "horizontal_tabs",
    "related_modal_active": True,
}

JAZZMIN_UI_TWEAKS = {
    "theme": "darkly",
    "dark_mode_theme": "darkly",
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-dark",
    "accent": "accent-primary",
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": False,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
}

# ===================
# EMAIL CONFIGURATION
# ===================
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', 'fady555555555522@gmail.com')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', 'lpbu adms usni fjqv')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

ACCOUNT_ADAPTER = 'pages.adapters.CustomAccountAdapter'
ACCOUNT_PASSWORD_RESET_TOKEN_GENERATOR = 'django.contrib.auth.tokens.PasswordResetTokenGenerator'
ACCOUNT_PASSWORD_RESET_TOKEN_EXPIRY = 24

# ============
# STRIPE KEYS
# ============
STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY", "sk_test_51RauUlGfwzChTOC8PXXS8sRr3jVsdP7Zq03T9fLCM3Y3gS2G286RudvtAvCjdU2OjMw59W4AQJeRD9mn7T3gnunr00m5d9MHP8")
STRIPE_PUBLISHABLE_KEY = os.environ.get("STRIPE_PUBLISHABLE_KEY", "pk_test_51RauUlGfwzChTOC83HiX3g5umkw5xUvSIsRPC9mx1J4pmNDmLRY7FfPC1Uim33AH1UAmHec9c4qb2PP3QcGReVPK00DOxuCePe")

# ====================
# REST FRAMEWORK
# ====================
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

# ====================
# CHANNEL LAYERS
# ====================
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
    },
}
