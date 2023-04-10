import requests
from datetime import datetime

MY_LAT = 42.395760 # latitude
MY_LONG = -70.993150 # longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) - 4 
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) - 4

time_now = datetime.now().hour

def isitDark():
    if time_now > sunset or time_now < sunrise: return(True)

def isISSabove():
    if isitDark():
        if iss_latitude - MY_LAT <= 5 and iss_longitude - MY_LONG <= 5:
            return(True)
        else:
            print("The ISS is not in viewing range for you right now")
    else:
        print("Not dark enough outside to see the ISS")

# print(sunrise, sunset, time_now)
# print(iss_latitude, iss_longitude)
# print(MY_LAT, MY_LONG)

isISSabove()
