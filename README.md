# Test-Driven Development (TDD) implementation in Python Django

## Installation steps

- Open a newly created project folder in vscode.
- Open terminal 
- create a virtual environment and activate it

```sh
py -m venv tdd03
```

- Select python interpretor 
> (python 3.8.6 (tdd03)

- Close and open the terminal to see venv is auto activated (tdd03)
- Now install django
```sh 
pip install django 
```

- Create a django project

` django-admin startproject tdd`

- create a test_settings.py inside the project directory (tdd) where settings.py resides

> test_settings.py

```sh
# using SQLITE database for testing
from .settings import *
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}
EMAIL_BACKEND = 'django.core.mail.backends.locmen.EmailBackend'
```

- install the latest version of pytest and required plugins:
```sh
$ pip install pytest
$ pip install pytest-django
$ pip install ipdb
$ pip install pytest-cov
```

- Now close the terminal and open a new terminal to get the effect of the newly installed modules
- Create a new file tdd/pytest.ini where we write


> pytest.ini file

```sh
[pytest]
DJANGO_SETTINGS_MODULE = tdd.test_settings
addopts = --nomigrations --cov=.  --cov-config=.coveragerc --cov-report=html
```
> Now the project directory structure will be like so:

```sh
pytest_cache
vscode
tdd
    - tdd
        - _pycache_
        - __init__.py
        - asgi.py
        - settings.py
        - test_settings.py
        - urls.py
        - wsgi.py
    manage.py
    pytest.py
tdd03
project-structure-01.jpg
README.md
```

## - Time to run the test

```sh
py.test
```
- The following output will be displayed:

```sh
(tdd03) PS C:\FDrive\A1PythonProjects\TDD\tdd03_pytest_django> py.test
================================================ test session starts ================================================ 
platform win32 -- Python 3.8.6, pytest-6.1.2, py-1.9.0, pluggy-0.13.1
rootdir: C:\FDrive\A1PythonProjects\TDD\tdd03_pytest_django
plugins: cov-2.10.1, django-4.1.0
collected 0 items

=============================================== no tests ran in 0.14s =============================================== 
(tdd03) PS C:\FDrive\A1PythonProjects\TDD\tdd03_pytest_django>
```

#### Now create a configuration file for coverage report

> .coveragerc file

```sh
[run]
omit =
    tdd/*,
    *apps.py,
    *migrations/*,
    *settings*,
    *tests/*,
    *urls.py,
    *wsgi.py,
    manage.py
```
## Testing of components of app

#### First create an app

- Go inside the root tdd folder and create app

```sh
django-admin startapp tddapp
```

> Now the folder structure will be:

```sh
pytest_cache
vscode
tdd
    - tdd
        - _pycache_
        - __init__.py
        - asgi.py
        - settings.py
        - test_settings.py
        - urls.py
        - wsgi.py
    tddapp
    - coveragerc
    - manage.py
    - pytest.py
tdd03
project-structure-01.jpg
README.md
```

- We will remove the tests.py from the app files and make new folder tests and __init__.py file to initialize it. Let’s create new test_models.py inside the tests folder.

```sh
delete tddapp/test.py
mkdir tddapp/tests
create tddapp/tests/__init__.py
create tddapp/tests/test_models.py
```

- It’s better to have tests folder for each Django app and for each code file to have a test file as an example: “models.py” i.e. “test_models.py”

- We need to install a mixer as some models can have many mandatory fields and it will be slow to create values for all those fields. A mixer is a tool that helps us to create test fixtures.

```sh
pip install mixer
```

- In test_models.py, we will create a new class names TestPost.

> test_models.py file

```sh
import pytest

from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


class TestPost:
    def test_model(self):
        obj = mixer.blend('tddapp.Post')
        assert obj.pk == 1, 'Should create a Post instance'
```

- Make sure your app is stated in INSTALLED_APPS in settings.py

- Add a new model in models.py file
> models.py
```sh
class Post(models.Model):
    description= models.TextField()
```

## The final project structure will look so:

```sh
pytest_cache
vscode
tdd
    pytest_cache
    htmlcov
    - tdd
        - _pycache_
        - __init__.py
        - asgi.py
        - settings.py
        - test_settings.py
        - urls.py
        - wsgi.py
    - tddapp
        __pycache__
        migrations
        tests
        - __init__.py
        - admin.py
        - apps.py
        - models.py
        - views.py
    - coverage    
    - coveragerc
    - manage.py
    - pytest.py
tdd03
project-structure-01.jpg
README.md
```

- Now, run the test by using the py.test and the test should pass.

>  Let’s have a look at our coverage report. Every time it runs a test, it generates an HTML coverage folder called htmlcov. This consists of an index.html file that can be viewed.

- Add extension in vscode :

> HTML Preview - Thomas Haakon Townsend

- Now the right click on the index.html file and select preview

