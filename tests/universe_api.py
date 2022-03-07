import requests
import json
from dotenv import load_dotenv, find_dotenv
import os

# Initilize API_KEY
# Get the path to the directory this file is in
BASEDIR = os.path.abspath(os.path.dirname(__file__))
# Connect the path with your '.env' file name
load_dotenv(os.path.join(BASEDIR, '.env'))

API_KEY = os.getenv("API_Authorization")

def get_university_from_db():
    base_url = "https://api.m3o.com/v1/db/Read"
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + API_KEY
}
    table_to_query = 'university'
    payload = json.dumps({
        "table": table_to_query
    })
   
    response = requests.post(base_url, headers=headers, data=payload)
    json_data = json.loads(response.text)
    return json_data['records']
    
def get_universities_by_country(country):
    base_url = "http://universities.hipolabs.com/search?"
    params = {
        'country': country,
    }
    response = requests.get(base_url, params=params)
    status_code = response.status_code
    json_data = json.loads(response.text)
    return json_data, status_code