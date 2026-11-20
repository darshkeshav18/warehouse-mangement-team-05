
import requests
from requests.packages import package

URL = "http://127.0.0.1:8001"

# checks our register
# user_creds = {"username": "potato", "password": "carrot123", "user_type": "customer"}
# response = requests.post(url=URL+"/signup", json=user_creds)
# print(response.status_code) # prints only the status code 
# print(response.json()) # prints the message that we see in swagger

# checks login
user_creds = {"username": "ratatouille", "password": "remytherat"}
response = requests.post(url=URL+"/login", json=user_creds)
response_json = response.json()
access_token = response_json["access_token"]
refresh_token = response_json["refresh_token"]


# checks search package
header = {"token": access_token}
# response = requests.get(url=URL+"/packages", headers=header)
# print(response.json())

# checks package id
# response = requests.get(url=URL+"/packages/1", headers=header)
# print(response.json())


# checks register package
# package = {
#   "name": "rat food",
#   "destination": "sams's house",
#   "weight": 10
# }
# response = requests.post(url=URL+"/packages",json=package, headers=header)
# print(response.json())

# checks update package
# package_update = {
#   "name": "human food",
#   "destination": "sam's house",
#   "weight": 25
# }

# response = requests.patch(url=URL+"/packages/2",json=package_update, headers=header)
# print(response.json())


# checks delete package
response = requests.delete(url=URL+"/packages/2", headers=header)
print(response.json())