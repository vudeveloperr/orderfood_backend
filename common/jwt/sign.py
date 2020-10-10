from flask import abort
from jwt import JWT 
instand = JWT()
from jwt.utils import get_int_from_datetime
from datetime import datetime, timedelta, timezone
 def sign(message):
     message={
    "userId":1,
    "name":'admin',
    "phone":'0356798938',
    'iat': get_int_from_datetime(datetime.now(timezone.utc)),
    'exp': get_int_from_datetime(
        datetime.now(timezone.utc) + timedelta(hours=1)),
    }
    signing_key = "afkawfl1421ADwawd!%@qdawdajlkwdjaldjzlcjwidj"
     compact_jws = instance.encode(message, signing_key, alg='RS256')
     return token