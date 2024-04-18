#!/usr/bin/env python3
'''Module containing Authentication functionality'''

from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """ Class for managing API authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method to validate if endpoint requires authentication """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True

        l_path = len(path)
        if l_path == 0:
            return True

        slash_path = True if path[l_path - 1] == '/' else False

        tmp_path = path
        if not slash_path:
            tmp_path += '/'

        for exc in excluded_paths:
            l_exc = len(exc)
            if l_exc == 0:
                continue

            if exc[l_exc - 1] != '*':
                if tmp_path == exc:
                    return False
            else:
                if exc[:-1] == path[:l_exc - 1]:
                    return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Method to handle authorization header """
        if request is None:
            return None

        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('User'):
        """ Method to validate current user """
        return None

    def session_cookie(self, request=None) -> str:
        """ Retrieve the value of the session cookie from the request.

        Args:
            request: The Flask request object.

        Returns:
            str: The value of the session cookie if it exists, otherwise None.
        """
        if request is None:
            return None
        
        session_cookie_name = getenv("SESSION_NAME", "_my_session_id")
        return request.cookies.get(session_cookie_name)