# Project 0x02: Session Authentication

## Background Context

In this project, you will implement Session Authentication without using any additional modules. While in practice it's discouraged to build your own authentication system and recommended to use established frameworks, this project aims to provide a hands-on understanding of the authentication mechanism.

### Resources

Read or watch:

- [REST API Authentication Mechanisms - Only the session auth part](https://restfulapi.net/session-authentication-101/): This resource provides an overview of session authentication and its role in RESTful APIs.
- [HTTP Cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies): Understand the fundamentals of HTTP cookies and their significance in web applications, including session management.
- [Flask](https://flask.palletsprojects.com/en/2.0.x/): Flask is a lightweight WSGI web application framework in Python. You'll use Flask to implement session authentication.
- [Flask Cookie](https://flask.palletsprojects.com/en/2.0.x/quickstart/#cookies): Learn how to work with cookies in Flask, which is essential for session management.

Task 0: Et moi et moi et moi!

Objective: Copy all work from the previous Basic authentication project into this new folder. Additionally, add a new endpoint (GET /users/me) to retrieve the authenticated User object.

    Steps:
        Copy the models and api folders from the previous project (0x06. Basic authentication).
        Ensure all mandatory tasks from the previous project are completed.
        Update @app.before_request in api/v1/app.py to assign the result of auth.current_user(request) to request.current_user.
        Update the method for the route GET /api/v1/users/<user_id> in api/v1/views/users.py to handle the case where <user_id> is equal to "me" and request.current_user is not None.

Task 1: Empty session

Objective: Create a class SessionAuth that inherits from Auth. This class will serve as the foundation for implementing session authentication.

    Steps:
        Define a new class SessionAuth inheriting from Auth.
        Implement the class without any methods or attributes initially.

Task 2: Create a session

Objective: Implement a method create_session(self, user_id: str = None) -> str in the SessionAuth class to generate a Session ID for a given User ID.

    Steps:
        Add a method create_session to the SessionAuth class.
        Validate the input user_id parameter.
        Generate a Session ID using a UUID.
        Store the Session ID in a dictionary with the corresponding User ID.
        Return the generated Session ID.

Task 3: User ID for Session ID

Objective: Add a method user_id_for_session_id(self, session_id: str = None) -> str to the SessionAuth class, which retrieves the User ID associated with a given Session ID.

    Steps:
        Add a method user_id_for_session_id to the SessionAuth class.
        Validate the input session_id parameter.
        Retrieve the User ID from the stored dictionary using the Session ID.
        Return the corresponding User ID.

Task 4: Session cookie

Objective: Implement a method session_cookie(self, request=None) in api/v1/auth/auth.py to extract the session cookie value from a request.

    Steps:
        Add a method session_cookie to the Auth class in api/v1/auth/auth.py.
        Validate the input request parameter.
        Extract the session cookie value from the request cookies.
        Return the session cookie value.

Task 5: Before request

Objective: Update the @app.before_request method in api/v1/app.py to handle session authentication, ensuring that unauthorized requests are rejected.

    Steps:
        Update the @app.before_request method in api/v1/app.py.
        Exclude the URL path /api/v1/auth_session/login/ from authentication checks.
        Check if the request contains both an authorization header and a session cookie.
        If not, abort the request with status code 401.

Task 6: Use Session ID for identifying a User

Objective: Implement a method current_user(self, request=None) in the SessionAuth class to retrieve the authenticated User instance based on the session ID.

    Steps:
        Add a method current_user to the SessionAuth class.
        Retrieve the session ID from the request cookie.
        Use the session ID to fetch the corresponding User instance.
        Return the authenticated User instance.

Task 7: New view for Session Authentication

Objective: Create a new Flask view to handle session authentication routes, including user login and session creation.

    Steps:
        Create a new Flask view for session authentication routes.
        Define a route POST /auth_session/login to handle user login.
        Retrieve email and password parameters from the request form.
        Validate the email and password.
        Create a session for the authenticated user and set the session cookie.
        Return the authenticated User instance in JSON format.

Task 8: Logout

Objective: Implement a method destroy_session(self, request=None) in the SessionAuth class to handle user logout by destroying the session.

    Steps:
        Add a method destroy_session to the SessionAuth class.
        Retrieve the session ID from the request cookie.
        Delete the session ID entry from the stored dictionary.
        Return True if the session was successfully destroyed, False otherwise.

Task 9: Expiration?

Objective: Add an expiration mechanism to session IDs to enhance security and prevent session hijacking.

    Steps:
        Modify the SessionAuth class to include an expiration duration for session IDs.
        Implement logic to check the expiration of session IDs.
        Expire session IDs if they exceed the specified duration.

Task 10: Sessions in database

Objective: Implement a database-backed session authentication system using a new model UserSession and an authentication class SessionDBAuth.

    Steps:
        Create a new model UserSession to represent session data in the database.
        Implement methods in SessionDBAuth to interact with the database for session management.
        Update api/v1/app.py to use SessionDBAuth for authentication if specified in the environment variable AUTH_TYPE.
