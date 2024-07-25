import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

# Define your connection details
server = 'ctrt-sqlserver.database.windows.net'
database = 'ctrt-sqldb'
username = 'CTRT-admin'
password = 'Hso2Ghana'
hospitals_kumasi = 'silver.SO_Hospitals_Kumasi' 
hospitals_accra = 'silver.SO_Hospitals_Accra' 
port = '1433'  # Default is 1433, e.g., '1433'

# Create the connection string for SQLAlchemy
connection_string = (
    f"mssql+pyodbc://{username}:{password}@{server}:{port}/{database}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
)

# Establish the connection using SQLAlchemy create_engine
engine = create_engine(connection_string, echo=False)  # Set echo=True for debugging

# Define the query
Kumasi = f"SELECT * FROM {hospitals_kumasi}"
Accra = f"SELECT * FROM {hospitals_accra}"

# Execute the query and load the data into a DataFrame
df_k = pd.read_sql(Kumasi, engine)
df_a = pd.read_sql(Accra, engine)


df_k['Region'] = df_k['Region'].replace('Ashanti Region', 'Ashanti')
#from datetime import datetime

#df_pop['Date'] = datetime.today().strftime('%m/%d/%Y')
#df_pop['Date'] = pd.to_datetime(df_pop['Date']).dt.date




# Select specific columns from df_his

# Concatenate df_his_selected with df_pop, ignoring avg_household_size and number_of_households

df_appended = pd.concat([df_a, df_k], ignore_index=True)


pd.set_option('display.max_columns', None)



df_appended['Date'] = datetime.today().strftime('%m/%d/%Y')
df_appended['Date'] = pd.to_datetime(df_appended['Date']).dt.date


#print(df_appended['Date'])
#df_appended['Population'] = df_appended['Population'].astype(int)
#df_appended['Population'] = pd.to_numeric(df_appended['Population'], errors='coerce')

new_schema = 'gold'
new_table_name = 'PS_fact_Amenities'

# Write DataFrame to the new table in the specified schema in the database
df_appended.to_sql(new_table_name, engine, schema=new_schema, if_exists='replace', index=False)

print(f"Data written to {new_schema}.{new_table_name} successfully.")