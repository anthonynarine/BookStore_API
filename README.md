# BookStore_API



Linking our project to to mysqlclient

1. create a local_settings.py file in the project folder.

2. in settings.py scroll to databases. 

    cut the entire section out and past it into local.settings.py

    This new file is already marked in gitignore so whatever 
    is in that file will not be pushed. 


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
    ~ helps convert JSON into pyhton objects and python objects into JSON

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




CREATING VIEWS FUNCTION
    1. in view.py 
        Create GET all function 

 ~ imports needed       from rest_framework.decorators import api_view
                        from rest_framework.response import Response
                        from .serializer import BookSerializer
                        from .models import Book

        @api_view(["GET"])
        def books_list(request):
            """function to get all objects"""
            
            books = Book.object.all() 
        ~ we now need to use the serializer to convert the python data to json ~   

        ~ conventional use of seiralizer ~
            serializer = BookSerializer(books, many=True)

            ~ books in will take the python data 
            ~ and convert it to Json data
            ~ many=True this tells the serializer that it will
            ~ potentially be multiple books that needs to be serialized

            return Response(serializer.data) 

            ~ all the books data will be stored on a variable called data 
            on BookSerializer() so we send our response as serializer.data ~




    2. Create urls.py file (in app folder)

 ~ imports needed    from django.urls import path
                     from . import views

            urlpatterns = [                               ~standard syntax
                path("books/", views.books_list)
            ]

    3. Update project settings URL

   ~import needed    from django.urls import path, include

        urlpatterns = [
            path("admin/", admin.site.urls),
            path("api/books/", include("books.urls")),
        ]
 
        ** we will need to remove book in our app URLs file to
        ** to avoid http://127.0.0.1:8000/api/books/books/    request
        ** remoing book/ from our app urls file will bring our search to
        ** http://127.0.0.1:8000/api/books/






Next ADMIN SETTING  ~ Will help to seed our data ~

Admin center setup. 
    1. python manage.py createsuperuser

    2. fill out prompts.
        user name admin
        password (you will not get to see the pw) ~root
        email 

    check mysql workbench auth_user execute query
    and the admin inflow will populate

    3. python manage.py runserver
       follow link
       add /admin to link
       log on using username and pw
       users and groups shold be available for edits.

    
    
    REGISTERING our Book model
    1. app folder -> admin.py -> import appmodel...ex below 

       from .models import Book
    
    2. in admin.py
       admin.site.register(Book) #the model is passed in 

    This allows us to view and seed data through our django admin page. 
    ~ refresh server and we will see books on our page!


            ~ NOTE ~
        any price attribute will default as a str in django
        it should be converted to a int
To Convert:
            1. got to project settings.py
            2. create anywere in this file (as long as it's not in somethign else :)
                
                REST_FRAMEWORK = {
                    "COERCE_DECIMAL_TO_STRING": False
                }




        ~ CREATING POST FUNCTIONALITY ~

Currently our books_list only takes "GET" requests. Lets add "POST" request to the list. 
This is able to happen becuase neiter our GET all or POST new object request will require pk (id)

We will be doing this through HTTP request and not through Django admin this will 
allow anyone to create new Book objects and not just the developer

@api_view(["GET"])
def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book);
        return Response(serializer.data)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND);

    ~ FUNCTIONALITY FOR POST BEWLOW

    elif request.method == "POST":
        serializer = BookSerializer(data=request.data)
 """ here we'll be accessing the request (function parameter) then any data on that incoming request. 

        serializer.is_valid(raise_exception=True) 
        serializer.save()
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        The serializer has built in capability to raise exceptions so we don't need 
        seperate if else statements. 
            
     



    ~ Get BY ID EendPoint functionality ~

@api_view(["GET"])  
def book_detail(request, pk):             
    try:
        book = Book.objects.get(pk-pk)
        serializer = BookSerializer (book)
        return Response(serializer.data)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND);

 ~ function logic
     we pass the pk in -> django automatically grabs the url  path we set up  
     pass it to the appropiate parameter (pk)
     we then query the car table to get the specific car
     it there is an exception it means there isn't a car in the database with 
     that pk

Refractoring the function above:
~import
    from django.shortcuts import get_list_or_404, get_object_or_404

@api_view(["GET"])
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    serializer = BookSerializer(book);
    return Response(serializer.data)

with the functionality that get_list_or_404, get_object_or_404 provides we 
no longet need the try, except block. We just pass the class name (Book)
and the idintifer we want back (pk)



        ~ CREATING UPDATE FUNCTIONALITY ~+
    ~ since update will require only a pk from the back end we can add the functionality to our 
      the book_detail() function. 

     1. we need to the ojbect pk from the database.
         book = get_object_or_404(Book, pk=pk) This gets the object or send a 404 error

     2. we have to serialze the object  
        1st by pasing in the object (book)

        2nd we pass in the data and set it = to request.data
        this take a look at the imcoming data compare it to the object data
        and updates it in the database. 

        serializer = BookSerializer(book, data=request.data);

    3. serializer.is_valid(raise_exception=True)
    4. serializer.save()   #this updates our object (book) in the database
    5  return Response(serializer.data)

~function complete with query for PUT and upade functionality

    @api_view(["GET","PUT"])
    def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk) #available GET and PUT request not need to repeat
    if request.method == "GET":   
        serializer = BookSerializer(book);
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = BookSerializer(book, data=request.data)
        serializer.save() #this updates our object (book) in the database
        return Response(serializer.data)

           

