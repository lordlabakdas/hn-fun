from flask import Flask
from controller.hn_apis import hn_apis
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)
app.mongo = mongo

print("hi")
app.register_blueprint(hn_apis)

@app.route("/")
def hello_jobs():
    return "Welcome to Hacker News job insights"

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5000)
