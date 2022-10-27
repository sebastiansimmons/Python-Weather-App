import requests
import sys
# Using the weather.gov API
# https://www.weather.gov/documentation/services-web-api
# https://weather-gov.github.io/api/
# EXAMPLE RESPONSE
# https://api.weather.gov/points/45.6018,-122.7007
# https://api.weather.gov/gridpoints/TOP/31,80/forecast

# DESIGN PLAN
# User enters zip code
# Program references zip code to longitude and lattitude list from here https://gist.github.com/erichurst/7882666 that was downloaded to zip_lat_long
# REQUEST sent to weather.gov API
# use PySide to display:
# Current weather
# Maybe some other shit but let's start with that because I'm new to this



r = requests.get('https://api.weather.gov/points/45.601815.-122.700798/')

r = requests.get('https://api.weather.gov/points/39.7456,-97.0892')


