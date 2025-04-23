import pandas as pd
import sqlalchemy
import logging
from sqlalchemy import text

def load_data(df: pd.DataFrame, db_url: str = "postgresql://postgres:password@db:5432/earthquakes"): 
    logging.info("Connecting to the PostgreSQL database")
    try:
        engine = sqlalchemy.create_engine(db_url)
        with engine.connect() as connection:
            logging.info("Inserting data into the database...")
            df.to_sql("earthquakes", con=connection, if_exists="replace", index=False)
            logging.info("Data successfully inserted into the 'earthquakes' table.")
            result = connection.execute(text("SELECT COUNT(*) FROM earthquakes;"))
            count = result.scalar()
            logging.info(f"Total rows in 'earthquakes' table: {count}")
    except Exception as e:
        logging.error(f"Error while inserting data: {e}")
        raise
