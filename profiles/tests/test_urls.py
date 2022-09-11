import pytest
from django.urls import reverse, resolve
from profiles.models import Profile
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_profile_url():
    user_for_test = User(username='test_user')
    Profile.objects.create(user_for_test, 'paris')

    path = reverse('profile', kwargs={'username': 'test_user'})

    assert path == 'test_user/'
    assert resolve(path).view_name == 'profile'


@pytest.mark.django_db
def test_profiles_index_url():

    path = reverse('profiles_index')

    assert path == '/'
    assert resolve(path).view_name == 'profiles_index'
