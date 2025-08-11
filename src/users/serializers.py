from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

user_model = get_user_model()

class UserApiSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True,
        max_length=150,
        validators=[UniqueValidator(
            queryset=user_model.objects.all()
        )
    ]
    )
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(
            queryset=user_model.objects.all()
        )
    ]
    )
    password = serializers.CharField(
        write_only=True,
        min_length=8,
        required=True
    )
    class Meta:
        model = user_model
        fields = '__all__'

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = user_model(**validated_data)
        user.set_password(password)  # хэшируем пароль
        user.save()
        return user