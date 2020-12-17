import requests

API_URL = "https://opentdb.com/api.php"
API_PARAMS = {
    "amount": 10,
    "type": "boolean"
}
response = requests.get(API_URL, params=API_PARAMS)
response.raise_for_status()
data = response.json()
question_data = data["results"]
