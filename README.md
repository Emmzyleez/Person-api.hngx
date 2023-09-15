# Person Api


## Description

This project is a simple REST API built using Python and Django Rest Framework. It allows you to perform CRUD (Create, Read, Update, Delete) 
operations on a "person" resource. You can add new people, fetch details of existing people, 
update their information, and remove them from the database. 


## Table of Contents

* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
  * [Endpoints](#endpoints)
  * [Request Parameters](#request-parameters)
  * [Examples](#examples)
* [Source Code](#source-code)
* [Documentation](#documentation)
* [Hosting](#hosting)
  
## Getting Started

### Prerequisites

Before you begin, make sure you have the following prerequisites installed:

* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [Django Rest Framework](https://www.django-rest-framework.org/)
    
### Installation

1. Clone the GitHub repository:

   ```bash
   git clone https://github.com/emmzyleez/person-api-hngx.git 
2. Navigate to the project directory:

   ```bash
   cd person-api-hngx
 3. Create and activate virtual environment
    
    ```bash
    python -m venv .venv
    venv\scripts\activate
 4. Install project dependencies:

    ```bash
    pip install -r requirements.txt
5. Create a new Django project:

   ```bash
   django-admin startproject person .
6. Create a new Django App:

   ```bash
   python manage.py startapp myapp
7. Apply database migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
8. Start the development server:

   ```bash
   python manage.py runserver
   
The Person API should now be running locally at `http://localhost:8000/`


## Usage
### Endpoints
* `POST /api`: Create a new person by providing their name.
* `GET /api/<user_id>`: Retrieve details of a person by their unique user ID.
* `PUT /api/<user_id>`: Update the details of an existing person by their user ID.
* `DELETE /api/<user_id>`: Remove a person from the database by their user ID.

### Request Parameters
For `POST /api`: Send a JSON request with the `name` attribute to create a new person. Example: `{"name": "Emmanuel Moses"}`.

For `GET /api/<user_id>`, `PUT /api/<user_id>`, and `DELETE /api/<user_id>`: Replace `<user_id>` with the unique identifier of the person you want to access.

### Examples
Here are some sample API usage examples:

* Create a Person (POST):
 Send a POST request to /api with the following JSON body:
  ```json
  {"name": "Emmanuel Moses"} 
* Fetch Person Details (GET):
  Send a GET request to /api/1 to retrieve details for the person with ID 1.
* Update Person Details (PUT):
  Send a PUT request to /api/1 with updated information to modify the details of the   person with ID 1.
* Remove a Person (DELETE):
  Send a DELETE request to /api/1 to remove the person with ID 1 from the database.

## Source Code

- In `models.py`, define and validate the `Person` model.

```python
# models.py
from django.db import models
from django.core.validators import RegexValidator

string_only_validator = RegexValidator(
    regex=r'^[a-zA-Z\s]*$',
    message='Only strings are allowed.',
    code='invalid_string'
)

class Person(models.Model):
    name = models.CharField(max_length=250, validators=[string_only_validator])

```

- In `views.py`, create views for handling HTTP requests and responses related to the Person model
```python
# views.py
from rest_framework import generics
from .models import Person
from .serializers import PersonSerializer

class PersonListView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

```


## Documentation
For detailed information on request/response formats, setup instructions, and sample API usage, please refer to the [DOCUMENTATION.md](https://github.com/Emmzyleez/person-api-hngx/blob/main/DOCUMENTAION.md) file in the repository.


## Hosting
The Person API is hosted on https://emmzyleez.pythonanywhere.com/api


