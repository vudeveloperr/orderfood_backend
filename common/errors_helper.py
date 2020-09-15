from flask import abort

from common.http_code import HTTP_500_INTERNAL_SERVER_ERROR, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED, \
    HTTP_403_FORBIDDEN


def send_internal_server_error(code=None, message=None):
    message = "something went wrong"
    status = HTTP_500_INTERNAL_SERVER_ERROR
    return abort(status, message)


def send_schema_validation_error(code=None, message=None):
    message = "request is missing required fields"
    status = HTTP_400_BAD_REQUEST
    return abort(status, message)


def send_object_already_exists_error(code=None, message=None):
    message = "object already exists"
    status = HTTP_400_BAD_REQUEST
    abort(status, message)


def send_object_not_exists_error(code=None, message=None):
    message = "object not exists"
    status = HTTP_400_BAD_REQUEST
    abort(400, message)


def send_adding_object_error(code=None, message=None):
    message = "adding object added by other is forbidden"
    status = HTTP_403_FORBIDDEN
    abort(status, message)


def send_updating_object_error(code=None, message=None):
    message = "updating object added by other is forbidden"
    status = HTTP_403_FORBIDDEN
    abort(status, message)


def send_deleting_object_error(code=None, message=None):
    message = "deleting object added by other is forbidden"
    status = HTTP_403_FORBIDDEN
    abort(status, message)


def send_unauthorized_error(code=None, message=None):
    message = "invalid username or password"
    status = HTTP_401_UNAUTHORIZED
    abort(status, message)


def send_integrity_error(code=None, message=None):
    message = "error when adding"
    status = HTTP_400_BAD_REQUEST
    abort(status, message)
