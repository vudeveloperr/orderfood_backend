from config import db, ma
from sqlalchemy import Column, SmallInteger, String, Date, Integer, Text


class User(db.Model):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(15), unique=True)
    full_name = Column(String(50))
    image_url = Column(String(100))
    # security_level = Column(String(15))
    # tenant_id = Column(SmallInteger)
    address = Column(String(100))
    # start_working_date = Column(Date)
    # work_history = Column(Text)
    # tel = Column(String(50))
    mobile = Column(String(50))
    email = Column(String(50))
    created_date = Column(Date)
    password = Column(String(100))
    image_path = Column(String(200))
    # superior_id = Column(Integer)
    # role = Column(Integer)
    status = Column(SmallInteger)


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
        sqla_session = db.session
        # load_instance = True
