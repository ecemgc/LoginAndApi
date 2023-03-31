from rest_framework import status
from rest_framework.exceptions import APIException


class BadRequestException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST

    def __init__(self, msg):
        APIException.__init__(self, msg)
        self.status_code = status.HTTP_400_BAD_REQUEST
        self.message = msg


class UnAuthorizedException(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED

    def __init__(self, msg):
        APIException.__init__(self, msg)
        self.status_code = status.HTTP_401_UNAUTHORIZED
        self.message = msg

class PermissionDeniedException(APIException):
    status_code = status.HTTP_403_FORBIDDEN

    def __init__(self, msg):
        APIException.__init__(self, msg)
        self.status_code = status.HTTP_403_FORBIDDEN
        self.message = msg


class NotFoundException(APIException):
    status_code = status.HTTP_404_NOT_FOUND

    def __init__(self, msg):
        APIException.__init__(self, msg)
        self.status_code = status.HTTP_404_NOT_FOUND
        self.message = msg


class InternalServerException(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

    def __init__(self, msg):
        APIException.__init__(self, msg)
        self.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        self.message = msg