import os


def test_pytest_env():
    assert "CURRENT_USER" in os.environ
    assert os.environ["USER"] == os.environ["CURRENT_USER"]
