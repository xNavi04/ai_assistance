from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionSaveName(Action):

    def name(self) -> Text:
        return "action_save_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Extract the name entity
        name = tracker.get_slot("username")
        if not name:
            dispatcher.utter_message(text="Miło Cię poznać")
            return []

        dispatcher.utter_message(text=f"Miło Cię poznać, {name}!")
        return []

class ActionBye(Action):

    def name(self) -> Text:
        return "action_bye"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Extract the name entity
        name = tracker.get_slot("username")
        if not name:
            dispatcher.utter_message(text="Do widzenia i zapraszam ponownie!")
            return []

        dispatcher.utter_message(text=f"Do widzenia i zapraszam ponownie, {name}!")
        return []
