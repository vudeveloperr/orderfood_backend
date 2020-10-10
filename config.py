# Import from third party
import connexion
import hiyapyco

# from flask_sqlalchemy import SQLAlchemy
from database import db, ma
# from flask_cors import CORS
from common.databases.mysql_connection import mysql_connection_string

options = {"swagger_ui": True}  # turn off ui
connex_app = connexion.FlaskApp(
    __name__,
    specification_dir='swagger-doc/',
    options=options)
flask_app = connex_app.app

# CONIG UPLOAD FOLDER
UPLOAD_FOLDER = './static/'  # relative path


flask_app.config['SQLALCHEMY_DATABASE_URI'] = mysql_connection_string
flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# #config turn on sql query on logging
flask_app.config["SQLALCHEMY_ECHO"] = False
flask_app.config["CORS_HEADERS"] = 'Content-Type'
flask_app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
flask_app.config[
    'SECRET_KEY'] = "QdjqxOEiclZ5OIM26yBxd6K5N4TgsW3UYNG0uc5hvn0IGrbgTeSW52wld0svkUjABJJ5rUL5VBSMGOpHpswhUqjJhaRR7W2MKyC1E4bvs8dE0Ft1dRlckaacpWZ9oBIuXPLYUZVeqpOMwR3dWr4SLkwt142hsSZxwR3dWr4SLkwt142hsSZx4bN8mIifIh7Uh0tTrhMN "

# ======================================================#
db.init_app(flask_app) # db tach ra file rieng nhe
ma.init_app(flask_app)

# CORS(flask_app, resources={r"/api/*": {"origins": "*"}})

swagger_file = hiyapyco.load(
    [
        'swagger_files/main.yaml',
        'controllers/users/users.yaml',
        'controllers/products/products.yaml'
    ],
    method=hiyapyco.METHOD_MERGE
)
swagger_file_dumped = hiyapyco.dump(swagger_file)
