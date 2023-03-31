import requests
import connect

NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise = input("Tell me which exercise you did: ")

params = {
    "query": exercise
}

# params = {
#     "query": "ran 3 miles",
#     "gender": "female",
#     "weight_kg": 72.5,
#     "height_cm": 167.64,
#     "age": 30
# }

response = requests.post(url=NUTRITIONIX_ENDPOINT, json=params, headers=connect.headers)
response.raise_for_status()
print(response.json())
