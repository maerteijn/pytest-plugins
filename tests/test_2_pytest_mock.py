import pytest_plugins.models
from pytest_plugins.models import User


def test_pytest_mock__patch(mocker):
    mocker.patch(
        "pytest_plugins.models.check_user_on_remote_server",
        side_effect=ConnectionError("Error"),
    )

    user = User()
    assert not user.exists_on_remote_server()


def test_pytest_mock__spy(mocker):
    spy = mocker.spy(pytest_plugins.models, "check_user_on_remote_server")

    user = User()
    user.exists_on_remote_server()

    assert spy.called
    assert spy.call_count == 1

    mocker.stop(spy)

    user.exists_on_remote_server()
    assert spy.call_count == 1
