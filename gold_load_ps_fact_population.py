import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

# Define your connection details
server = 'ctrt-sqlserver.database.windows.net'
database = 'ctrt-sqldb'
username = 'CTRT-admin'
password = 'Hso2Ghana'
population = 'silver.AA_Population_Descripton_Ghana'  
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

# Execute the query and load the data into a DataFrame
df = pd.read_sql(Population, engine)

#print(df)

melted_df= pd.melt(df, id_vars=['ADM0_NAME', 'ADM0_PCODE','ADM1_NAME', 'ADM2_NAME'], 
                   value_vars=['T_25_29', 'T_30_34','T_35_39', 'T_40_44','T_45_49', 'T_50_54','T_55_59', 'T_60_64','T_65_69'])

melted_df = melted_df.rename(columns={'ADM0_NAME': 'Country'})
melted_df = melted_df.rename(columns={'ADM0_PCODE': 'Country Code'})
melted_df = melted_df.rename(columns={'ADM1_NAME': 'Region'})
melted_df = melted_df.rename(columns={'ADM2_NAME': 'Town'})
melted_df = melted_df.rename(columns={'variable': 'Age Category'})
melted_df = melted_df.rename(columns={'value': 'Population'})

melted_df['Country'] = melted_df['Country'].apply(str.title)
melted_df['Region'] = melted_df['Region'].apply(str.title)
melted_df['Town'] = melted_df['Town'].apply(str.title)

melted_df['Age Category'] = melted_df['Age Category'].str.replace('T_', '')
melted_df['Age Category'] = melted_df['Age Category'].str.replace('_', ' - ')

melted_df['Population'] = melted_df['Population'].astype(int)


melted_df['Date'] = '2021-01-01'
melted_df['Date'] = pd.to_datetime(melted_df['Date']).dt.date


print(melted_df)


new_schema = 'gold'
new_table_name = 'AA_fact_Population_Per_Agegroup'

# Write DataFrame to the new table in the specified schema in the database
melted_df.to_sql(new_table_name, engine, schema=new_schema, if_exists='replace', index=False)

print(f"Data written to {new_schema}.{new_table_name} successfully.")