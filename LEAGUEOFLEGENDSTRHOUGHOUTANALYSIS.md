# My League Of Legends Project

![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/-SQL-4479A1?style=flat-square&logo=postgresql&logoColor=white)

Welcome to my first project! This project focuses on building a program to search and see the best player on the server of EUW in the game of League Of Legends, to not only watch his achievements but to compare it with yours, in this README file I'll show you my thought proccess and upload my data, codes and all.

## Technologies Used
- Python
- SQL

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/tempztzektana/portfolio
2. Everything should be organized for easy to look through, though I'll add photos here so you don't need to worry.

## The start of the project
At first I needed to gather the data, for that I used the raw data collection from the game API that user [Mitchell J](https://www.kaggle.com/datasnaek) uploaded on site [kaggle](https://www.kaggle.com/datasets/datasnaek/league-of-legends?resource=download). The data is 7 years old and is mostly in json files that I need to first convert. 

## Converting JSON files to add the to my SQL database
Using Python and installing 3 libraries [pandas](https://pandas.pydata.org/), [psycopg2](https://www.psycopg.org/docs/) and [SQLAlchemy](https://www.sqlalchemy.org/) (because the pandas library works only with SQLite and I'm working with PostgreSQL, for SQLAlchemy I needed to install the psycopg2-binary library that doesn't work with later versions than 3.11):

1. Installing dependecies
   ```bash
   pip install pandas sqlalchemy psycopg2-binary
   ```
   
After the instalation I've looked into the JSON file using VSC to see how the data is interpreted.
   
Example from data:

  <div align="center">
  <img src="https://github.com/user-attachments/assets/243d631e-9876-41b6-9dec-6d15a4c9d612" alt="Moje obrázek" width="400">
  </div>

With the way the content is interpreted I started researching in the pandas guidebook how to proceed and what lines of code are needed. With that said I've come up with this code

```python
# Importing the dependency libraries
import pandas as pd
from sqlalchemy import create_engine
import json

# The path to the JSON file
json_file_path = "\GitHub\Portfolio\LEAGUE OF LEGENDS THROUGHOUT ANALYSIS\Data\champion_info.json"

#Loading data from the JSON file
with open(json_file_path, 'r') as file:
    json_data = json.load(file)

# Conversion of the data to dataframe (pandas)
champions_data = json_data['data']                              # extraction of the 'data' contents
df = pd.DataFrame.from_dict(champions_data, orient='index')     # Conversion to the dataframe, saving ton of time writing out the full code

# Addition of the columns 'type' and 'version'
df['type'] = json_data['type']
df['version'] = json_data['version']

# Renaming the id column with champion_id to add the ID primary key
df.rename(columns={'id':'champion_id'}, inplace=True)

final_df = df[['champion_id', 'type', 'version', 'title', 'key', 'name']]
# print(final_df.to_string(index=False)) # For test before the real run

# Connecting to the database
db_uri = 'postgresql://postgres:_____@localhost:5432/LEAGUE OF LEGENDS MATCH HISTORY'
engine = create_engine(db_uri)

# Saving it into the database
final_df.to_sql('champion_info', engine, if_exists='replace', index=False)


## Conclusion of the conversion
```

With that done and completed I've achieved a python program conversion of JSON files into PostgreSQL database system, PostgreSQL has option to add JSON file datatypes but that would be easier and I would'nt need to use python at all with that and I was looking forward to use python, in addition you can see my rough skills with python.

With simple SQL query I've checked if everything is succesfully connected into the database
```SQL
   SELECT * FROM champion_info
```
And the output was: 
<div align="center">
  <img src="https://github.com/user-attachments/assets/62d8005f-a3bb-468c-8b82-f07ac04671a5" alt="Moje obrázek" width="800">
</div>

Now what is left to do is extracting all the JSON files into the database.
## Creating customizable program to convert the JSON datatype
The data has 3 files of JSON datatype, for that I figured out I'll make the code into function and only call which I needed (I need only 2 files since the first was for the test).
For that I've easily just updated the path and some information of data according to the file and made a main.py file to call both functions together at once.

After 2 hours I've finally figured out how to add inputs into the code, I've also added a 5 lines of example what is inside the file.
The code I've came up with:

```python
#Importing the dependency libraries
import pandas as pd
from sqlalchemy import create_engine
import json


def export_json_to_database_champion_info():
    # The path to the JSON file
    print("Enter the path to the file: ")
    path = input()

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
    file_data = json_data['data']                              # Extraction of the 'data' contents
    df = pd.DataFrame.from_dict(file_data, orient='index')     # Conversion to the dataframe

    # Print the structure of the dataframe for debugging
    print("DataFrame columns:", df.columns.tolist()) # Show what's inside the dataframe
    print("DataFrame head:\n", df.head())  # Print first few rows

    # Addition of the columns 'type' and 'version'
    df['type'] = json_data['type']
    df['version'] = json_data['version']

    # Renaming the id column with the idname to add the ID primary key in SQL
    print("What to do you want to rename the ID to: ")
    idname = input()
    
    if 'id' in df.columns:
        df.rename(columns={'id': idname}, inplace=True)
    else:
        print("Warning: 'id' column not found. No renaming performed.")

    if df.empty:
        print("Error: The DataFrame is empty. No data to export.")
        return

    # Connecting to the database
    db_uri = 'postgresql://postgres:_____@localhost:5432/LEAGUE OF LEGENDS MATCH HISTORY'
    engine = create_engine(db_uri)


    print("Lastly, what do you want to name the table?: ")
    tablename = input()
    df.to_sql(tablename, engine, if_exists='replace', index=False)
export_json_to_database_champion_info()
```

After this accomplishment I'm able to compile this python file. Tinkering a while and I've finally made the raw code for the whole application using 3 files.
* main_conversion_file.py
```python
   #Name of the function
def main():
    print("Welcome to JSON to SQL exporter!")
    print("""
Press 1 to continue
Press 2 to see the credits
Press q to quit
          """)
    inputmain = input()         #User input
    if inputmain == str(1):     #Go to the main file
        import databaseconnect
        databaseconnect.dataconnect()
    elif inputmain == str(2):   #See the credits
        print("This program was created by Filip Vašíček as his side project for the main project of his league of legends analysis.")
        print("Press enter to continue.\n")
        inputcredit = input()

        if inputcredit == "":
            main()
        else:
            print("I've said enter!\n")
            main()

    elif inputmain == "q":      #Quit the program
        exit() 
    else: 
        print("Can't read the input!\n")
        main()
#call the function
main()
```

* databaseconnect.py
```python
#Basic dependencies
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError



#Connect to the URI database
def dataconnect():
    db_uri = input("Write out your database URI. (Example: postgresql://username:password@host:port/database_name for PostgreSQL): \n")
    try:
        
# Create the engine
        engine = create_engine(db_uri)
        
# Try to connect to the database
        with engine.connect() as connection:
            print("\nConnection successful!\n")
            import functions_for_conversion
            functions_for_conversion.export_json_to_database_champion_info(engine)
            return engine 
            
    except SQLAlchemyError as e:
# Handle the error and print an appropriate message
        print(f"\nConnection failed: {e}\n")
```

* functions_for_conversion.py
```python
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

```

After that I've compiled the files into 1 exec file and can finally move onto the data manipulation itself. (The code itself will need some tinkering since it is raw and not yet fully optimized, for that I'll need more time but this is the raw version I've come up with and that works.)

## Creating SQL queries.







