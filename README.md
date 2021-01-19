# Django Template Project / RESTful API

This a Django 3.0+ project

## Features

- Django 3.0+
- [Django REST Framework](https://www.django-rest-framework.org/) - Powerful and flexible toolkit for building Web APIs.
- [Django REST Registration](https://django-rest-registration.readthedocs.io/en/latest/index.html) - User registration REST API, based on Django-REST-Framework.
- [Django Cors Headers](https://pypi.org/project/django-cors-headers/) - A Django application for handling the server headers required for Cross-Origin Resource Sharing (CORS).
- [Django Filter](https://django-filter.readthedocs.io/en/stable/) - Simple way to filter down a queryset based on parameters a user provides.
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) - A JSON Web Token authentication plugin for the Django REST Framework.
- [Whitenoise](http://whitenoise.evans.io/en/stable/) - Radically simplified static file serving for Python web apps
- Procfile for running gunicorn with New Relic's Python agent.
- Support for automatic generation of [OpenAPI](https://www.openapis.org/) schemas.

## Prerequisites

- Python 3.5>
- POSTMAN
- Virtualenv
- Git

## Instalation

    $ python3 -m venv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt
    $ python manage.py migrate
    $ python manage.py createsuperuser

## Run project

    $ python manage.py runserver

### Assignments

- 10 Examples of ORM Create
- 10 Examples of ORM List/Filter/Order
- 5 Examples of ORM Get
- 5 Examples of ORM Update/Partial
- 5 Examples of ORM Delete

### Glossary

- Model
- Serializer
- Viewset
- Mixin
- JSON
- Headers
  - Content-Type
  - Authorization
  - Cookie
  - Accept
  - Content-Length
  - Attachment
- Parsers
- Renders
- Status codes
  - 200:
  - 201:
  - 400:
  - 401:
  - 404:
  - 500:
    ...
- HTTP Methods:
  - GET
  - POST
  - PUT
  - PATCH
  - DELETE
  - HEAD
  - OPTIONS
- JWT
  - Definition
  - HS254
- OpenAPI
 - 

## License

The MIT License (MIT)

Copyright (c) 2020 Raúl Novelo

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
