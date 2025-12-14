from rest_framework import serializers
from ..models import Books, UserBooks, CustomUser

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'