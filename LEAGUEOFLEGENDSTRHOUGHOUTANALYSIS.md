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
   ```python
   pip install pandas sqlalchemy psycopg2
   ```
