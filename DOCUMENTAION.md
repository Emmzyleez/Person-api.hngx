# Person API

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [REST API Development](#rest-api-development)
  - [CREATE](#create)
  - [READ](#read)
  - [UPDATE](#update)
  - [DELETE](#delete)
- [Database Modeling](#database-modeling)
- [Testing](#testing)
- [Dynamic Parameter Handling](#dynamic-parameter-handling)
- [Setup Instructions](#setup-instructions)
- [GitHub Repository](#github-repository)
- [Documentation](#documentation)
- [Hosting](#hosting)
- [Assumptions](#assumptions)
- [Limitations](#limitations)

## Introduction

This project is a simple REST API built using Python, specifically the Django and Django Rest Framework, capable of performing CRUD (Create, Read, Update, Delete) operations on a "person" resource. You can add new people, fetch details of existing people, update their information, and remove them from the database.

## Requirements

The project requirements include:

1. **REST API Development**: Develop an API with endpoints for CRUD operations.
2. **Database Modeling**: Optionally, create UML diagrams to represent the system's design and database structure.
3. **Testing**: Use tools like Postman or Python scripts to test CRUD operations.
4. **Dynamic Parameter Handling**: Ensure the API can handle dynamic input for operations using a person's name.
5. **GitHub Repository**: Create a well-organized GitHub repository with essential files.
6. **Documentation**: Provide clear documentation outlining request/response formats, setup instructions, sample usage, known limitations, assumptions, and more.
7. **Hosting**: Host the API on a server and ensure accessibility.

## REST API Development

### CREATE

- Endpoint: `/api`
- Description: Adds a new person to the database.
- HTTP Method: POST
- Request Body Example:
  ```json
  {"name": "Emmanuel Moses"}
- Response: Returns the created person's details.

### READ

- Endpoint: `/api/{user_id}`
- Description: Fetches details of a person by their ID.
- HTTP Method: GET
- Response Example:
  ```json
  {
    "id": 1,
    "name": "Emmanuel Moses"
  }

### UPDATE

- Endpoint: `/api/{user_id}`
- Description: Modifies details of an existing person by their ID.
- HTTP Method: PUT
- Request Body Example:
  ```json
  {"name": "Updated Name"}
- Response: Returns the updated person's details.

### DELETE
- Endpoint: `/api/{user_id}`
- Description: Removes a person by their ID.
- HTTP Method: DELETE
- Response: Returns a success message.
  
## Testing
Testing scripts for CRUD operations using tools like Postman or Python scripts are available. You can use these scripts to:

- Add a new person.
- Fetch details of a person.
- Modify the details of an existing person.
- Remove a person.

## Dynamic Parameter Handling
The API is designed to handle dynamic input. You can perform operations using a person's name. For example, if you pass "Emmanuel Moses," you can perform all CRUD operations on "Emmanuel Moses."

## Setup Instructions

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

## GitHub Repository
The project is hosted on GitHub, and the repository contains essential files and resources: https://github.com/Emmzyleez/person-api-hngx

## Documentation
Detailed documentation on how to set up, run, and use the API is provided in the repository's [README.md file](https://github.com/Emmzyleez/person-api-hngx/blob/main/README.md). Please refer to the [README](https://github.com/Emmzyleez/person-api-hngx/blob/main/README.md) for comprehensive instructions.

## Hosting
The API is hosted on a server with the following URL: https://emmzyleez.pythonanywhere.com/api/

## Assumptions
- The API successfully performs all CRUD operations.
- Clear and accurate UML diagrams are provided.
- Testing scripts successfully test all CRUD operations without manual intervention.
- The API correctly handles and responds to different parameters.
- The API correctly validates the 'name' field as a string only
- The GitHub repository is well-organized and publicly accessible.
- Documentation provides clear guidance on API usage, setup, request/response formats, and sample usage.

## Limitations
API provides basic error handling, but there may be situations where more detailed error messages are needed for debugging, which are not currently implemented.
