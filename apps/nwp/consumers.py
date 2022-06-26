import json
from channels.generic.websocket import WebsocketConsumer
from .utils import predict_next_word
import json, datetime


class NwpConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        self.send(text_data=json.dumps({
            'type': 'Success',
            'message': 'You are now connected'
        }))

    
    def receive(self,text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json.get('message')
        print(message)
        predicted_words = predict_next_word(message)

        self.send(text_data=json.dumps({
            'type':'chat',
            'message':predicted_words
        }))

    def disconnect(self):
        pass
