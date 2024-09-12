from django.urls import reverse
from playwright.sync_api import expect


def test_pytest_playwright__admin_login(
    live_server, django_db_serialized_rollback, page, admin_user
):
    response = page.goto(live_server.url + reverse("admin:login"))
    assert response.status == 200

    page.fill("#id_username", admin_user.username)
    page.fill("#id_password", "password")
    page.click('input[type="submit"]')

    assert page.url == live_server.url + reverse("admin:index")
