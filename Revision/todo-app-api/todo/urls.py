from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from . import views


router = DefaultRouter()
router.register('items', views.TodoItemViewSet)

app_name = 'todo'

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('me/', views.ManageUserView.as_view(), name='me'),
    path('', include(router.urls)),
]