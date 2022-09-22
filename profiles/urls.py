from django.urls import path
from .views import profile, index


urlpatterns = [
    path('', index, name='profiles_index'),
    path('<str:username>/', profile, name='profile'),
]
