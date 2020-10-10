from flask import jsonify, abort, make_response
from jwt import JWT
instance = JWT()

def verify(token):
    verifying_key = "afkawfl1421ADwawd!%@qdawdajlkwdjaldjzlcjwidj"
    message_received = instance.decode(token, verifying_key, do_time_check=True)
    return message_received
