import requests
import connect

NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = f"https://api.sheety.co/{connect.SHEETY_USER_NAME}/" \
                  f"{connect.SHEETY_PROJ_NAME}/{connect.SHEETY_SHEET_NAME}"
exercise_text = input("Tell me which exercise you did: ")

params = {
    "query": exercise_text,
    "gender": connect.GENDER,
    "weight_kg": connect.WEIGHT_KG,
    "height_cm": connect.HEIGHT_CM,
    "age": connect.AGE
}

# response = requests.post(url=NUTRITIONIX_ENDPOINT, json=params, headers=connect.headers)
# results = response.json()
# print(results)

sheety_params = {
    "workout": {
        "date": "31/03/2023",
        "time": "12:30:00",
        "exercise": "Walking",
        "duration": 15,
        "calories": 255
    }
}

sheety_response = requests.post(url=SHEETY_ENDPOINT, json=sheety_params, headers=connect.sheety_headers)
# sheety_response = requests.get(url=SHEETY_ENDPOINT, headers=connect.sheety_headers)
sheety_results = sheety_response.json()
print(sheety_results)
