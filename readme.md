# Django REST Framework Tutorial
This is the final project of the django REST Framework as you can find in the oficial [webpage](https://www.django-rest-framework.org/tutorial/).


Find the original repo for project structure and names in the [oficial repo](https://github.com/encode/django-rest-framework).

## Pre-requisites
It make use of Pipenv a wonderful tool that aims to bring the best of all packaging worlds to the Python world. [Extracted from the oficial documentation](https://pipenv.readthedocs.io/en/latest/).

Installation is simple as:
```sh
brew install pipenv
```
("assuming that you are using mac os")

Give a start to the [Pipenv repo](https://github.com/pypa/pipenv/) and also you can say [thanks](https://saythanks.io/to/kennethreitz) to kennethreitz for the awesome job in this wonderful tool.

## Installation
Just run:
```sh
pipenv install
```
Automatically retrieves the packages saved previously in the Pipfile.lock

## Running
Use:
```sh
pipenv shell
```
To enter in the pipenv interactive mode, then run(It will create the database in sqlite format and also run migrations for tables creation
) sqlite is used for tutorial version and easy access to functionalities, in your product use a stable and production ready database (Poastgres, MySQL, Mongo, Oracle):
```sh
python3 manage.py migrate
```

*Recommended superuser(admin) creation, it will helps to manage data in the UI
Then we can run the project as simple as:
```sh
python3 manage.py createsuperuser
```

Then we can run the project as simple as:
```sh
python3 manage.py runserver
```

## Base


## Changes

