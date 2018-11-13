from flask import current_app
import requests


_BASEURL_ = "https://hacker-news.firebaseio.com/v0/item/"


class DataInserts(object):
    def create_document(self, id):
        document = dict(title="Hello", content="Hello, world!")
        docs = current_app.mongo.db.docs
        doc_id = docs.insert_one(document).inserted_id
        return doc_id

    def save_max_item_to_db(self, id):
        headers={"Content-Type": "application/x-www-form-urlencoded"}
        print(_BASEURL_ + str(id) + ".json")
        response = requests.get(_BASEURL_ + str(id) + ".json", headers=headers)
        print(response.content)
        if response.json()["type"] == "job":
            jobs = current_app.mongo.db.jobs
            job_id = jobs.insert_one(response.json()).inserted_id
            self.get_item_from_db(job_id)
            return job_id

    def get_item_from_db(self, id):
        job = current_app.mongo.db.jobs.find({"id": job_id})
        print(job)
