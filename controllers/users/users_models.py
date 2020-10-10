from config import ma
from sqlalchemy import Column, SmallInteger, String, Date, Integer, Text, BigInteger
from database import db


class User(db.Model):
    __tablename__ = "User"
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(15), unique=True)
    full_name = Column(String(50))
    image_url = Column(String(255))
    address = Column(String(100))
    mobile = Column(String(50))
    email = Column(String(50))
    created_date = Column(BigInteger),
    updated_date = Column(BigInteger),
    password = Column(String(100))
    image_path = Column(String(200))
    status = Column(SmallInteger)


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
        sqla_session = db.session
        # load_instance = True
