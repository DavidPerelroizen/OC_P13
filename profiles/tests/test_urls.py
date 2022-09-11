import pytest
from django.urls import reverse, resolve
from profiles.models import Profile
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_profile_url():
    user_for_test = User(username='test_user')
    profile_for_test = Profile()
    profile_for_test.user = user_for_test
    profile_for_test.favorite_city = 'paris'

    path = reverse('profile', kwargs={'username': 'test_user'})

    assert path == '/profiles/test_user/'
    assert resolve(path).view_name == 'profile'


@pytest.mark.django_db
def test_profiles_index_url():

    path = reverse('profiles_index')

    assert path == '/profiles/'
    assert resolve(path).view_name == 'profiles_index'
