import pyrebase
from config import config

firebase = pyrebase.initialize_app(config)
firebase_db = firebase.database()
print(firebase_db)

my_stream = firebase_db.child("/v0/maxitem").stream(new_post_handler,
                                           stream_id="new_posts")
