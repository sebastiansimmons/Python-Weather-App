# lib.py - Library file for a zipcode based weather app.
import csv
from xmlrpc.client import boolean


ZIPCODE_FILE = "zip_lat_long"

def load_2010_zipcodes() -> dict:
    '''Loads the 2010 zipcode dataset and returns a dictionary'''
    file = "data/zip_lat_long"
    zips = {}

    f = open(file, "r")
    f.readline()    # Pop the first line that shows the format
    for line in f:
        line = line.strip() # Strip new line character
        zip_lat_long = line.split(",")
        zips[zip_lat_long[0]] = (zip_lat_long[1], zip_lat_long[2])
    return zips

def load_simplemap_zips() -> dict:
    '''Loads the https://simplemaps.com free data set and returns a dictionary'''
    zips = {}
    file = "data/uszips.csv"

    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            zips[row['zip']] = row
    return zips

def load_2022_census_zipcodes() -> dict:
    '''loads the 2022 census zipcode tabulation dataset'''
    zips = {}
    file = "data/2022_Gaz_zcta_national.txt"

    with open(file, "r") as f:
        # Pop the data legend first line
        legend = f.readline().strip().split("\t")
        zip_index = legend.index('GEOID')
        lat_index = legend.index('INTPTLAT')
        lon_index = legend.index('INTPTLONG')
        for line in f:
            line = line.strip().split("\t")
            zips[line[zip_index]] = {"lat": line[lat_index], "long": line[lon_index]}
        return zips
            

