from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework import filters

from .models import TodoItem
from .serializers import TodoItemSerializer, UserSerializer

# Create your views here.
class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user profile."""
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self):
        """Retrieve and return authenticated user."""
        return self.request.user


class TodoItemViewSet(viewsets.ModelViewSet):
    serializer_class = TodoItemSerializer
    queryset = TodoItem.objects.all()

    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('task_name',)
    ordering_fields = ('created_at', 'updated_at', 'is_complicated')
    ordering = ('-updated_at')

    def get_queryset(self):
        """Return objects for the current authenticated user only."""
        return self.queryset.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        """Create a new todo and assign it to the user."""
        serializer.save(user=self.request.user)
