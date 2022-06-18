# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
from typing import Any, Text, Dict, List
import random

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, UserUtteranceReverted, AllSlotsReset 
import time 




class ActionGoodbye(Action):

    def name(self) -> Text:
        return "action_goodbye"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        messages = ["Goodbye.I am very glad that I could be of help.","Goodbye.I am so glad that I could be helpful."] 
        reply = random.choice(messages) 
          
        attachment = {
			"query_response": reply,
			"data":[],
			"type":"normal_message",
			"data_fetch_status": "success"
		}

        dispatcher.utter_message(attachment=attachment)

        return []  


class ActionGreet(Action):

    def name(self) -> Text:
        return "action_greetings_from_bot"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        messages = ["Hi! There I am your assistant.Feel free to bombard any queries.Let me know your name.","Hello how can I help you Can I know your name?SO that It would be easy for me to address you? ?","Hey? How you doing? What's your name? I am up for any queries you have.","How  what's your name and how can I help you please let me know.I am your assistant."] 
        reply = random.choice(messages)
         
        attachment = {
			"query_response": reply,
			"data":[],
			"type":"normal_message",
			"data_fetch_status": "success"}
        

        dispatcher.utter_message(attachment=attachment)

        return []  




class ActionAskBusinessInterest(Action):

    def name(self) -> Text:
        return "action_ask_bussiness_interest"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        prediction = tracker.latest_message
        try : 
            print(prediction)
            name = prediction["entities"][0]["value"]
        except :
            name = tracker.get_slot('user_name')
        
        try :  
            messages = [f"{name} Do you want to buy,sell or rent anything?",f"{name} What do you want to buy ?",f"{name} Please choose an option for buy,sell or rent",f"{name} What do  you want , buy ,sell or rent?",f" What do you like to do? buy,sell or rent something {name}?"]
            reply = random.choice(messages)   
            attachment = {
                "query_response": reply,
                "data":[],
                "type":"normal_message",
                "data_fetch_status": "success"
            }

            dispatcher.utter_message(attachment=attachment)

            return []
        
        except :
            messages = ["Do you want to buy,sell or rent anything?","What do you want to buy?","Please choose an option for buy,sell or rent","What do  you want , buy ,sell or rent?","What do you like to do? buy,sell or rent something?"]
            reply = random.choice(messages)   
            attachment = {
                "query_response": reply,
                "data":[],
                "type":"normal_message",
                "data_fetch_status": "success"
            }

            dispatcher.utter_message(attachment=attachment)

            return []


class ActionEOIForm(Action):

    def name(self) -> Text:
        return "action_EOI_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        messages = ['Would you mind filling out this EOI form?',"Please fill out this EOI form.This will help us to know more about you and your interest","Thankyou for reaching out .You can fill up this EOI form","Please fill out the EOI form."]
        form_details = [
            {"label":"Name","name":"name","view":"text","type":"text"},
            {"label":"Email","name":"email", "view":"text","type":"email"},
            {"label":"Phone Number","name":"phoneNo", "view":"text","type":"phone"},
            {"label":"Movement_Timeline","name":"moveTimeline", "view":"text","type":"text"}
        ]

        reply = random.choice(messages)   
        attachment = {
			"query_response": reply,
			"data":form_details,
			"type":"message_with_form",
			"data_fetch_status": "success"
		}

        dispatcher.utter_message(attachment=attachment)

        return []


class ActionAppraisalForm(Action):

    def name(self) -> Text:
        return "action_appraisal_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        messages = ['Would you mind filling out this EOI form?',"Please fill out this EOI form.This will help us to know more about you and your interest","Thankyou for reaching out .You can fill up this EOI form","Please fill out the EOI form."]
        form_details = [
            {"label":"Name","name":"name","view":"text","type":"text"},
            {"label":"Email","name":"email", "view":"text","type":"email"},
            {"label":"Item","name":"item", "view":"text","type":"text"},
            {"label":"Used_Years","name":"use_years", "view":"text","type":"number"}
        ]

        reply = random.choice(messages)   
        attachment = {
			"query_response": reply,
			"data":form_details,
			"type":"message_with_form",
			"data_fetch_status": "success"
		}

        dispatcher.utter_message(attachment=attachment)

        return []



