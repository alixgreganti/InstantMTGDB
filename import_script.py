import os
import time
import requests
import pandas as pd
from sqlalchemy import create_engine

# Create SQL Alchemy engine
engine = create_engine('mysql+pymysql://root:root@localhost/mydb')

while True:
    # Download JSON
    response = requests.get("https://data.scryfall.io/oracle-cards/oracle-cards-20230521210353.json")
    data = response.json()

    # Check if file size has changed
    new_file_size = len(response.content)
    old_file_size = os.path.getsize('oracle-cards.json') if os.path.isfile('oracle-cards.json') else 0

    if new_file_size != old_file_size:
        # Write new file
        with open('oracle-cards.json', 'w') as f:
            f.write(response.text)

        # Convert to DataFrame
        df = pd.DataFrame(data)

        # Save to MySQL
        df.to_sql('cards', engine, if_exists='replace')

    # Wait for 24 hours
    time.sleep(24 * 60 * 60)
