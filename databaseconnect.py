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
