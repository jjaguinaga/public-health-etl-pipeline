import pandas as pd
from pymongo import MongoClient

def get_raw_data():
   client = MongoClient('localhost', 27017)
   db = client['public_health']
   collection = db['covid_raw']
   data = list(collection.find())
   df = pd.DataFrame(data)
   return df
   
# print(df['age_group'].unique())

def clean_data(df):
   df = df.drop(columns=['_id', 'mmwr_week'])
   df = df[df.age_group != 'all_ages_adj']
   df = df.drop(columns=['age_adj_vax_ir', 'age_adj_unvax_ir', 'age_adj_irr'])
   float_col = ['vaccinated_with_outcome', 'fully_vaccinated_population', 'unvaccinated_with_outcome', 'unvaccinated_population', 'crude_vax_ir', 'crude_unvax_ir', 'continuity_correction', 'crude_irr']
   
   for column in float_col:
      if column == 'crude_irr':
         df[column] = pd.to_numeric(df[column], errors='coerce')
         df[column] = df[column].fillna(df[column].mean())
      else:
         df[column] = df[column].str.replace(',', '').astype(float)
   
   return df

if __name__ == '__main__':
   df = get_raw_data()
   df = clean_data(df)
   print(df.head())
   print(df.info())