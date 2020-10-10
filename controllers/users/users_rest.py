from config import db
from controllers.users.users_models import User, UserSchema
from .users_ultils import select_all_user, select_user_by_id
from . import users_ultils as utils
from common.send_response_helper import send_get_success, send_create_success, send_error, send_update_success, \
    send_delete_success
# from ..auth.auth_rest import get_user_info_from_token, lazy_hashing
# from datetime import datetime
# from common.http_code import HTTP_403_FORBIDDEN, HTTP_404_NOT_FOUND, HTTP_200_OK, HTTP_406_NOT_ACCEPTABLE

from controllers.users.users_ultils import select_all_user


def api_get_all_user(page_size: int = 20, page_number: int = 1):
    """
        get all user pagination
    """
    data, total = select_all_user(page_size, page_number)
    return send_get_success(data=data, total=total)


def api_post_user(
        user_name: str = None,
        full_name: str = None,
        image_url: str = None,
        address: str = None,
        mobile: str = None,
        email: str = None,
        created_date=None,
        password: str = None,
        image_path: str = None):
    user_dict = {
        "user_name": user_name,
        "full_name": full_name,
        "image_url": image_url,
        "address": address,
        "mobile": mobile,
        "email": email,
        "created_date": created_date,
        "password": password,
        "image_path": image_path,
        "status": 1
    }
    print(user_dict)
    data = utils.create_new_user(user=user_dict)
    print(data)
    return 'data'


def get_user_by_id(user_id: int):
    data = select_user_by_id(user_id)
    return send_get_success(data)


def api_put_user(user_id: int):
    return 'hello'


def api_delete_user(user_id: int):
    return 'hello'
