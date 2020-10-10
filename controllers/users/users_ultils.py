from sqlalchemy.sql import text
from sqlalchemy import or_

from common.databases import mysql_helper as mysql
from common.http_code import HTTP_404_NOT_FOUND
from common.send_response_helper import send_abort
from database import db
from controllers.users.users_models import UserSchema, User


def select_all_user(page_size: int, page_number: int) -> (list, int):
    """
    get all user pagination
    :param page_size:
    :param page_number:
    :return:
    """
    select_query = "select * from User where status=1"
    count_query = "select count(*) from User where status=1"
    data = mysql.execute_select_query_and_paginate(
        select_query=select_query,
        page_size=page_size,
        page_number=page_number)
    total = mysql.execute_count_query(count_query)
    return data, total


def create_new_user(user) -> dict:
    """

    :param user:
    :return:
    """

    new_user = User(**user)

    print(new_user)
    db.session.add(new_user)
    db.session.commit()
    user_dict = UserSchema().dump(new_user, many=False)
    return user_dict


def select_user_by_id(user_id) -> dict:
    """

    :param user_id:
    :return:
    """
    user_schema = UserSchema()
    user = User.query.filter_by(user_id=user_id, static=1).one_or_none()
    if user is None:
        return send_abort(message=f"user with user_id: {user_id} not exist", code=HTTP_404_NOT_FOUND)
    data = user_schema.dump(user)
    return data


def check_user_exists(user_name: str = None, user_id: str = None) -> bool:
    """

    :param user_name:
    :param user_id:
    :return:
    """
    user = User.query.filter(or_(User.user_name == user_name, User.user_id == user_id)).first()
    if user:
        return True
    else:
        return False


# minh co the viet test tuwng file o day
# co ve ko chay roi
# print("====")
# user_dict = {
#     "user_name": "user_name",
#     "full_name": "full_name",
#     "image_url": "image_url",
#     "address": "address",
#     "mobile": "mobile",
#     "email": "email",
#     "created_date": 'created_date',
#     "password": "password",
#     "image_path": "image_path",
#     "status": 1
# }
# new_user = User(**user_dict)
# print(new_user)
# result = create_new_user(user_dict)
# print("result", result)