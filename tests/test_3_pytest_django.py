import pytest
from django.urls import reverse
from pytest_django.asserts import assertQuerySetEqual, assertTemplateUsed

from pytest_plugins.models import User


@pytest.mark.django_db
def test_pytest_django__django_db(django_user_model):
    user = django_user_model()
    assert user.pk is None

    user.save()
    assert user.pk is not None


@pytest.mark.django_db
def test_pytest_django__assert_num_queries(
    django_user_model, django_assert_num_queries
):
    with django_assert_num_queries(1):
        user = django_user_model()
        user.save()


@pytest.mark.django_db
def test_pytest_django__fixtures(client, admin_user):
    response = client.get(reverse("admin:index"))
    assert response.status_code == 302

    client.force_login(admin_user)
    response = client.get(reverse("admin:index"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_pytest_django__assert_queryset_equal(django_user_model, admin_user):
    assert django_user_model.objects.exists()
    assertQuerySetEqual(django_user_model.objects.all(), User.objects.all())


@pytest.mark.django_db
def test_pytest_django__assert_template_used(admin_client):
    response = admin_client.get(reverse("admin:index"))
    assertTemplateUsed(response, "admin/index.html")