class ActionSendListings(Action):

    def __init__(self):
        self.link_data = "https://www.google.com/"

    def name(self) -> Text:
        return "action_send_listings"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        messages = ["Click on the link to view available listings","These are the available listings","Here's the link of the listings"] 
        reply = random.choice(messages)
        reply = reply + self.link_data
        attachment = {
			"query_response": reply,
			"data":[],
			"type":"normal_message",
			"data_fetch_status": "success"}
        

        dispatcher.utter_message(attachment=attachment)

        return []   

class ActionBookTimeWithAgent(Action):        
    def name(self) -> Text:
        return "action_book_time_with_agent"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        messages = ["When do you want to book time with an agent?","When would you want to book time with the agent","At what time do you want to book time with the agent?"] 
        reply = random.choice(messages)
        reply = reply + self.link_data

        form_details = [
            {"label":"Time","time":"time","view":"text","type":"text"} 
        ]

        attachment = {
			"query_response": reply,
			"data":form_details,
			"type":"normal_message",
			"data_fetch_status": "success"}
        
        

        dispatcher.utter_message(attachment=attachment)

        return []    

class ActionBookTimeWithAgent(Action):        
    def name(self) -> Text:
        return "action_time_scheduled_agent"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        messages = ["Congratulations your time has been schedulded !!","Good luck !! Your time has been scheduleded with the client","Great you are now scheduled for the given time with the client."] 
        reply = random.choice(messages)
        

        attachment = {
			"query_response": reply,
			"data":[],
			"type":"normal_message",
			"data_fetch_status": "success"}
        
        

        dispatcher.utter_message(attachment=attachment)

        return []    

class ActionGoodToGo(Action):        
    def name(self) -> Text:
        return "action_good_to_go"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        messages = ["Thankyou for your time.Your request has been submitted !!","Good luck !! Thankyou for your valuable time your request is submitted","Great you are good to go.Thankyou for your valuable time."] 
        reply = random.choice(messages)
        

        attachment = {
			"query_response": reply,
			"data":[],
			"type":"normal_message",
			"data_fetch_status": "success"}
        
        

        dispatcher.utter_message(attachment=attachment)

        return []       

class ActionRequestCallback(Action):        
    def name(self) -> Text:
        return "action_request_callback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        messages = ["We will send you to the contact form of our office.Please fill in the required details.Thankyou","We are directing you to our contact page.Please fill out the necessary details in the form.","Redirecting to the contact page.Please fill in the form details."] 
        reply = random.choice(messages)
        form_details = [
            {"label":"Name","name":"name","view":"text","type":"text"},
            {"label":"Email","name":"email", "view":"text","type":"email"},
            {"label":"Item","name":"item", "view":"text","type":"text"},
            {"label":"Used_Years","name":"use_years", "view":"text","type":"number"}
        ]

        attachment = {
			"query_response": reply,
			"data":form_details,
			"type":"normal_message",
			"data_fetch_status": "success"}
        
        

        dispatcher.utter_message(attachment=attachment)

        return []               

class ActionOutOfScope(Action):        
    def name(self) -> Text:
        return "action_out_of_scope"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        messages = ["Sorry ! Would you mind asking relevant queries?","It would be great if you asked relevant queries?","Would you mind asking relevant queries?","I think the questions are getting out of scope.Would you mind talking relevant questions?"] 
        reply = random.choice(messages)
        

        attachment = {
			"query_response": reply,
			"data":[],
			"type":"normal_message",
			"data_fetch_status": "success"}
        
        

        dispatcher.utter_message(attachment=attachment)

        return []       
            
