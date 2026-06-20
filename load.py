import pandas as pd
from sqlalchemy import create_engine
from transform import get_raw_data, clean_data

engine = create_engine('postgresql://naga@localhost:5432/covid_vaccine_project')
 
def load_data():
   vaccine = get_raw_data()
   vaccine = clean_data(vaccine)
   vaccine.to_sql('vaccine', engine, if_exists='replace', index=False)
   
if __name__ == '__main__':
    load_data()
    print('Data loaded into PostgreSQL!')