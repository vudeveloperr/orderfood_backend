from config import db
from controllers.users.users_models import User, UserSchema
# from .users_utils import select_all_user, select_subordinate_by_user_id, select_user_by_id
# from . import users_utils as utils
from common.send_response_helper import send_get_success, send_create_success, send_error, send_update_success, \
    send_delete_success
# from ..auth.auth_rest import get_user_info_from_token, lazy_hashing
from datetime import datetime
from common.http_code import HTTP_403_FORBIDDEN, HTTP_404_NOT_FOUND, HTTP_200_OK, HTTP_406_NOT_ACCEPTABLE


# from ..resource import resource_utils
# from ..resource.resource_utils import ResourceUtilsCore


def api_get_all_user(page_size: int = 20, page_number: int = 1):
    """
        get all user pagination
        """
    select_query = "select * from users where status=1"
    count_query = "select count(*) from users where status=1"
    # data = pg.execute_select_query_and_paginate(
    #     select_query=select_query,
    #     page_size=page_size,
    #     page_number=page_number)
    # total = pg.execute_count_query(count_query)
    # return data, total
    return 'hello'


def api_post_user():
    return 'hello'


def get_user_by_id():
    return 'hello'


def api_put_user():
    return 'hello'


def api_delete_user():
    return 'hello'
