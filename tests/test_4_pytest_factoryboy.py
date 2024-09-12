import os


def test_pytest_factory_boy(django_user_model, user, user_factory):
    assert isinstance(user, django_user_model)

    another_user = user_factory()
    assert isinstance(user, django_user_model)
