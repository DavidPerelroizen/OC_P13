import pytest
from django.urls import reverse, resolve
from lettings.models import Address, Letting


@pytest.mark.django_db
def test_address_model_creation():
    address_for_test = Address()
    address_for_test.number = 53
    address_for_test.street = 'rue de la crête'
    address_for_test.city = 'Annecy'
    address_for_test.state = 'HS'
    address_for_test.zip_code = 74960
    address_for_test.country_iso_code = 'FRA'
    address_for_test.save()

    expected_value = '53 rue de la crête'

    assert str(address_for_test) == expected_value


@pytest.mark.django_db
def test_letting_model_creation():
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
