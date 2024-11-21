from flask import Flask
import os

endpoint_secret = "kdsjf98usddvbkjlwesadvkjadsd7sdv3evjk3evjn3lekvjn"

def create_app():
    app = Flask(__name__)

    state = {
        'all_predict': 0,
        "ll_predict": 0,
        'correct_pred': 0,
        'bot_response': [],
        'user_message': "",
        'TRAINING_DATA_PATH': "data/nlu.yml",
        'RASA_API_URL': "http://0.0.0.0:5005/webhooks/rest/webhook"
    }

    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", endpoint_secret)

    return app, state