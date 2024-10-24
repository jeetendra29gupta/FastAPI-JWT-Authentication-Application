# FastAPI JWT Authentication Application

Welcome to the FastAPI JWT Authentication Application! This project demonstrates how to implement user authentication and authorization using JSON Web Tokens (JWT) in a FastAPI framework. It uses TinyDB for lightweight data storage, providing a simple and efficient solution for managing user data.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [TinyDB](#tinydb)
- [Requirements](#requirements)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
  - [Welcome Endpoint](#welcome-endpoint)
  - [User Signup](#user-signup)
  - [User Login](#user-login)
  - [Protected Endpoint](#protected-endpoint)
  - [Refresh Token](#refresh-token)
- [Testing](#testing)
- [Acknowledgments](#acknowledgments)

## Features

- **User Registration**: Sign up users with full name, username, and password.
- **User Authentication**: Login to receive access and refresh tokens.
- **Protected Routes**: Access restricted content with valid tokens.
- **Token Refresh**: Refresh access tokens without re-authentication.
- **Error Handling**: User-friendly error messages for common issues.
- **Lightweight Database**: Uses TinyDB for easy user data management.

## Technologies Used

- **FastAPI**: High-performance web framework for building APIs.
- **JWT**: For token management.
- **TinyDB**: Lightweight document-oriented database for storing user data.
- **Python**: Programming language.
- **Uvicorn**: ASGI server for running the application.

## TinyDB

[TinyDB](https://tinydb.readthedocs.io/) is a simple, lightweight document-oriented database implemented in pure Python. It is designed for easy use and requires no external dependencies, making it ideal for small projects. In this application, TinyDB is employed to store user information, including usernames and hashed passwords, offering an efficient way to handle data without the complexity of a larger database system.

## Requirements

- Python 3.7 or higher

## Getting Started

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/jeetendra29gupta/FastAPI-JWT-Authentication-Application.git
   cd FastAPI-JWT-Authentication-Application
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:

   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install required packages**:

   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

To start the FastAPI application, run:

```bash
python fastapi_jwt_main_app.py
```

Now, navigate to `http://localhost:8181` in your web browser to interact with the API.

## API Endpoints

### Welcome Endpoint

- **GET /**  
  **Description**: Returns a welcome message.  
  **Response**:
  ```json
  {
      "status_code": 200,
      "detail": "Welcome to FastAPI JWT Application"
  }
  ```

### User Signup

- **POST /signup**  
  **Request Body**:
  ```json
  {
      "full_name": "User Full Name",
      "username": "username",
      "password": "your_password"
  }
  ```
  **Response**:
  ```json
  {
      "status_code": 201,
      "detail": "User created successfully, user ID {user_id}!",
      "user": {
          "full_name": "User Full Name",
          "username": "username"
      }
  }
  ```
  **Error**: If the username is already taken, returns a 400 error.

### User Login

- **POST /login**  
  **Request Body**:
  ```json
  {
      "username": "username",
      "password": "your_password"
  }
  ```
  **Response**:
  ```json
  {
      "token_type": "bearer",
      "access_token": "your_access_token",
      "refresh_token": "your_refresh_token"
  }
  ```

### Protected Endpoint

- **GET /protected**  
  **Authorization**: Bearer token required in the header.  
  **Response**:
  ```json
  {
      "message": "Welcome, {username}!"
  }
  ```

### Refresh Token

- **GET /refresh_token**  
  **Authorization**: Bearer token required in the header.  
  **Response**:
  ```json
  {
      "token_type": "bearer",
      "access_token": "new_access_token",
      "refresh_token": "new_refresh_token"
  }
  ```

## Testing

To run the tests, make sure you have pytest installed:
Run the tests using:

```bash
pytest test_fastapi_jwt_main_app.py
```
Output:

```txt
C:\Users\Admin\Workspace\python_project\.venv\Scripts\python.exe "C:/Program Files/JetBrains/PyCharm Community Edition 2024.2.3/plugins/python-ce/helpers/pycharm/_jb_pytest_runner.py" --path C:\Users\Admin\Workspace\python_project\test_fastapi_jwt_main_app.py 
Testing started at 14:53 ...
Launching pytest with arguments C:\Users\Admin\Workspace\python_project\test_fastapi_jwt_main_app.py --no-header --no-summary -q in C:\Users\Admin\Workspace\python_project

============================= test session starts =============================
collecting ... collected 8 items

test_fastapi_jwt_main_app.py::test_index PASSED                          [ 12%]
test_fastapi_jwt_main_app.py::test_signup PASSED                         [ 25%]
test_fastapi_jwt_main_app.py::test_signup_existing_user PASSED           [ 37%]
test_fastapi_jwt_main_app.py::test_login PASSED                          [ 50%]
test_fastapi_jwt_main_app.py::test_protected PASSED                      [ 62%]
test_fastapi_jwt_main_app.py::test_protected_no_token PASSED             [ 75%]
test_fastapi_jwt_main_app.py::test_refresh_token PASSED                  [ 87%]
test_fastapi_jwt_main_app.py::test_refresh_token_no_token PASSED         [100%]

============================== 8 passed in 1.43s ==============================

Process finished with exit code 0
```


## Acknowledgments

- **FastAPI Documentation**: [FastAPI](https://fastapi.tiangolo.com/)
- **JWT Documentation**: [JWT.io](https://jwt.io/)
- **TinyDB Documentation**: [TinyDB](https://tinydb.readthedocs.io/)
- **Workflow**: For a more comprehensive understanding of the workflow, please refer to `fastapi_jwt_run_app.py`, where requests and session management are utilized to interact with the various endpoints.

Output:
```txt
C:\Users\Admin\Workspace\python_project\.venv\Scripts\python.exe C:\Users\Admin\Workspace\python_project\fastapi_jwt_run_app.py 
# Call the welcome endpoint
{'status_code': 200, 'detail': 'Welcome to FastAPI JWT Application'}

# Dummy user list
[{'full_name': 'Jeetendra Gupta', 'username': 'juju_raven', 'password': 'juju@raven#1814'}, {'full_name': 'Sameer Gupta', 'username': 'black_rose', 'password': 'black@rose#1814'}, {'full_name': 'Prince Gupta', 'username': 'blue_bird', 'password': 'blue@bird#1814'}]

# Sign up users
{'detail': 'User created successfully, user ID 1!', 'user': {'full_name': 'Jeetendra Gupta', 'username': 'juju_raven'}}
{'detail': 'User created successfully, user ID 2!', 'user': {'full_name': 'Sameer Gupta', 'username': 'black_rose'}}
{'detail': 'User created successfully, user ID 3!', 'user': {'full_name': 'Prince Gupta', 'username': 'blue_bird'}}

# Sign up with already users
{'error': 'Error 400: {"detail":"Username: juju_raven, already registered"}'}
{'error': 'Error 400: {"detail":"Username: black_rose, already registered"}'}
{'error': 'Error 400: {"detail":"Username: blue_bird, already registered"}'}

# Log in the given user to get tokens
{'token_type': 'bearer', 'access_token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqdWp1X3JhdmVuIiwiZXhwIjoxNzI5NzgyNTQ3fQ.B7M3oSCx35X-gn97l53mODO2U68-UjNgEEYh4oRbhl4', 'refresh_token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqdWp1X3JhdmVuIiwiZXhwIjoxNzMwMzg1NTQ3fQ.xYCW6rluK8dyZcWO3R1wleYs7xHh2yUvh0UWfnvbdoA'}

# Access protected endpoint
{'message': 'Welcome, juju_raven!'}

# Refresh the access token
{'token_type': 'bearer', 'access_token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqdWp1X3JhdmVuIiwiZXhwIjoxNzI5NzgyNTQ3fQ.B7M3oSCx35X-gn97l53mODO2U68-UjNgEEYh4oRbhl4', 'refresh_token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqdWp1X3JhdmVuIiwiZXhwIjoxNzMwMzg1NTQ3fQ.xYCW6rluK8dyZcWO3R1wleYs7xHh2yUvh0UWfnvbdoA'}

#Access protected endpoint again with the new access token
{'message': 'Welcome, juju_raven!'}

Process finished with exit code 0
```