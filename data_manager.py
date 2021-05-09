import os
import requests
from pprint import pprint

token = os.environ["SHEETY_TOKEN"]
endpoint = os.environ["SHEETY_ENDPOINTS"]
user_endpoint = os.environ["SHEETY_USER_ENDPOINT"]

headers = {
    "Authorization": token,
}

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheet_data = {}

    def get_data(self):
        response = requests.get(url=endpoint, headers=headers)
        data = response.json()
        self.sheet_data = data["prices"]
        return self.sheet_data

    def update_data(self):
        for city in self.sheet_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"],
                }
            }
            response = requests.put(url=f"{endpoint}/{city['id']}", json=new_data, headers=headers)
            print(response.text)

    def get_emails(self):
        response = requests.get(url=user_endpoint, headers=headers)
        data = response.json()
        self.email_data = data["users"]
        return self.email_data

