from django.conf import settings
from django.contrib.auth import models
from django.utils.translation import gettext_lazy as _

__all__ = ("User",)


def check_user_on_remote_server(user):
    # Here you should imagine a very complicated call here to a remote
    # user database to verify if this user exists
    return True


class User(models.AbstractUser):
    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def exists_on_remote_server(self):
        try:
            return check_user_on_remote_server(user=self)
        except ConnectionError:
            return False
