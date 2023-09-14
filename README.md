# Person Api

## Description

This project is a simple REST API built using Python and Django Rest Framework. It allows you to perform CRUD (Create, Read, Update, Delete) 
operations on a "person" resource. You can add new people, fetch details of existing people, 
update their information, and remove them from the database. 

## Table of Contents

* [Getting Started](getting_started)
  * [Prequisites](prequisites)
  * [Installation](installation)
* [Usage](usage)
  * [Endpoints](endpoints)
  * [Request Parameters](request_parameters)
  * [Examples](examples)
* [UML Diagrams](uml_diagrams)
* [GitHub Repository](github_repository)
* [Documentation](documentation)
* [Hosting](hosting)

## Prerequisites

Before you begin, make sure you have the following prerequisites installed:

* Python 3.x
* Django
* Django Rest Framework
  
## Installation

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
   django-admin startproject person_api .
6. Create a new Django App:

   ```bash
   python manage.py startapp myapp
7. Apply database migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
    
