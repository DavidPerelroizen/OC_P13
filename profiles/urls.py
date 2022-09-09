from django.urls import path
from .views import profile, index


urlpatterns = [
    path('', index, name='index'),
    path('<str:username>/', profile, name='profile'),
]
