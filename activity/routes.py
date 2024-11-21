from flask import render_template, jsonify, request, send_from_directory
import requests
from log_activity import append_wrong_answer
from training_data_activity import TrainingDataActivity
import datetime
from shudtown import shutdown


def init_routes(app, state):
    training_data_activity = TrainingDataActivity(training_data_path=state['TRAINING_DATA_PATH'])
    @app.route('/')
    def index():
        template = "index.html"
        return render_template(template)
    @app.route('/webhook', methods=['POST'])
    def webhook():
        feedback = training_data_activity.get_user_feedback()
        if feedback == 0:
            state['user_message'] = request.json['message']
        if state['user_message'].lower() == "koniec":
            shutdown(state['all_predict'], state['correct_pred'])
            return jsonify({'response': 'Aplikacja została zakończona.'})
        rasa_response = requests.post(state['RASA_API_URL'], json={'message': state['user_message']})
        rasa_response_json = rasa_response.json()
        if feedback != 0:
            state['all_predict'] += 1
            if feedback == 1:
                state['correct_pred'] += 1
                intent = training_data_activity.get_intent_from_nlu(state['bot_response'][0]["text"])
                training_data_activity.add_example_to_intent(intent, state['user_message'])
            else:
                current = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                append_wrong_answer(current, state['user_message'], state['bot_response'])
        if 'custom' in rasa_response_json[0]:
            bot_response = rasa_response_json[0]['custom']['blocks']
        else:
            bot_response = rasa_response_json
        if feedback == 0:
            state["bot_response"] = bot_response
        return jsonify(bot_response)
    @app.route('/static/<path:filename>')
    def serve_image(filename):
        return send_from_directory('static', filename)