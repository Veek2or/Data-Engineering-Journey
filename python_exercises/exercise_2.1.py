'''
2.1 Extract. Using requests, find which months are available, then download all street-level
crimes around Newcastle city centre (latitude 54.9783, longitude -1.6178) for the latest month.
Save the raw JSON untouched to data/raw/ with the month in the filename.
'''
import os
import requests

# Step 1: find the latest available month
dates_url = "https://data.police.uk/api/crimes-street-dates"
response = requests.get(dates_url)
response.raise_for_status()  # stop if the request failed

months = response.json()
dates_only = [x["date"] for x in months]
most_recent_month = max(dates_only)  # "YYYY-MM" strings sort correctly as text

# Step 2: download crimes for that month
crimes_url = "https://data.police.uk/api/crimes-street/all-crime"
crime_params = {
    "lat": 54.9783,
    "lng": -1.6178,
    "date": most_recent_month,
}

crime_response = requests.get(crimes_url, params=crime_params)
crime_response.raise_for_status()

# Step 3: save the raw JSON
os.makedirs("data/raw", exist_ok=True)  # create folder if missing
file_name = f"data/raw/crimes_{most_recent_month}.json"

with open(file_name, "w", encoding="utf-8") as f:
    f.write(crime_response.text)  # .text keeps it exactly as the server sent it

print(f"Saved {len(crime_response.json())} crimes to {file_name}")