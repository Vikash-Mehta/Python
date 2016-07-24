Python Django Tutorial



Install python
Install Django
django-admin startproject myproject

Django create a “myapp” folder
    python manage.py startapp myapp

To initiate the database:
    python manage.py migrate

To create superuser
    python manage.py createsuperuser

To run the server
    python manage.py runserver

Template Directory(settings.py)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_DIR + '/myapp/views/'],
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







#Django create a “myapp” folder
    python manage.py startapp authentication

#Migrating the app
        python manage.py makemigrations
        python manage.py migrate


#Making yourself a superuser
    python manage.py createsuperuser


#Checkpoint
#To make sure everything is properly configured, let's take a quick break and open Django's shell:
    python manage.py shell
    from authentication.models import Account
    a = Account.objects.latest('created_at')

#To get serialized detail
    >>> from authentication.models import Account
    >>> from authentication.serializers import AccountSerializer
    >>> account = Account.objects.latest('created_at')
    >>> serialized_account = AccountSerializer(account)
    >>> serialized_account.data.get('email')
    >>> serialized_account.data.get('username')