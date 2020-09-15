
from flask import jsonify, abort, make_response


def send_error(message="Error", code=400):
    return make_response(jsonify({"code": code, "message": message}), code)


def send_create_success(data=None, message="Created success", code=200, total=None):
    if total is None:
        return make_response(jsonify({"code": code, "message": message, "data": data}), 200)
    return make_response(jsonify({"code": code, "message": message, "data": data, "total": total}), 200)


def send_get_success(data=None, message="Get success", code=200, total=None):
    if total is None:
        return make_response(jsonify({"code": code, "message": message, "data": data}), 200)
    return make_response(jsonify({"code": code, "message": message, "data": data, "total": total}), 200)


def send_update_success(data=None, message="Update success", code=200, total=None):
    if total is None:
        return make_response(jsonify({"code": code, "message": message, "data": data}), 200)
    return make_response(jsonify({"code": code, "message": message, "data": data, "total": total}), 200)


def send_delete_success(data=None, message="Delete success", code=200, total=None):
    if total is None:
        return make_response(jsonify({"code": code, "message": message, "data": data}), 200)
    return make_response(jsonify({"code": code, "message": message, "data": data, "total": total}), 200)


def send_abort(code=400, message=None):
    abort(code, message)
