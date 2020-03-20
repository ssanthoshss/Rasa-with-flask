# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import re
from firebase import firebase

class ActionCluster(Action):

    def name(self) -> Text:
        return "action_cluster"

    def run(self, dispatcher,tracker,domain):
        Cluster = tracker.latest_message.get('text')
        Cluster = re.findall("(?<=Cluster:).+", Cluster)
        dispatcher.utter_message(text="Your Cluster is {}".format(Cluster[0]))
        return []

class ActionParking(Action):

    def name(self) -> Text:
        return "action_parking"

    def run(self, dispatcher,tracker,domain):
        global firebase
        UserName = tracker.latest_message.get('text')

        firebase = firebase.FirebaseApplication('https://parkinglotbot-djokap.firebaseio.com/', None)
        UserName = firebase.get('/Details', UserName)

        
        dispatcher.utter_message(text= "Currently you have {} parknig lot".format(UserName))
        return []