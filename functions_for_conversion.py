#Importing the dependency libraries
import pandas as pd
import json
from sqlalchemy.exc import SQLAlchemyError


#Function for the export
def export_json_to_database_champion_info(engine):
# The path to the JSON file
    print("Enter the path to the file(press enter to go back): ")
    path = input()
    if path == "":
        print("Returning back.")
        return
    else:
# Loading data from the JSON file
        try:
            with open(path, 'r') as file:
                json_data = json.load(file)
        except FileNotFoundError:
            print("Error: The specified file was not found.")
            return
        except json.JSONDecodeError:
            print("Error: the file is not a valid JSON")
            return

# Conversion of the data to dataframe (pandas)
    file_data = json_data['data']                               # Extraction of the 'data' contents
    df = pd.DataFrame.from_dict(file_data, orient='index')      # Conversion to the dataframe

# Print the structure of the dataframe for debugging
    print("DataFrame columns:", df.columns.tolist())            # Show what's inside the dataframe
    print("DataFrame head:\n", df.head())                       # Print first few rows

# Addition of the columns 'type' and 'version'
    df['type'] = json_data['type']
    df['version'] = json_data['version']

# Renaming the id column with the idname to add the ID primary key in SQL
    def rename_id():
        print("What to do you want to rename the ID to: ")
        idname = input()
        
        if 'id' in df.columns:
            df.rename(columns={'id': idname}, inplace=True)
        else:
            print("Warning: 'id' column not found. No renaming performed. Try again")
            print("DataFrame columns:", df.columns.tolist())    # Show what's inside the dataframe for the renaming
            print("DataFrame head:\n", df.head())
            rename_id() #Return back to renaming the ID
    if df.empty:
        print("Error: The DataFrame is empty. No data to export.")
        return
    rename_id()
    # Export Dataframe to SQL 
    try:
            table_name = input("Set your table name: \n")  # Set your table name here
            df.to_sql(table_name, con=engine, if_exists='replace', index=False)
            print(f"Data successfully exported to the '{table_name}' table in the database.")
    except SQLAlchemyError as e:
            print(f"Error exporting data to SQL: {e}")
