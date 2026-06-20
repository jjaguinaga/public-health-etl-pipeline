import pandas as pd
from extract import extract_data, store_raw_data
from load import load_data 

if __name__ == '__main__':
   data = extract_data()
   store_raw_data(data)
   load_data()