# Online Test Management System

## Project Description

An online test management system where admins can create tests and users can attempt the tests and receive their results. Built with FastAPI and MySQL.

## Features

- Admin: Manage tests (CRUD operations), questions, and view user results.
- User: Register, login, view available tests, submit answers, and view results.
- User authentication and authorization.

## Setup and Installation

1. **Clone the repository**
    ```bash
    git clone <repository-url>
    cd online_test_management
    ```

2. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3. **Setup MySQL Database**
    ```sql
    # Run the SQL script to create the database and tables
    mysql -u <username> -p < database_name> < schema.sql
    ```

4. **Run the application**
    ```bash
    python run_server.py
    ```

5. **Run tests**
    ```bash
    pytest
    ```

## Docker

1. **Build Docker image**
    ```bash
    docker build -t online_test_management .
    ```

2. **Run Docker container**
    ```bash
    docker run -d -p 8000:8000 online_test_management
    ```

## API Endpoints

### Auth
- POST `/auth/register`
- POST `/auth/login`

### Admin
- POST `/admin/tests`
- POST `/admin/tests/{test_id}/questions`
- GET `/admin/results`

### User
- GET `/user/tests`
- POST `/user/submit`
- GET `/user/results`

## Testing with Postman

1. **Import Postman Collection**
    - Open Postman
    - Click on `Import`
    - Select `postman_collection.json` from the project directory

2. **Register User**
    - Select `Register User` request
    - Click `Send`

3. **Login User**
    - Select `Login User` request
    - Click `Send`
    - Copy the `access_token` from the response

4. **Create Test**
    - Select `Create Test` request
    - Click on `Authorization` tab and select `Bearer Token`
    - Paste the `access_token` in the `Token` field
    - Click `Send`

5. **List Tests**
    - Select `List Tests` request
    - Click `Send`
