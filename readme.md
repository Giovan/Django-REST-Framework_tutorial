# Django REST Framework Tutorial
This is the final project of the django REST Framework as you can find in the oficial [webpage](https://www.django-rest-framework.org/tutorial/).


Find the original repo for project structure and names in the [oficial repo](https://github.com/encode/django-rest-framework).

## Pre-requisites
It make use of Pipenv a wonderful tool that aims to bring the best of all packaging worlds to the Python world. [Extracted from the oficial documentation](https://pipenv.readthedocs.io/en/latest/).

Installation with brew is simple as:
```sh
brew install pipenv
```
("assuming that you are using mac os")

Give a start to the [Pipenv repo](https://github.com/pypa/pipenv/) and also you can say [thanks](https://saythanks.io/to/kennethreitz) to kennethreitz for the awesome job in this wonderful tool.

## Installation
Run:
```sh
pipenv install
```
Automatically retrieves the packages saved previously in the Pipfile.lock

## Running
Use:
```sh
pipenv shell
```
To enter in the pipenv interactive mode


Then run:
```sh
python3 manage.py migrate
```

It will create the database in sqlite format and also run migrations for tables creation; sqlite is used for tutorial version and easy access to functionalities, in your product use a stable and production ready database (Poastgres, MySQL, Mongo, Oracle)


*Recommended superuser(admin) creation, it will helps to manage data in the UI
```sh
python3 manage.py createsuperuser
```


Then we can run the project as simple as:
```sh
python3 manage.py runserver
```

You get this response in console:
<p><a href="http://localhost:8000"><img src="https://namoxbase.ams3.cdn.digitaloceanspaces.com/Screen%20Shot%202018-12-08%20at%206.47.04%20PM.png" alt="drf-console-run"></a></p>

Project in action
<p align="center"><a href="http://localhost:8000"><img src="https://namoxbase.ams3.cdn.digitaloceanspaces.com/Screen%20Shot%202018-12-08%20at%207.01.00%20PM.png" alt="drf-snippets"></a></p>

Test in console -

GET:
<p><a href="http://localhost:8000"><img src="https://namoxbase.ams3.cdn.digitaloceanspaces.com/Screen%20Shot%202018-12-08%20at%207.02.17%20PM.png" alt="drf-get-method-runnig"></a></p>

POST:
<p><a href="http://localhost:8000"><img src="https://namoxbase.ams3.cdn.digitaloceanspaces.com/Screen%20Shot%202018-12-08%20at%207.02.17%20PM.png" alt="drf-snippets-post-method-ok"></a></p>


## Base
Directory Tree
```sh
tree
```

Doesn't works?
```sh
brew install tree
```

Project structure:
```sh
.
├── Pipfile
├── Pipfile.lock
├── apiconfig
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
├── readme.md
└── snippets
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations
    │   ├── 0001_initial.py
    │   └── __init__.py
    ├── models.py
    ├── permissions.py
    ├── serializers.py
    ├── serializers.py.bak
    ├── tests.py
    ├── urls.py
    ├── urls.py.bak
    ├── views.mixins.py.bak
    ├── views.py
    └── views.py.bak
```

## Changes

