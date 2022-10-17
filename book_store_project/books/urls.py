from django.urls import path
from . import views

urlpatterns = [
    path("", views.books_list),
    path("<int:pk>/", views.book_detail),   # <> allows ojbects to be passed 
]


