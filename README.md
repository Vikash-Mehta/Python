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
