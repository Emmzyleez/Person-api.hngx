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
- [GitHub Repository](#github-repository)
- [Documentation](#documentation)
- [Setup Instructions](#setup-instructions)
- [API Usage](#api-usage)
  - [Request/Response Formats](#requestresponse-formats)
  - [Sample Usage](#sample-usage)
- [Hosting](#hosting)
- [Known Limitations and Assumptions](#known-limitations-and-assumptions)
- [Acceptance Criteria](#acceptance-criteria)

## Introduction

This project is a simple REST API built using Python, specifically the Django and Django Rest Framework, capable of performing CRUD (Create, Read, Update, Delete) operations on a "person" resource. The API interfaces with a chosen database and is designed to handle parameters dynamically.

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

- Endpoint: /api/{user_id}
- Description: Fetches details of a person by their ID.
- HTTP Method: GET
- Response Example:
  ```json
  {
    "id": 1,
    "name": "Emmanuel Moses"
  }

### UPDATE

- Endpoint: /api/{user_id}
- Description: Modifies details of an existing person by their ID.
- HTTP Method: PUT
- Request Body Example:
  ```json
  {"name": "Updated Name"}
- Response: Returns the updated person's details.

### DELETE
- Endpoint: /api/{user_id}
- Description: Removes a person by their ID.
- HTTP Method: DELETE
- Response: Returns a success message.

## Database Modeling
Optionally, we have provided UML diagrams to illustrate the project's class and model structure. [UML Diagram Link]

## Testing
Testing scripts for CRUD operations using tools like Postman or Python scripts are available. You can use these scripts to:

- Add a new person.
- Fetch details of a person.
- Modify the details of an existing person.
- Remove a person.

## Dynamic Parameter Handling
The API is designed to handle dynamic input. You can perform operations using a person's name. For example, if you pass "Emmanuel Moses," you can perform all CRUD operations on "Emmanuel Moses."

## GitHub Repository
The project is hosted on GitHub, and the repository contains essential files and resources: [GitHub Repository Link]

## Documentation
Detailed documentation on how to set up, run, and use the API is provided in the repository's README.md file. Please refer to the README for comprehensive instructions.

## Hosting
The API is hosted on a server with the following URL: https://myexistingdomain.com/api.

## Acceptance Criteria
- The API successfully performs all CRUD operations.
- Clear and accurate UML diagrams are provided.
- Testing scripts successfully test all CRUD operations without manual intervention.
- The API correctly handles and responds to different parameters.
- The GitHub repository is well-organized and publicly accessible.
- Documentation provides clear guidance on API usage, setup, request/response formats, and sample usage.
