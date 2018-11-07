from flask import current_app


class DataInserts(object):
    def create_document(self, id):
        document = dict(title="Hello", content="Hello, world!")
        docs = current_app.mongo.db.docs
        doc_id = docs.insert_one(document).inserted_id
        return doc_id
