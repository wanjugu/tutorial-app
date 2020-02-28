# tutorial-app
This is website application built with Django python framework. 
The app was writen as part of django learning process following https://pythonprogramming.net/django-web-development-python-tutorial/

# About the App
This is a sample tutorial app develop with django framework.
We have used the following
- marializecss.com for styling
- Sqlite database

# How to run the Project
1. Git Clone the app
2. Use command tool to run the application server. 
On windows give command the following command >> python manage.py runserver 
3. Access the application via the link 127.0.0.1:8000

# creating the super-user
1. On windows cmd run >> python manage.py shell  
2. Run the following commands on the shell to create new user
- from django.contrib.auth.models import User
- user=User.objects.create_user('foo', password='bar')
- user.is_superuser=True
- user.is_staff=True
- user.save()

# Login in as admin
1. Access teh  Admin via link 127.0.0.1:8000/admin
2. Login using previously created credentials
