from lib import *


#ZIPS = load_zip_codes()
ZIPS = load_2022_census_zipcodes()

multnomah = "97217"
print(multnomah in ZIPS)
print(ZIPS[multnomah])
print(ZIPS[multnomah]["lat"])
print(ZIPS[multnomah]["long"])