from flask import Flask
from controller.hn_apis import hn_apis

app = Flask(__name__)

app.register_blueprint(hn_apis)

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5000)
