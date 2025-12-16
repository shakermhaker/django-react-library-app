from django.urls import path, include
from .views import getBooks, createBook, bookDetail
from .views.user_views import UserView
from rest_framework_simplejwt import views as jwt_views
from .views.authtest_views import HelloView
from .views.CustomSimpleJWTview import CustomTokenObtainpairView

urlpatterns = [
    path("books/", getBooks, name='getBooks'),
    path("books/create/", createBook, name='createBook'),
    path("books/<int:pk>", bookDetail, name='bookDetail'),
    path('token/', CustomTokenObtainpairView.as_view(), name ='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name ='token_refresh'),
    path('hello/', HelloView.as_view(), name ='hello'),
    path("user/register/", UserView.as_view(), name='register'),
    
] 