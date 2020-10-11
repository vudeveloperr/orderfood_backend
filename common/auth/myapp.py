from flask import Flask, request, g, jsonify
# from customer import middleware
from customer import customer
from sign import sign
from flask_cors import CORS
app = Flask('DemoApp')
import ast
# calling our middleware
CORS(app, resources={r"/api/*": {"origins": "*"}})  # config cors

@app.route('/', methods=['GET', 'POST'])
@customer
def hello():
    return g.data

@app.route('/sign-in', methods=['POST'])
def sign_in():
    data = request.data
    dict_str = data.decode("UTF-8")
    mydata = ast.literal_eval(dict_str)
    print(mydata)
    username = mydata['username']
    password = mydata['password']
    username1 = "meoyeu123"
    password1 = "meoyeu123"
    if(username == username1 and password == password1):
        token =sign() #Thong tin user trong db
        return jsonify({"data":{"token":token},"code":0, "message":"Thanh cong"})
    else: 
        return jsonify({"code":1, "message":"Sai tai khoan hoac mat khau"})
if __name__ == "__main__":
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.run('0.0.0.0', '5000', debug=True)