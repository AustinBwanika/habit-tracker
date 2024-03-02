import requests
import datetime
import os
TOKEN = os.environ["TOKEN"]
USERNAME = "bwanika"
GRAPHID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# below created a new user profile on pixela
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# The code belows creates the graph

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
date = datetime.date.today()
today = datetime.date(year=2023, month=7, day=10)

date = date.strftime("%Y%m%d")
quantity = "4.5"


post_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": quantity
}

# response = requests.post(url=post_endpoint, json=post_config, headers=headers)
# print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": quantity
}

response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today.strftime('%Y%m%d')}"
# response = requests.delete(url=delete_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)