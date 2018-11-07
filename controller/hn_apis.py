from flask import Blueprint, request, jsonify
from core.data_inserts import DataInserts

hn_apis = Blueprint("hn_apis", __name__)


@hn_apis.route("/save-post-to-db", methods=["POST"])
def save_post_to_db():
    id = request.json["id"]
    print(id)
    data_inserts_obj = DataInserts()
    doc_id = data_inserts_obj.create_document(id)
    print(doc_id)
    return jsonify({"id": str(doc_id)})
