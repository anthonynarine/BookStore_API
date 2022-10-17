from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def books_list(request):
    """function to GET All books"""
    
    return Response("ok")
    
    
        
