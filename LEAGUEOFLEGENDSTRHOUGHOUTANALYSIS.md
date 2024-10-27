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
Using Python and installing 2 libraries [pandas](https://pandas.pydata.org/) and [SQLAlchemy](https://www.sqlalchemy.org/) (because the pandas library works only with SQLite and I'm working with PostgreSQL, for SQLAlchemy I needed to install the psycopg2-binary library that doesn't work with later versions than 3.11):

1. Installing dependecies
   ```bash
   pip install pandas sqlalchemy psycopg2
   ```
After the instalation I've looked into the json file using VSC to see how the data is interpreted.
   Example from data
  <div align="center">
  <img src="https://github.com/user-attachments/assets/243d631e-9876-41b6-9dec-6d15a4c9d612" alt="Moje obrázek" width="400">
  </div>
With the way the content is interpreted noted I started researching in the pandas guidebook how to proceed and what lines of code are needed. With that said I've come up with this code
   
         # Importing the dependency libraries
         import pandas as pd
         from sqlalchemy import create_engine
         import json
            
         # The path to the JSON file
         json_file_path = r"\GitHub\Portfolio\LEAGUE OF LEGENDS THROUGHOUT ANALYSIS\Data\champion_info.json"
         
         # Loading data from the JSON file
         with open(json_file_path, 'r') as file:
             json_data = json.load(file)
         
         # Conversion of the data to dataframe (pandas)
         champions_data = json_data['data']                              # extraction of the 'data' contents
         df = pd.DataFrame.from_dict(champions_data, orient='index')     # Conversion to the dataframe
         
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

With that done and completed I've achieved a python programme conversion of JSON files into PostgreSQL database system, PostgreSQL has option to add JSON file datatypes but that would be easier and I would'nt need to use python at all with that and I was looking forward to use python, in addition you can see my rough skills with python.

