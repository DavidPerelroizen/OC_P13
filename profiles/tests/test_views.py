import pytest

from django.urls import reverse
from django.test import Client
from profiles.models import Profile
from pytest_django.asserts import assertTemplateUsed
from django.contrib.auth.models import User
from bs4 import BeautifulSoup


@pytest.mark.django_db
def test_profile_index_view():
    client = Client()
    path = reverse('profiles_index')

    response = client.get(path)

    assert response.status_code == 200
    assertTemplateUsed(response, 'profiles/index.html')


@pytest.mark.django_db
def test_profile_view():
    client = Client()
    user_for_test = User()
    user_for_test.username = 'test_user'
    profile_for_test = Profile()
    profile_for_test.user = user_for_test
    profile_for_test.favorite_city = 'paris'

    path = reverse('profile', kwargs={'username': 'test_user'})

    response = client.get(path)

    soup = BeautifulSoup(response.data, features="html.parser")
    soup_content = soup.find_all("h1")

    assertion_check = 'test_user'

    assert response.status_code == 200
    assert assertion_check == soup_content[0].get_text()
    assertTemplateUsed(response, "profiles/profile.html")


