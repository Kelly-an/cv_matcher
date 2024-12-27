from pymongo import MongoClient
from config.params import MONGO_URL, DB_NAME
import pandas as pd

def get_db():
    client = MongoClient(MONGO_URL)
    # Access the database
    db = client[DB_NAME]
    return db

def insert_resume(collection_name, documents: pd.DataFrame, resume_id):
    try:
        print(f'Resume Id {resume_id}')
        db = get_db()
        collection = db[collection_name]
        # Deleting existing data from previous run
        result = collection.delete_one({'resume_id': resume_id})
        print(f'Deleted {result.deleted_count} from {collection_name}')
        documents['resume_id'] = resume_id
        result = collection.insert_one(documents)
        print(f"Inserted {result.inserted_id} document in collection {collection_name}")
    except Exception as e:
        print(f'Could not insert in {collection_name}: {e}')
