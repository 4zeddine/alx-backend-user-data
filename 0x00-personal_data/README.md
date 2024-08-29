# Personal Data Project

Learn how to protect user personal data through various tasks.

## Tasks

### 0. Regex-ing
- **File:** `filtered_logger.py`
- **Function:** `filter_datum`
- **Features:**
  - Obfuscate specified fields in a log message using regex.
  - Arguments:
    - `fields`: List of strings representing fields to obfuscate.
    - `redaction`: String to replace the field's value.
    - `message`: Log message to be processed.
    - `separator`: Character separating fields in the log message.
  - The function uses `re.sub` to perform the substitution with a single regex.
  - The function should be less than 5 lines long.

### 1. Log Formatter
- **File:** `filtered_logger.py`
- **Class:** `RedactingFormatter`
- **Features:**
  - Custom formatter class for logging.
  - Redact sensitive fields in log records.
  - Constructor accepts a list of fields to filter.
  - Implement `format` method using `filter_datum` to filter log messages.
  - The `format` method should be less than 5 lines long.

### 2. Create Logger
- **File:** `filtered_logger.py`
- **Function:** `get_logger`
- **Features:**
  - Create and configure a logger named `"user_data"`.
  - Set logging level to `logging.INFO`.
  - Add a `StreamHandler` with `RedactingFormatter`.
  - Prevent propagation to other loggers.
  - Define a `PII_FIELDS` tuple containing important fields from `user_data.csv`.

### 3. Connect to Secure Database
- **File:** `filtered_logger.py`
- **Function:** `get_db`
- **Features:**
  - Connect to a MySQL database using environment variables for credentials.
  - Retrieve database connection as a `mysql.connector.connection.MySQLConnection` object.
  - Environment variables:
    - `PERSONAL_DATA_DB_USERNAME` (default: "root").
    - `PERSONAL_DATA_DB_PASSWORD` (default: "").
    - `PERSONAL_DATA_DB_HOST` (default: "localhost").
    - `PERSONAL_DATA_DB_NAME`.

### 4. Read and Filter Data
- **File:** `filtered_logger.py`
- **Function:** `main`
- **Features:**
  - Retrieve all rows from the `users` table in the database.
  - Log each row with sensitive fields filtered.
  - Filtered fields include `name`, `email`, `phone`, `ssn`, and `password`.
  - Only the `main` function should run when the module is executed.

### 5. Encrypting Passwords
- **File:** `encrypt_password.py`
- **Function:** `hash_password`
- **Features:**
  - Encrypt user passwords using bcrypt.
  - Return a salted, hashed password as a byte string.
  - Use the `bcrypt` package with `hashpw` for encryption.

### 6. Check Valid Password
- **File:** `app.py`
- **Function:** `is_valid`
- **Features:**
  - Validate a password against a hashed password using bcrypt.
  - Arguments:
    - `hashed_password`: Byte string of the hashed password.
    - `password`: Plaintext password to validate.
  - Return `True` if the password matches, otherwise `False`.

## Resources

- [What Is PII, non-PII, and Personal Data?](https://intranet.alxswe.com/rltoken/jf71oYqiETchcVhPzQVnyg)
- [Logging Documentation](https://intranet.alxswe.com/rltoken/W2JiHD6cbJY1scJORyLqnw)
- [bcrypt Package](https://intranet.alxswe.com/rltoken/41oaQXfzwnF1i-wT8W0vHw)
- [Logging to Files, Setting Levels, and Formatting](https://intranet.alxswe.com/rltoken/XCpI9uvguxlTCsAeRCW6SA)
