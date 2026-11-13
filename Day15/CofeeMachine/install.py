import sqlite3
import os
from query import (
    CREATE_DRINKS_TABLE, INSERT_DRINKS,
    CREATE_COINS_TABLE, INSERT_COINS,
    CREATE_INGREDIENTS_TABLE, INSERT_INGREDIENTS,
    CREATE_TRANSACTIONS_TABLE
)

base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_dir, "data", "cofeemachine.db")

os.makedirs(os.path.dirname(db_path), exist_ok=True)


try:
    with sqlite3.connect(db_path) as con:
        
        cur = con.cursor()
        
        # Execute Table Creations
        cur.execute(CREATE_DRINKS_TABLE)
        cur.execute(CREATE_COINS_TABLE)
        cur.execute(CREATE_INGREDIENTS_TABLE)
        cur.execute(CREATE_TRANSACTIONS_TABLE)
        
        # Insert Initial Data
        # Note: Using 'OR IGNORE' in SQL is a good practice if you run this 
        # script multiple times to avoid Primary Key errors.
        cur.execute(INSERT_DRINKS.replace("INSERT INTO", "INSERT OR IGNORE INTO"))
        cur.execute(INSERT_COINS.replace("INSERT INTO", "INSERT OR IGNORE INTO"))
        cur.execute(INSERT_INGREDIENTS.replace("INSERT INTO", "INSERT OR IGNORE INTO"))
        
        print("Database initialized and populated successfully.")

except sqlite3.Error as e:
    print(f"An error occurred: {e}")

finally:
    # The 'with' block commits, but we still need to close the connection
    if 'con' in locals():
        con.close()
