from flask import Flask, request, g, jsonify
# from customer import middleware
from customer import customer
from sign import sign
app = Flask('DemoApp')

# calling our middleware


@app.route('/', methods=['GET', 'POST'])
@customer
def hello():
    return g.data

@app.route('/sign-in', methods=['POST'])
def sign_up():
    username = request.form['username']
    password = request.form['password']
    username1 = "meoyeu123"
    password1 = "meoyeu123"
    if(username == username1 and password == password1):
        token =sign() #Thong tin user trong db
        return jsonify({"data":{"token":token},"code":0, "message":"Thanh cong"})
    else: 
        return jsonify({"code":1, "message":"Sai tai khoan hoac mat khau"})
if __name__ == "__main__":
    app.run('127.0.0.1', '5000', debug=True)