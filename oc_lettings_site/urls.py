from django.contrib import admin
from django.urls import path, include


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path('', include('oc_lettings_site_base.urls', namespace='oc-lettings-site-base')),
    path('admin/', admin.site.urls),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('lettings/', include('lettings.urls', namespace='lettings')),
    path('sentry-debug/', trigger_error),
]
