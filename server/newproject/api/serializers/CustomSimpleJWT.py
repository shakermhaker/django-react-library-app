from ..models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['username'] = self.user.username
        data['email'] = self.user.email
        data['role'] = self.user.role
        if self.user.profile_picture:
            data['profile_picture'] = self.user.profile_picture.url
        else:
            data['profile_picture'] = None
        return data
        