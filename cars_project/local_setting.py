
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!$$xx$yt41wazy4e945i^wii6_38$dgz)49)a0e4004i6x&31!'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}