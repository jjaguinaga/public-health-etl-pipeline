import pandas as pd
import psycopg2
from transform import get_raw_data, clean_data

def load_data():
    vaccine = get_raw_data()
    vaccine = clean_data(vaccine)
    
    conn = psycopg2.connect(dbname='covid_vaccine_project', user='naga', host='localhost')
    cur = conn.cursor()
    
    # Drop and recreate table
    cur.execute('DROP TABLE IF EXISTS vaccine CASCADE;')
    
    # Create columns dynamically
    cols = ', '.join([f'"{c}" TEXT' for c in vaccine.columns])
    cur.execute(f'CREATE TABLE vaccine ({cols});')
    
    # Insert rows
    for _, row in vaccine.iterrows():
        vals = ', '.join(['%s'] * len(row))
        cur.execute(f'INSERT INTO vaccine VALUES ({vals})', tuple(row.astype(str)))
    
    conn.commit()
    cur.close()
    conn.close()

if __name__ == '__main__':
    load_data()
    print('Data loaded into PostgreSQL!')