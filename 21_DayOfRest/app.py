'''
Ivan Yeung
SoftDev
K20 -- REST API
2022-11-21
time spent:  0.5hr
'''
import requests

country = "brazil"

API_URL = f"https://restcountries.com/v3.1/name/{country}"
print("***DIAG: API url ***")
print(API_URL)

r = requests.get(API_URL) #creating a response object that will get us the information we needr
api_dict = r.json() #r.json() returns a dictonary after deconding the response object
population = (api_dict[0])["population"]
currency = (api_dict[0])["currencies"]
print("Population of Brazil: " + str(population))
print("Currencies of Brazil: " + str(currency))
