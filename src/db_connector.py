from pymongo import MongoClient
from config.params import MONGO_URL, DB_NAME
import pandas as pd

def get_db():
    client = MongoClient(MONGO_URL)
    # Access the database
    db = client[DB_NAME]
    return db

def insert_documents(collection_name, documents: pd.DataFrame, fetch_data_range):
    try:
        print(f'Range {fetch_data_range}')
        db = get_db()
        collection = db[collection_name]
        # Deleting existing data from previous run
        result = collection.delete_many({'date_range': fetch_data_range})
        print(f'Deleted {result.deleted_count} from {collection_name}')
        documents['date_range'] = fetch_data_range
        result = collection.insert_many(documents.to_dict(orient='records'))
        print(f"Inserted {len(result.inserted_ids)} documents in collection {collection_name}")
    except Exception as e:
        print(f'Could not insert in {collection_name}: {e}')
