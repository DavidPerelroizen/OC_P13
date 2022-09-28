from django.urls import path
from .views import index


app_name = 'oc-lettings-site-base'
urlpatterns = [
    path('', index, name='index'),
]
