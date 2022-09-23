import pytest

from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_profile_index_view():
    client = Client()
    path = reverse('index')

    response = client.get(path)

    assert response.status_code == 200
    assertTemplateUsed(response, 'oc_lettings_site_base/index.html')
    assert 1 == 2
