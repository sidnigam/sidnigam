import requests
from datetime import datetime

MY_LAT = 42.395760
MY_LNG = -70.993150

response=requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

longitude = response.json()["iss_position"]["longitude"]
latitude = response.json()["iss_position"]["latitude"]

location = (latitude,longitude)

print(location)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

response2 = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
response2.raise_for_status()

sunrise = int(response2.json()["results"]["sunrise"].split("T")[1].split(":")[0]) - 4
sunset = int(response2.json()["results"]["sunset"].split("T")[1].split(":")[0]) - 4

time_now = datetime.now().hour
print(time_now)
print(sunrise)
print(sunset)