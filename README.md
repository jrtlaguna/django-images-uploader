# Django Image Uploader

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/jrtlaguna/django-images-uploader.git
$ cd django-images-uploader
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python3.8 -m virtualenv venv
$ source venv/bin/activate
```

Then install the dependencies:

```sh
(venv)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies:
```sh
(venv)$ python manage.py migrate
(venv)$ python manage.py runserver
```
