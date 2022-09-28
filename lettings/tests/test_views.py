import pytest
from django.urls import reverse
from django.test import Client
from lettings.models import Letting, Address
from pytest_django.asserts import assertTemplateUsed
from bs4 import BeautifulSoup


@pytest.mark.django_db
def test_letting_view():
    address_for_test = Address()
    address_for_test.number = 53
    address_for_test.street = 'rue de la crête'
    address_for_test.city = 'Annecy'
    address_for_test.state = 'HS'
    address_for_test.zip_code = 74960
    address_for_test.country_iso_code = 'FRA'
    address_for_test.save()

    letting_for_test = Letting()
    letting_for_test.title = 'Letting for test'
    letting_for_test.address = address_for_test
    letting_for_test.save()

    expected_value = 'Letting for test'

    assert str(letting_for_test) == expected_value

    client = Client()
    path = reverse('lettings:letting', kwargs={'letting_id': letting_for_test.id})

    response = client.get(path)

    soup = BeautifulSoup(response.content, features="html.parser")
    soup_content = soup.find_all("h1")

    assertion_check = letting_for_test.title

    assert response.status_code == 200
    assert assertion_check == soup_content[0].get_text()
    assertTemplateUsed(response, "lettings/letting.html")


@pytest.mark.django_db
def test_lettings_index_view():
    client = Client()
    path = reverse('lettings:index')

    response = client.get(path)

    soup = BeautifulSoup(response.content, features="html.parser")
    soup_content = soup.find_all("h1")

    assertion_check = 'Lettings'

    assert response.status_code == 200
    assertTemplateUsed(response, 'lettings/index.html')
    assert assertion_check == soup_content[0].get_text()
