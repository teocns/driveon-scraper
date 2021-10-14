from api import retrieve_single_vehicle_data, retrieve_all_available_vehicles
import json
import base64
from config import API_REQUEST_HEADERS, GET_REQUEST_HEADERS
import requests
from config import BASE_URL
from db import save_coche
from helpers import make_apireq_data
from cloudscraper import CloudScraper


all_coches = retrieve_all_available_vehicles()

print("Retrieved %s cars" % len(all_coches))

for coche in all_coches:
    single_coche = retrieve_single_vehicle_data(coche['oid'])
    save_coche(single_coche)
    print("Saved coche %s" % single_coche['oid'])
