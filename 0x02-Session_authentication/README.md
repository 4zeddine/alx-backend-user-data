# Session Authentication

This project focuses on implementing session authentication for user authentication in a web application.

## Project Overview

The goal is to enhance the existing Basic authentication system by adding session-based authentication. This allows for a more user-friendly experience, especially for web browsers that support cookies.

## Key Components

1. **SessionAuth Class**: A new authentication class that manages session creation and user identification.
2. **Session ID**: Unique identifiers generated for each user session.
3. **Cookie-based Storage**: Storing session IDs in cookies for persistent authentication.
4. **User Retrieval**: Methods to retrieve user information based on session IDs.
5. **Login/Logout Functionality**: Endpoints for user login and logout using session authentication.
6. **Session Expiration**: Implementation of session expiration for enhanced security.
7. **Database Integration**: Storing session information in a database for persistence across server restarts.

## Main Tasks

1. Create the SessionAuth class
2. Implement session creation and user ID retrieval methods
3. Add cookie handling for session IDs
4. Update the API to use session authentication
5. Create login and logout endpoints
6. Implement session expiration
7. Integrate session storage with a database

## API Endpoints

- `GET /api/v1/users/me`: Retrieve the authenticated user's information
- `POST /api/v1/auth_session/login`: User login
- `DELETE /api/v1/auth_session/logout`: User logout

## Environment Variables

- `AUTH_TYPE`: Set to 'session_auth' to enable session authentication
- `SESSION_NAME`: Name of the cookie used for storing the session ID
- `SESSION_DURATION`: Duration of the session in seconds

## Getting Started

1. Clone the repository
2. Set up the required environment variables
3. Install dependencies
4. Run the application

## Resources

- [REST API Authentication Mechanisms - Only the session auth part](https://www.youtube.com/watch?v=501dpx2IjGY)
- [HTTP Cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)
- [Flask](https://flask.palletsprojects.com/)
- [Flask Cookie](https://flask.palletsprojects.com/en/1.1.x/quickstart/#cookies)