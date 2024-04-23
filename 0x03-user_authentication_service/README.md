# 0x03. User Authentication Service
## Back-end

In the industry, you should not implement your own authentication system and use a module or framework that does it for you (like in Python-Flask: Flask-User). Here, for the learning purpose, we will walk through each step of this mechanism to understand it by doing.

## Resources
Read or watch:
- [Flask documentation](https://flask.palletsprojects.com/en/2.0.x/)
- [Requests module](https://docs.python-requests.org/en/latest/)
- [HTTP status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
- How to declare API routes in a Flask app
- How to get and set cookies
- How to retrieve request form data
- How to return various HTTP status codes

## Setup
You will need to install bcrypt
```bash
pip3 install bcrypt

## Tasks
### 0. User model
- Create a SQLAlchemy model named User for a database table named users.
- Model attributes: id, email, hashed_password, session_id, reset_token.
- This model will represent user data in the database.

### 1. Create user
- Implement the `add_user` method in the DB class to add a user to the database.
  - Use SQLAlchemy to insert a new user record into the `users` table.
  - The method should accept two required string arguments: email and hashed_password.
  - Ensure that the email is unique in the database.

### 2. Find user
- Implement the `find_user_by` method in the DB class to find a user based on input arguments.
  - Use SQLAlchemy to query the `users` table based on the provided keyword arguments.
  - If no user is found, raise SQLAlchemy's NoResultFound exception.

### 3. Update user
- Implement the `update_user` method in the DB class to update user attributes.
  - Use the `find_user_by` method to locate the user to update.
  - Update the user's attributes based on the keyword arguments provided.
  - Commit the changes to the database.

### 4. Hash password
- Define a `_hash_password` method to hash a password using bcrypt.
  - Use the bcrypt library to generate a salted hash of the input password.
  - This method will ensure that passwords are securely stored in the database.

### 5. Register user
- Implement the `register_user` method in the Auth class to register a user.
  - Check if the user already exists in the database.
  - If the user does not exist, hash the password and add the user to the database.
  - Return the registered user object.

### 6. Basic Flask app
- Set up a basic Flask app with a single GET route ("/") returning a JSON payload.
  - Use Flask to create a simple API endpoint that returns a welcome message in JSON format.
  - This serves as the entry point for the authentication service.

### 7. Register user
- Implement a POST route ("/users") to register a user.
  - Parse form data from the request to extract email and password.
  - Use the `register_user` method from the Auth class to register the user.
  - Return appropriate JSON responses based on the registration result.

### 8. Credentials validation
- Implement the `valid_login` method in the Auth class to validate user credentials.
  - Check if the provided email and password match a user in the database.
  - Use bcrypt to verify the hashed password against the stored hash.

### 9. Generate UUIDs
- Implement a `_generate_uuid` function in the auth module to generate UUIDs.
  - Use the uuid module to generate a new UUID string.
  - UUIDs are used for generating session IDs and reset tokens.

### 10. Get session ID
- Implement the `create_session` method in the Auth class to create a session ID.
  - Find the user corresponding to the email provided.
  - Generate a new UUID and store it in the user's session_id field.
  - Return the session ID.

### 11. Log in
- Implement a POST route ("/sessions") to log in a user.
  - Parse form data from the request to extract email and password.
  - Validate the credentials using the `valid_login` method.
  - If the login is successful, create a session for the user and set a session ID cookie.
  - Return appropriate JSON responses based on the login result.

### 12. Find user by session ID
- Implement the `get_user_from_session_id` method in the Auth class to find a user by session ID.
  - Use the session ID from the request cookie to retrieve the corresponding user.
  - This method enables user authentication based on session IDs.

### 13. Destroy session
- Implement the `destroy_session` method in the Auth class to destroy a user session.
  - Set the user's session_id field to None.
  - This method logs out a user by invalidating their session ID.

### 14. Log out
- Implement a DELETE route ("/sessions") to log out a user.
  - Parse the session ID from the request cookie.
  - Destroy the session using the `destroy_session` method.
  - Return appropriate JSON responses based on the logout result.

### 15. User profile
- Implement a GET route ("/profile") to retrieve user profile information.
  - Use the session ID from the

