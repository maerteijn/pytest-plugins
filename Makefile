.PHONY: bootstrap versions update install migrate lint test test-e2e format

default: install migrate

bootstrap:
	pip install "pip>=24.2,<25" "pip-tools>=7.4.1,<8"

versions:
	pip-compile --no-strip-extras --upgrade -o requirements.txt pyproject.toml
	pip-compile --no-strip-extras --extra dev --upgrade -o requirements-dev.txt pyproject.toml

install:
	pip install -r requirements-dev.txt -e .

migrate:
	manage.py migrate

lint:
	ruff check src/**
	mypy .

test:
	pytest

test-e2e:
	 playwright install firefox
	 DJANGO_ALLOW_ASYNC_UNSAFE=1 pytest --headed tests/test_5_pytest_playwright.py --browser firefox

format:
	ruff check --select I --fix src/** tests/**
	ruff format src/** tests/**

superuser:
	DJANGO_SUPERUSER_USERNAME=admin DJANGO_SUPERUSER_EMAIL=admin@example.com DJANGO_SUPERUSER_PASSWORD=admin manage.py createsuperuser --noinput
