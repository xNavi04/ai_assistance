import yaml
import re
from data import utter_intent, answer_utter
from flask import request

class TrainingDataActivity:
    def __init__(self, training_data_path):
        self.training_data_path = training_data_path

    def load_training_data(self):
        with open(self.training_data_path, 'r', encoding='utf-8') as file:
            return yaml.safe_load(file)

    def save_training_data(self, question, intent):
        with open(self.training_data_path, 'r', encoding='utf-8') as file:
            lines = [line.rstrip('\n') for line in file if line.strip()]
        with open(self.training_data_path, 'w', encoding='utf-8') as file2:
            i = 0
            for line in lines:
                file2.write(line + "\n")
                if i == 50:
                    print(line)
                    i = 0
                    file2.write(question + "\n")
                if intent == line:
                    i = 50


    def add_example_to_intent(self, intent, example):
        data = self.load_training_data()
        for intent_data in data['nlu']:
            if intent_data['intent'] == intent:
                question = example
                sentences = re.split(r'\s*-\s*', intent_data['examples'])
                sentences = [sentance.rstrip() for sentance in sentences]
                sentences = [sentence for sentence in sentences if sentence]
                for x in sentences:
                    if x.lower() == question.lower():
                        return 0
        check_intent = "- intent: " + intent
        add_question = "    - " + example

        self.save_training_data(add_question, check_intent)
        return 1

    @staticmethod
    def get_intent_from_nlu(answer):
        utter = answer_utter[answer]
        print(utter)
        return utter_intent[utter]

    @staticmethod
    def get_user_feedback():
        feedback = request.json.get('feedback', '').lower()
        if feedback == "yes":
            return 1
        if feedback == "no":
            return -1
        else:
            return 0