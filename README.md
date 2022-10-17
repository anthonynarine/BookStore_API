# BookStore_API



Linking our project to to mysqlclient

1. create a local_settings.py file in the project folder.

2. in settings.py scroll to databases. 

    cut the entire section out and past it into local.settings.py

    This new file is already marked in gitignore so whatever 
    is in that file will not be pushed. 

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",    ****make sure change from sqlite3 to mysql
        "NAME": "cars_database",
        "HOST": "localhost",
        "USER": "****",
        "PASSWORD": "****"

    }
}

3. at the bottom of our setting.py file 

try:
    from cars_project.local_settings import *
except ImportError:
    pass

4. cut out the security key from settings.py and past into local_settings.py. 

git commits will not have user info and secret keys. 

5. connecting the djanjo applictaion to mysql workbench
    1. +sql
    
    2. CREATE DATABASE <database_name> *must be name of the databse created
       in the settings files. (now found in local_settings.py)

    3. lightning bolt 

    4. refresh
    
    5. database shold be seen under schemas. 

    6. python manage.py migrate (defined table shold be created)





Creating App Serializers  

1. in app folder create file serializer.py

    import. 
    from rest_framework import serializers

2. import app. 
    from .models import Car

3. create class.
 ~the class is always named after the model followed by Serializer 

    class CarSerializer(serializers.ModelSerializer): 
        class Meta:
            model = Book
            fields = ["id", "title", "author", "genre", "price", "year_published", "quantity"]


Next ADMIN SETTING.  

Admin center setup. 
    1. python manage.py createsuperuser

    2. fill out prompts.
        user name
        password (you will not get to see the pw)
        email 

    check mysql workbench auth_user execute query
    and the admin inflow will populate

    3. python manage.py runserver
       follow link
       admin
       log on using username and pw
       users and groups shold be available for edits.

    4. registering the model with our Django admin.py
       app folder -> admin.py -> import appmodel...ex below 

       from .models import Car
    
    5. in admin.py
       admin.site.register(Car) #the model is passed in 
