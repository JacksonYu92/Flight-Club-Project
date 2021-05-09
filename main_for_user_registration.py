import requests
import os


sheety_endpoint = os.environ['SHEETY_ENDPOINT']
sheety_auth = os.environ['SHEETY_AUTH']

print("Welcome to Jackson's Flight Club.")
print("We find the best flight deals and email you.")
f_name = input("What is your first name?\n")
l_name = input("What is your last name?\n")
email = input("What is your email?\n")
email_confirmed = input("Type your email again.\n")

headers = {
    "Authorization": sheety_auth,
}

if email == email_confirmed:
    parameters = {
        "user": {
            "firstName": f_name,
            "lastName": l_name,
            "email": email,
        }
    }

    response = requests.post(url=sheety_endpoint, json=parameters, headers=headers)
    print(response.text)