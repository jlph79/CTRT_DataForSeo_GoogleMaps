import pandas as pd
from sqlalchemy import create_engine

# Define your connection details
server = 'ctrt-sqlserver.database.windows.net'
database = 'ctrt-sqldb'
username = 'CTRT-admin'
password = 'Hso2Ghana'
table_name = 'bronze.PS_Highschools_Accra' 
port = '1433'  # Default is 1433, e.g., '1433'

# Create the connection string for SQLAlchemy
connection_string = (
    f"mssql+pyodbc://{username}:{password}@{server}:{port}/{database}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
)

# Establish the connection using SQLAlchemy create_engine
engine = create_engine(connection_string, echo=False)  # Set echo=True for debugging

# Define the query
query = f"SELECT * FROM {table_name}"

# Execute the query and load the data into a DataFrame
df = pd.read_sql(query, engine)

# Show the DataFrame

#pd.set_option('display.max_columns', None)
#pd.reset_option('max_columns')

print(df)
#w['female'] = w['female'].map({'female': 1, 'male': 0})
# Add transformations

#REPLACE
df['rating_value'] = df['rating_value'].replace(',', 0)
#print(df[['rating_value']].to_string(index=False)) 

#df['A'] = df['A'].replace('@', '', regex=True)

#SPLIT

print(df[['address']].to_string(index=False)) 
split_columns = df['address'].str.split(',', expand=True)

# Rename the new columns (optional)
max_splits = split_columns.shape[1]
column_names = [f'Col{i+1}' for i in range(max_splits)]
split_columns.columns = column_names

print(split_columns)
df = pd.concat([df, split_columns], axis=1)

df['Streetname'] = df['address'].str.split(',', n=1).str[0]
#print(df[['Streetname']].to_string(index=False)) 

#RATING
def classify_rating(rating):
    if rating > 4:
        return 'High'
    elif 2.5 <= rating <= 4:
        return 'Average'
    else:
        return 'Low'

# Create the rating_category column
df['rating_category'] = df['rating_value'].apply(classify_rating)
print(df[['rating_category']].to_string(index=False)) 

pd.set_option('display.max_columns', None)
print(df)
# Concatenate the new columns with the original dataframe
#df = pd.concat([df, split_columns], axis=1)

new_schema = 'silver'
new_table_name = 'Population'

# Write DataFrame to the new table in the specified schema in the database
#df.to_sql(new_table_name, engine, schema=new_schema, if_exists='replace', index=False)

#print(f"Data written to {new_schema}.{new_table_name} successfully.")