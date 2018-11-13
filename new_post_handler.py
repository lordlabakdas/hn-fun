import pyrebase
from config import config
from core.data_inserts import DataInserts
import requests
from pymongo import MongoClient

firebase = pyrebase.initialize_app(config)
firebase_db = firebase.database()
print(firebase_db)

client = MongoClient('localhost', 27017)
db = client["hn-fun"]
jobs = db.jobs
id = jobs.insert_one({"name": "Sahana"}).inserted_id
print(id)
_BASEURL_ = "https://hacker-news.firebaseio.com/v0/item/"
session = requests.session()

local_cache = []

def save_job_posts_to_db(id_list):
    global local_cache
    ids = list(set(id_list).symmetric_difference(set(local_cache)))
    headers = {"Content-Type": "application/json"}
    for id in ids:
        response = requests.get(_BASEURL_ + str(id) + ".json", headers=headers)
        if response.json()["type"] == "job":
            print(response.content, response.url, response.headers, response.status_code)
            job_id = jobs.insert_one(response.json()).inserted_id
            print(job_id)
    local_cache = id_list
    return "Ok"


def new_post_handler(message):
    save_job_posts_to_db(message["data"])


my_stream = firebase_db.child("/v0/jobstories").stream(new_post_handler,
                                                    stream_id="new_posts")
