# this program will get the weather from https://openweathermap.org/
# importing requests and json
import requests, json
#base URL
#BASE_URL ="https://api.openweathermap.org/data/2.5/weather?zip={zip code},{country code}&appid={API key}"
#base_Url =https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
BASE_URL ="https://api.openweathermap.org/data/2.5/weather?"

# for zipcode search use zipCode and countryCode plus apikey and units
#zipCode = "98226"
#user_zip=(input("What zip code would you like to see the weather for?"))
#countryCode = "US"
Latitude= 48.7974
Longitude= -122.4448
API_KEY = "920fb5024e83f724bfc1a2353d7ae8e5"
units = "imperial"

# updating the URL using lat and long
URl = BASE_URL + "lat=" + str(Latitude) + "&lon=" + str(Longitude) + "&appid=" + API_KEY + "&units=" + units
# updating the url with zip code in program
#URl = BASE_URL + "zip=" + zipCode + "," + countryCode + "&appid=" + API_KEY + "&units=" + units
# updating the url using user input for zip code
#URl = BASE_URL + "zip=" + user_zip + "," + countryCode + "&appid=" + API_KEY + "&units=" + units
# Http request
response = requests.get(URl)
print(response.status_code)
# print(URl)
if response.status_code == 200:
      # getting data in the json format
      data = response.json()
      # getting the main dict block
      main = data['main']
      # getting the temperature
      temperature = main['temp']
      # getting the humidity
      humidity = main['humidity']
      # Getting the pressure
      pressure = main['pressure']


print("Good Morning Ryan!"
      "\nI will tell you the weather for today in belilngham"
      "\nHere is the Temp " + str(temperature))
