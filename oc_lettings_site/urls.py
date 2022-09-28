from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('oc_lettings_site_base.urls')),
    path('admin/', admin.site.urls),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('lettings/', include('lettings.urls', namespace='lettings')),
]
