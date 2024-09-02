# Basic Authentication Project

## Overview
This project implements Basic authentication for an API. It covers various aspects of authentication, error handling, and API security.

## Task List

### 0. Simple Basic API
- [x] Set up the server
- [x] Test the API functionality

### 1. Unauthorized Error Handler
- [x] Implement 401 error handler in `api/v1/app.py`
- [x] Add `/api/v1/unauthorized` endpoint in `api/v1/views/index.py`

### 2. Forbidden Error Handler
- [x] Implement 403 error handler in `api/v1/app.py`
- [x] Add `/api/v1/forbidden` endpoint in `api/v1/views/index.py`

### 3. Auth Class
- [x] Create `Auth` class in `api/v1/auth/auth.py`
- [x] Implement required methods:
  - `require_auth`
  - `authorization_header`
  - `current_user`

### 4. Request Validation
- [x] Update `require_auth` method in `Auth` class
- [x] Implement path validation logic

### 5. Basic Auth
- [x] Create `BasicAuth` class
- [x] Update `api/v1/app.py` to use `BasicAuth`

### 6. Base64 Extraction
- [x] Implement `extract_base64_authorization_header` method

### 7. Base64 Decoding
- [x] Implement `decode_base64_authorization_header` method

### 8. User Credentials Extraction
- [x] Implement `extract_user_credentials` method

### 9. User Object
- [x] Implement `user_object_from_credentials` method

### 10. Overload Current User
- [x] Implement `current_user` method in `BasicAuth`

### 11. Allow Password with ":"
- [x] Improve `extract_user_credentials` to handle passwords with `:`

### 12. Require Auth with Stars
- [x] Enhance `require_auth` to support wildcard exclusions

## Resources
- [REST API Authentication Mechanisms](https://intranet.alxswe.com/rltoken/ssg5umgsMk5jKM8WRHk2Ug)
- [Base64 in Python](https://intranet.alxswe.com/rltoken/RpaPRyKx1rdHgRSUyuPfeg)
- [HTTP header Authorization](https://intranet.alxswe.com/rltoken/WlARq8tQPUGQq5VphLKM4w)
- [Flask](https://intranet.alxswe.com/rltoken/HG5WXgSja5kMa29fbMd9Aw)
- [Base64 Concept](https://intranet.alxswe.com/rltoken/br6Rp4iMaOce6EAC-JQnOw)