from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import TodoItem


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user object."""
    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'username']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def update(self, instance, validated_data):
        """Update user, handle password safely."""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user


class TodoItemSerializer(serializers.ModelSerializer):
    """Serializer for To-Do items."""
    class Meta:
        model = TodoItem
        fields = ['id', 'task_name', 'description', 'is_completed', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
