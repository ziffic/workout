import requests
import connect

NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercise you did: ")

params = {
    "query": exercise_text,
    "gender": connect.GENDER,
    "weight_kg": connect.WEIGHT_KG,
    "height_cm": connect.HEIGHT_CM,
    "age": connect.AGE
}

response = requests.post(url=NUTRITIONIX_ENDPOINT, json=params, headers=connect.headers)
results = response.json()
print(results)