from django.contrib.auth.models import User
from djoser import serializers
from djoser.conf import settings


class CustomUserSerializer(serializers.UserSerializer):
    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            settings.USER_ID_FIELD,
            settings.LOGIN_FIELD,
        ) + (
            'groups', 'is_staff', 
            'is_superuser', 'is_active',
            'first_name', 'last_name'
		)
        read_only_fields = (settings.LOGIN_FIELD,)
        

class CustomUserCreateSerializer(serializers.UserCreateSerializer):
    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            settings.LOGIN_FIELD,
            settings.USER_ID_FIELD,
            "password",
        ) + (
            'first_name', 'last_name'
		)
