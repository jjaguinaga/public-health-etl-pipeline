import requests
from pymongo import MongoClient

def extract_data():
    url = 'https://data.cdc.gov/resource/3rge-nu2a.json?$limit=2000'
    headers = {'Accept': 'application/json'}
    response = requests.get(url, timeout=30, headers=headers)
    return response.json()

def store_raw_data(data):
   client = MongoClient('localhost', 27017)
   db = client['public_health']
   collection = db['covid_raw']
   collection.delete_many({})
   collection.insert_many(data)
   print('Data loaded!')

if __name__ == '__main__':
   results = extract_data()
   store_raw_data(results)
   
