from django.urls import path
from .views import getBooks, createBook, bookDetail


urlpatterns = [
    path("books/", getBooks, name='getBooks'),
    path("books/create/", createBook, name='createBook'),
    path("books/<int:pk>", bookDetail, name='bookDetail')
] 