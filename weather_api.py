import requests

city_name = raw_input('Choose a city: ')
print 'You picked ' + city_name

endpoint = "https://publicdata-weather.firebaseio.com/%s/currently.json"%city_name
response = requests.get(endpoint)
data = response.json()

print data
