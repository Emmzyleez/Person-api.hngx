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

### 

- Endpoint: /api/{user_id}
- Description: Fetches details of a person by their ID.
- HTTP Method: GET
- Response Example:
  ```json
  {
    "id": 1,
    "name": "Emmanuel Moses"
  }

  
