import requests

url = "http://127.0.0.1:5000/predict"

# Data payload to send for prediction
data = {
    "sleep_hours": 7,
    "screen_time": 5,
    "physical_activity": 30,
    "journal_freq": 2,
    "previous_mood": 6
}

try:
    response = requests.post(url, json=data)

    if response.status_code == 200:
        print("✅ Prediction successful!")
        print("Result:", response.json())
    else:
        print("❌ Failed with status code:", response.status_code)
        print(response.text)

except Exception as e:
    print("❌ Error occurred while sending request:", str(e))