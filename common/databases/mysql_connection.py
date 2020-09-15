import mysql.connector

# from common.send_response_helper import send_abort
from common.send_response_helper import send_abort

MYSQL_HOST = 'localhost'
MYSQL_NAME = 'orderfood'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'Nguyenvanvu17150217'

mysql_connection_string = mysql.connector.connect(host=MYSQL_HOST, user=MYSQL_USER, passwd=MYSQL_PASSWORD,
                                                  database=MYSQL_NAME, auth_plugin='mysql_native_password')


# I have used 'host', 'username', 'password'
# mycursor = mysql_connection_string.cursor()
# mycursor.execute("SELECT * FROM User")
#
# myresult = mycursor.fetchall()
#
# # for db in mycursor:
# #     print(db)
#
# for x in myresult:
#   print(x)
#
# mysql_connection_string.close()

def get_mysql_connection():
    try:
        return mysql_connection_string
    except(Exception, mysql.Error) as error:
        message = f"get_mysql_connection {error}"
        return send_abort(code=400, message=message)


def execute_count_query(count_query) -> int:
    """
        Thực thi một câu lệnh count query -> trả về một số
    """
    connection = get_mysql_connection()
    cursor = connection.cursor()
    count = 0
    try:
        cursor.execute(count_query)
        rows = cursor.fetchall()
        cursor.close()
        connection.close()
        print('COUNT QUERY', rows[0][0])
        count = rows[0][0]
    except (Exception, mysql.Error) as error:
        print("execute_count_query error")
        connection.rollback()
        cursor.close()
        connection.close()
        print(error)

    return count


def execute_select_query(select_query : str) -> []:
    """
    Execute select query in POSTGRE
    :param select_query:
    :param connection: postgre connection
    :return: Mảng các giá trị dict hoặc []
    """
    connection = get_mysql_connection()
    cursor = connection.cursor()
    result = []
    try:
        cursor.execute(select_query)


    except(Exception, mysql.Error) as error:
        print("execute_select_query error", error)
        connection.rollback()
        cursor.close()
        connection.close()
        # send_abort(code=400, message="execute_select_query error")
    return result