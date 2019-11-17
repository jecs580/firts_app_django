"""
    Django settings for platzigram project.

    Generated by 'django-admin startproject' using Django 2.0.7.

    For more information on this file, see
    https://docs.djangoproject.com/en/2.0/topics/settings/

    For the full list of settings and their values, see
    https://docs.djangoproject.com/en/2.0/ref/settings/
"""
    # Este archivo define todas las configuraciones de nuestro proyecto
import os

    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    # Declara el lugar donde esta corriendo el proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    # Se utiliza para el hashin de las contraseñas
SECRET_KEY = 'jgh7aat7*wm%v%sn$@*txr*$lei9&9e%+12&^)xml2d)w#m7dm'

    # SECURITY WARNING: don't run with debug turned on in production!
    #Variable que marca que el proyecto esta en desarrollo, se recomienda ponerlo a false cuando se hace produccion
DEBUG = True

    # Que host estan permitidos interactuar con nuestro proyecto
ALLOWED_HOSTS = []


    # Application definition

    # Aplicaciones instaladas por defecto al crear el proyecto
INSTALLED_APPS = [
        # Django Apps
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        
        # Aplicaciones locales
        'posts',
        'users',
    ]

MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]
    # Define nuestro archivo principal de URL´s
ROOT_URLCONF = 'platzigram.urls'

TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]

WSGI_APPLICATION = 'platzigram.wsgi.application'


    # Database
    # https://docs.djangoproject.com/en/2.0/ref/settings/#databases
    #Configuracion de nuestra base de datos
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


    # Password validation
    # https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators
    # Validadores de Contraseñas, se puede crear nuestros propios validadores
AUTH_PASSWORD_VALIDATORS = [
        {
            # Los valores de tu contraseña no sean similires a nuestro usuario
            'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        },
        {
            # Validacion para minima longitud
            'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        },
        {
            # Valicacion contra un diccionario de contraseñas comunes
            'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        },
        {
            # Valicacion para que la contraseña no sea numerica
            'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
        },
    ]


    # Internationalization
    # https://docs.djangoproject.com/en/2.0/topics/i18n/
    # Lenguaje con el que se esta interactuando nuestra aplicacion, por defecto es íngles
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/2.0/howto/static-files/
    # Va a buscar el archivo estatico que se requiere
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # El media_root requiere que le demos la ruta donde esta alojado el proyecto seguido del directorio donde se almacenara los archivos. Para ayuda de los desarrolladores se usa el "os.path.join" esto permita que django traiga el valor de donde esta alojado el proyecto, sin impotar si lo movemos
MEDIA_URL = '/media/'
