import re
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
            
@api_view(["GET"])
def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book);
        return Response(serializer.data)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND);
        
           
           

        
