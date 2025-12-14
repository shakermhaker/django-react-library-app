from rest_framework import serializers
from .models import Books, UserBooks, Users

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'

class UserBookSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only = True)

    class Meta:
        model = UserBooks
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    favorite_books = UserBookSerializer(source = 'userbooks_set', many=True, read_only=True)

    class Meta:
        model = Users
        fields = '__all__'