# eProject 0x00: Personal Data Back-end Authentication

## Overview
This project focuses on handling personal data, implementing authentication, and securing sensitive information in a back-end application. The main objectives include understanding personally identifiable information (PII), implementing log filters to obfuscate PII fields, encrypting passwords, and authenticating to a database using environment variables.

## Learning Objectives

Understand what constitutes PII, such as names, addresses, social security numbers, and more, and recognize the importance of protecting this data. [Resource: [What is Personally Identifiable Information (PII)?](https://www.varonis.com/blog/what-is-pii-personally-identifiable-information/)]

- **Implementing a log filter to obfuscate PII fields**: Learn how to create a function that obscures sensitive information in log messages, ensuring that PII is not exposed in logs. This involves identifying PII fields and replacing them with placeholder values or redacted versions. [Resource: [Logging and Handling Sensitive Data](https://www.owasp.org/index.php/Logging_Cheat_Sheet#Mask_or_Redact_Sensitive_Data)]

- **Encrypting passwords and validating input passwords**: Understand the importance of securely storing passwords by encrypting them with a salted hash. Learn how to use bcrypt for password hashing and validation. This ensures that even if the password hashes are compromised, they cannot be easily decrypted. [Resource: [Hashing Passwords Correctly](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html#use-a-strong-and-robust-credential-storage-and-password-hashing-algorithm)]

- **Authenticating to a database using environment variables**: Learn best practices for securely accessing databases by retrieving credentials from environment variables, enhancing the security of your application. This prevents hardcoding sensitive information in your code, reducing the risk of exposure. [Resource: [Storing Secrets Safely](https://cloud.google.com/solutions/secrets-management)]

## Requirements
### 0. Regex-ing
Write a function called `filter_datum` that returns an obfuscated log message:

- **Arguments**:
  - `fields`: a list of strings representing all fields to obfuscate
  - `redaction`: a string representing how the field will be obfuscated
  - `message`: a string representing the log line
  - `separator`: a string representing the character separating all fields in the log line (message)
  
The function should use a regex to replace occurrences of certain field values. `filter_datum` should be less than 5 lines long and use `re.sub` to perform the substitution with a single regex. This task helps you understand how to use regular expressions to efficiently replace sensitive information in log messages. [Resource: [Regular Expressions in Python](https://docs.python.org/3/library/re.html)]

### 1. Log Formatter
Update the `RedactingFormatter` class to accept a list of strings `fields` as a constructor argument. Implement the `format` method to filter values in incoming log records using `filter_datum`. Values for fields in `fields` should be filtered. This task enhances your understanding of customizing log formatting and demonstrates how to apply the `filter_datum` function to log records. [Resource: [Python Logging Cookbook](https://docs.python.org/3/howto/logging-cookbook.html)]

### 2. Create Logger
Implement a `get_logger` function that returns a `logging.Logger` object:

- The logger should be named “user_data” and only log up to `logging.INFO` level.
- It should not propagate messages to other loggers.
- It should have a `StreamHandler` with `RedactingFormatter` as the formatter.

This task focuses on setting up a custom logger for handling user data. You'll learn how to configure loggers with specific settings and formatters, ensuring that sensitive information is properly redacted. [Resource: [Logging in Python](https://realpython.com/python-logging/)]

### 3. Connect to Secure Database
Implement a `get_db` function that returns a connector to the database (`mysql.connector.connection.MySQLConnection` object):

- Use the `os` module to obtain credentials from the environment.
- Use the `mysql-connector-python` module to connect to the MySQL database (`pip3 install mysql-connector-python`).

This task involves connecting to a secure database using environment variables for credential management. You'll learn how to retrieve sensitive information securely from environment variables and establish a connection to a MySQL database. [Resource: [Managing Database Credentials](https://cloud.google.com/solutions/managing-credentials)]

### 4. Encrypting Passwords
Implement a `hash_password` function that expects one string argument `password` and returns a salted, hashed password (a byte string). Use the `bcrypt` package to perform the hashing (with `hashpw`). This task demonstrates how to securely hash passwords using bcrypt, enhancing the security of user authentication in your application. [Resource: [Bcrypt Documentation](https://github.com/pyca/bcrypt/)]

### 5. Check Valid Password
Implement an `is_valid` function that expects two arguments (`hashed_password`: bytes type and `password`: string type) and returns a boolean. Use `bcrypt` to validate that the provided password matches the hashed password. This task focuses on password validation, ensuring that users can securely authenticate by comparing their input passwords with the hashed passwords stored in the database. [Resource: [Bcrypt Usage](https://auth0.com/blog/hashing-in-action-understanding-bcrypt/)]


