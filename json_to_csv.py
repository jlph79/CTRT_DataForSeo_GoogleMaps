import pandas as pd
import json

# Path to your JSON file
#json_file = 'DataForSEO_Output\extracted_GoogleMapsDataset_schools_raw.json'

# Path to your JSON file
json_file = 'test_file.json'  # Adjust the path to your file

# Read the JSON data from the file
with open('test_file.json') as json_file:
    jsondata = json.load(json_file)
    print("File opened")


# Extracting items from the nested JSON structure
items = jsondata['top_level']['level1']['level2']['items']

# Use json_normalize to flatten the nested JSON structure
df = pd.json_normalize(items, 
                       sep='_', 
                       record_path=None,
                       meta=['id', 'name', ['details', 'description'], ['details', 'metadata', 'type'], ['details', 'metadata', 'tags']])

# Renaming columns for clarity
df.columns = ['id', 'name', 'description', 'type', 'tags']
print(df)
# Print the loaded data to verify
#print(json.dumps(data, indent=4))
