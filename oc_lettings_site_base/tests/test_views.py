import pytest

from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed
from bs4 import BeautifulSoup


@pytest.mark.django_db
def test_profile_index_view():
    client = Client()
    path = reverse('index')

    response = client.get(path)

    soup = BeautifulSoup(response.content, features="html.parser")
    soup_content = soup.find_all("h1")

    assertion_check = 'Welcome to Holiday Homes'

    assert response.status_code == 200
    assertTemplateUsed(response, 'oc_lettings_site_base/index.html')
    assert assertion_check == soup_content[0].get_text()
