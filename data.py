import requests

# Fetch 10 T/F Questions from Opentdb
response = requests.get("https://opentdb.com/api.php", params={
    "amount": 10,
    "type": "boolean"
})
response.raise_for_status()

# Store the questions in question_data
question_data = response.json()["results"]
