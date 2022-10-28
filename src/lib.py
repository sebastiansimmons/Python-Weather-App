# lib.py - Library file for a zipcode based weather app.
ZIPCODE_FILE = "zip_lat_long"

def load_zip_codes() -> dict:
    '''Load the file of zip codes with their corresponding coordinates and return a dictionary'''
    zips = {}
    f = open(ZIPCODE_FILE, "r")
    f.readline()    # Pop the first line that shows the format
    for line in f:
        line = line.strip() # Strip new line character
        zip_lat_long = line.split(",")
        zips[zip_lat_long[0]] = (zip_lat_long[1], zip_lat_long[2])
    return zips
