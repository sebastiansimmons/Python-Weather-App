from xmlrpc.client import Boolean
import requests
import sys
from PySide6.QtWidgets import QLineEdit, QPushButton, QApplication, QVBoxLayout, QDialog

from lib import load_2022_census_zipcodes

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

# #You can retrieve the metadata for a given latitude/longitude coordinate with the /points endpoint (https://api.weather.gov/points/{lat},{lon}).



#r = requests.get('https://api.weather.gov/points/45.601815.-122.700798/')

#r = requests.get('https://api.weather.gov/points/39.7456,-97.0892')

# OLD LIST
# ZIPCODE_LIST = lib.load_zip_codes() 

ZIPCODE_LIST = load_2022_census_zipcodes()

class WeatherApp(QDialog):

    def __init__(self, parent=None):
        super(WeatherApp, self).__init__(parent)
        self.setWindowTitle("Get Weather")

        # Create Widgets
        self.zipInput = QLineEdit(placeholderText="Enter a zipcode...", inputMask="99999")
        self.button = QPushButton("Get Weather")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.zipInput)
        layout.addWidget(self.button)

        self.setLayout(layout)

        self.button.clicked.connect(self.getForecast)
    
    def getForecast(self):    
        zipcode = self.zipInput.text()
        print(f"Looking up weather at {zipcode}")
        print(type(zipcode))

        if self.zipcode_is_valid(zipcode):
            print(f"VALID ZIPCODE {zipcode}")
            lat = ZIPCODE_LIST[zipcode]["lat"]
            lon = ZIPCODE_LIST[zipcode]["long"]
            print(f"lat: {lat}, long: {lon}")

            # #You can retrieve the metadata for a given latitude/longitude coordinate with the /points endpoint (https://api.weather.gov/points/{lat},{lon})
            #r = requests.get(f'https://api.weather.gov/points/{lat},{lon}')


    def zipcode_is_valid(self, zipcode: str) -> Boolean:
        '''Checks if an entered string is a valid zipcode'''
        return zipcode in ZIPCODE_LIST




if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    weather = WeatherApp()
    weather.show()
    # Run the main Qt loop
    sys.exit(app.exec())