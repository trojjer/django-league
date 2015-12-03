# django-league
Demo Django app dealing with sports data.

Built with Python 3.4.3 and Django 1.9.

## Installation
- Clone this repo and cd to base directory.
- I used virtualenvwrapper; the resulting virtualenv directory is external to the project and this repo.
A virtualenv therefore needs to be created, either with `mkvirtualenv` or otherwise (with Python 3.4.3). Once this is done:

```
$ pip install -r requires/install.pip
$ cd league
$ python manage.py migrate
$ python manage.py runserver
```
