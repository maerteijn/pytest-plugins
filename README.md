# My most used pytest plugins for Django development

A demonstration repository for the following pytest plugins:

- [pytest-env](https://github.com/pytest-dev/pytest-env)
- [pytest-mock](https://github.com/pytest-dev/pytest-mock/)
- [pytest-django](https://github.com/pytest-dev/pytest-django)
- [pytest-factoryboy](https://github.com/pytest-dev/pytest-factoryboy)
- [pytest-playwright](https://github.com/microsoft/playwright-pytest)
- [pytest-repeat](https://github.com/pytest-dev/pytest-repeat)

## Development setup

### Requirements

- At least python 3.12 with a virtualenv

### Install the django project
```bash
pyenv virtualenv pytest-plugins  # or your alternative to create a venv
pyenv activate pytest-plugins
make bootstrap  # install correct / supported pip and pip-tools version
make install
```

### Linting

`ruff` and `mypy` linting
```bash
make lint
```

### Formatting

`ruff`
```bash
make format
```

### Test

`pytest` is used to run the tests
```bash
make test
```

### Playwright E2E test
```bash
make test-e2e
```










