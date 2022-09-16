import pytest
from profiles.models import Profile
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_model_profile():
    user_for_test = User()
    user_for_test.username = 'test_user'
    user_for_test.save()
    profile_for_test = Profile()
    profile_for_test.user = user_for_test
    profile_for_test.favorite_city = 'dijon'
    profile_for_test.save()

    expected_value = 'test_user likes dijon'

    assert str(profile_for_test)+' likes '+profile_for_test.favorite_city == expected_value
