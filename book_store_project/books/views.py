from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import BookSerializer
from .models import Book



@api_view(["GET", "POST"])
def books_list(request):
    """function to GET All books and POST new book"""
    
    if request.method == "GET":
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
@api_view(["GET","PUT", "DELETE"])
def book_detail(request, pk):
    """"function to GET by ID, Update and Delete using id"""
    book = get_object_or_404(Book, pk=pk) #available GET and PUT request not need to repeat
    if request.method == "GET":   
        serializer = BookSerializer(book);
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = BookSerializer(book, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save() #this updates our object (book) in the database
        return Response(serializer.data)
    elif request.method == "DELETE":
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        

        
