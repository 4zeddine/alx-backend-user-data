# User Authentication Service

This project contains tasks for learning to create a user authentication service.

## Requirements

- SQLAlchemy 1.3.x
- pycodestyle 2.5
- bcrypt
- python3 3.7

## Tasks

### 0. User model
- File: [user.py](user.py)
- Description: Implement a SQLAlchemy model named `User` for a database table named `users`.
- Attributes:
  - `id`: integer primary key
  - `email`: non-nullable string
  - `hashed_password`: non-nullable string
  - `session_id`: nullable string
  - `reset_token`: nullable string

### 1. Create user
- File: [db.py](db.py)
- Description: Complete the `DB` class to implement the `add_user` method.
- Requirements:
  - Method takes `email` and `hashed_password` as arguments
  - Returns a `User` object
  - Saves the user to the database

### 2. Find user
- File: [db.py](db.py)
- Description: Implement the `DB.find_user_by` method.
- Requirements:
  - Takes arbitrary keyword arguments
  - Returns the first row found in the `users` table as filtered by the input arguments
  - Raises appropriate exceptions when no results are found or wrong query arguments are passed

### 3. Update user
- File: [db.py](db.py)
- Description: Implement the `DB.update_user` method.
- Requirements:
  - Takes `user_id` and arbitrary keyword arguments
  - Updates the user's attributes and commits changes to the database
  - Raises `ValueError` for invalid arguments

### 4. Hash password
- File: [auth.py](auth.py)
- Description: Implement the `_hash_password` method.
- Requirements:
  - Takes a password string argument
  - Returns bytes (a salted hash of the input password)
  - Use `bcrypt.hashpw`

### 5. Register user
- File: [auth.py](auth.py)
- Description: Implement the `Auth.register_user` method.
- Requirements:
  - Takes `email` and `password` arguments
  - Returns a `User` object
  - If user exists, raise `ValueError`
  - If not, hash the password and save the user to the database

### 6. Basic Flask app
- File: [app.py](app.py)
- Description: Create a basic Flask app.
- Requirements:
  - Single `GET` route (`"/"`)
  - Returns JSON payload: `{"message": "Bienvenue"}`

### 7. Register user route
- File: [app.py](app.py)
- Description: Implement the user registration endpoint.
- Requirements:
  - Route: `POST /users`
  - Use `Auth` object
  - If user is created, return JSON payload: `{"email": "<registered email>", "message": "user created"}`
  - If user already exists, return JSON payload: `{"message": "email already registered"}` with 400 status code

### 8. Credentials validation
- File: [auth.py](auth.py)
- Description: Implement the `Auth.valid_login` method.
- Requirements:
  - Takes `email` and `password` arguments
  - Returns a boolean
  - Use `bcrypt.checkpw` to validate password

### 9. Generate UUIDs
- File: [auth.py](auth.py)
- Description: Implement the `_generate_uuid` function.
- Requirements:
  - Returns a string representation of a new UUID
  - Use the `uuid` module

### 10. Get session ID
- File: [auth.py](auth.py)
- Description: Implement the `Auth.create_session` method.
- Requirements:
  - Takes an `email` argument
  - Returns the session ID as a string
  - Find the user, generate a new UUID, store it in the database as the user's `session_id`

### 11. Log in
- File: [app.py](app.py)
- Description: Implement the `login` function for the `POST /sessions` route.
- Requirements:
  - If login is successful, create a new session and return JSON payload: `{"email": "<user email>", "message": "logged in"}`
  - If login fails, abort with 401 HTTP status

### 12. Find user by session ID
- File: [auth.py](auth.py)
- Description: Implement the `Auth.get_user_from_session_id` method.
- Requirements:
  - Takes a `session_id` argument
  - Returns the corresponding `User` or `None`

### 13. Destroy session
- File: [auth.py](auth.py)
- Description: Implement the `Auth.destroy_session` method.
- Requirements:
  - Takes a `user_id` argument
  - Updates the user's `session_id` to `None`

### 14. Log out
- File: [app.py](app.py)
- Description: Implement the `logout` function for the `DELETE /sessions` route.
- Requirements:
  - If user exists, destroy the session and redirect to `GET /`
  - If user does not exist, respond with 403 HTTP status

### 15. User profile
- File: [app.py](app.py)
- Description: Implement the `profile` function for the `GET /profile` route.
- Requirements:
  - If user exists, return JSON payload: `{"email": "<user email>"}`
  - If session ID is invalid or user does not exist, respond with 403 HTTP status

### 16. Generate reset password token
- File: [auth.py](auth.py)
- Description: Implement the `Auth.get_reset_password_token` method.
- Requirements:
  - Takes an `email` argument
  - If user exists, generate a UUID and update the user's `reset_token` database field
  - If user does not exist, raise a `ValueError`

### 17. Get reset password token
- File: [app.py](app.py)
- Description: Implement the `get_reset_password_token` function for the `POST /reset_password` route.
- Requirements:
  - If email is registered, respond with JSON payload: `{"email": "<user email>", "reset_token": "<reset token>"}`
  - If email is not registered, respond with 403 status code

### 18. Update password
- File: [auth.py](auth.py)
- Description: Implement the `Auth.update_password` method.
- Requirements:
  - Takes `reset_token` and `password` arguments
  - If reset_token is invalid, raise a `ValueError`
  - Otherwise, hash the password and update the user's `hashed_password` and `reset_token` fields

### 19. Update password end-point
- File: [app.py](app.py)
- Description: Implement the `update_password` function for the `PUT /reset_password` route.
- Requirements:
  - If token is valid, respond with JSON payload: `{"email": "<user email>", "message": "Password updated"}`
  - If token is invalid, respond with 403 HTTP code

### 20. End-to-end integration test
- File: [main.py](main.py)
- Description: Implement end-to-end integration tests for all endpoints.
- Requirements:
  - Implement functions for each sub-task (register, login, logout, etc.)
  - Use the `requests` module to query your web server
  - Use `assert` to validate responses

## Resources
- [Flask documentation](https://flask.palletsprojects.com/)
- [Requests module](https://docs.python-requests.org/en/latest/)
- [HTTP status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)