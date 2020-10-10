import mysql.connector

# from common.send_response_helper import send_abort

MYSQL_HOST = 'localhost'
MYSQL_NAME = 'orderfood'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'laduc123'

# mysql_connection_string = mysql.connector.connect(host=MYSQL_HOST, user=MYSQL_USER, passwd=MYSQL_PASSWORD,
# database=MYSQL_NAME, auth_plugin='mysql_native_password')

mysql_connection_string = "mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}".format(
    DB_USER=MYSQL_USER,
    DB_PASS=MYSQL_PASSWORD,
    DB_ADDR=MYSQL_HOST,
    DB_NAME=MYSQL_NAME)

def get_mysql_connection():
    try:
        connection = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            passwd=MYSQL_PASSWORD,
            database=MYSQL_NAME,
            auth_plugin='mysql_native_password')
        return connection
    except Exception as error:
        message = f"get_mysql_connection {error}"
        return message
