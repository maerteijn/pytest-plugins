import factory
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

User = get_user_model()
factory.Faker._DEFAULT_LOCALE = "nl_NL"


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Faker("first_name")
    email = factory.Faker("email")

    class Meta:
        model = User
        django_get_or_create = ("username",)
        skip_postgeneration_save = True
