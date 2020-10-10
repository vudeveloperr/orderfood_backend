import config
from flask import redirect
from flask_cors import CORS

app = config.connex_app

# combine
app.add_api(config.swagger_file) # ?
CORS(app.app, resources={r"/api/*": {"origins": "*"}})  # config cors


@app.route('/')
def home():
    return redirect("api/ui", code=302)

from decimal import *
getcontext().prec = 2

if __name__ == '__main__':
    app.run(port=8181, debug=True)
