import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

# Define your connection details
server = 'ctrt-sqlserver.database.windows.net'
database = 'ctrt-sqldb'
username = 'CTRT-admin'
password = 'Hso2Ghana'
population = 'bronze.KURO_Population' 
history = 'bronze.WP_Population_History' 
port = '1433'  # Default is 1433, e.g., '1433'

# Create the connection string for SQLAlchemy
connection_string = (
    f"mssql+pyodbc://{username}:{password}@{server}:{port}/{database}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
)

# Establish the connection using SQLAlchemy create_engine
engine = create_engine(connection_string, echo=False)  # Set echo=True for debugging

# Define the query
Population = f"SELECT * FROM {population}"
History = f"SELECT * FROM {history}"

# Execute the query and load the data into a DataFrame
df_pop = pd.read_sql(Population, engine)
df_his = pd.read_sql(History, engine)

df_pop.columns = df_pop.columns.str.strip()

df_pop['Household Population'] = (
    df_pop['Household Population']
    .str.replace('"', '')
    .str.replace('.','')
    .astype(int)
)

df_pop = df_pop.rename(columns={'Household Population': 'Population'})

df_pop['Number of Households'] = (
    df_pop['Number of Households']
    .str.replace('"', '')
    .str.replace('.','')
    .astype(int)
)


df_pop['Average Household Size'] = df_pop['Average Household Size'].astype(float)

df_pop['Date'] = datetime.today().strftime('%m/%d/%Y')

print(df_pop)

# Select specific columns from df_his

# Concatenate df_his_selected with df_pop, ignoring avg_household_size and number_of_households

df_appended = pd.concat([df_his, df_pop[['Region', 'Date', 'Population']]], ignore_index=True)

print(df_appended)

df_appended['Date'] = df_appended['Date'] = pd.to_datetime(df_appended['Date']).dt.date
#df_appended['Population'] = df_appended['Population'].astype(int)
df_appended['Population'] = pd.to_numeric(df_appended['Population'], errors='coerce')

new_schema = 'silver'
new_table_name = 'PS_Population_Ghana'

# Write DataFrame to the new table in the specified schema in the database
df_appended.to_sql(new_table_name, engine, schema=new_schema, if_exists='replace', index=False)

print(f"Data written to {new_schema}.{new_table_name} successfully.")