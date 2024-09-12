import pytest


@pytest.mark.django_db
def test_pytest_repeat(user_factory, django_user_model):
    user_factory.create_batch(size=2)
    assert django_user_model.objects.count() == 2
