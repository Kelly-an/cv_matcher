from config.params import (
    LANGUES_COLLECTION,
    FORMATIONS_COLLECTION,
    PERMIS_COLLECTION,
    COMPETENCES_COLLECTION,
    QUALITES_PROFESSIONNELLES_COLLECTION,
    OFFERS_COLLECTION, MAX_OFFRES, get_filename)
from src.etl.api_connector import get_all_offers
import src.etl.data_transformer as dt
from src.etl.db_connector import insert_documents
from re import sub as re_sub

def main():
    # Fetching from api and loading to data folder
    get_all_offers()

    for i in range(MAX_OFFRES//150):
        # Read the json file

        filepath = get_filename(i*150, (i*150)+149)
        df = dt.read_data(filepath)
        fetch_date_range = re_sub(r'[^0-9a-z]', '', filepath)

        # Apply simple transformations, that don't require an other table
        df = dt.simple_transfo(df)

        # Apply normalisation for these columns
        for col in [
            LANGUES_COLLECTION,
            FORMATIONS_COLLECTION,
            PERMIS_COLLECTION,
            COMPETENCES_COLLECTION,
            QUALITES_PROFESSIONNELLES_COLLECTION
        ]:
            df, df_col = dt.expand_list_fields(df, col)
            insert_documents(col, df_col, fetch_date_range)

        # inserting normalised offers in table
        insert_documents(OFFERS_COLLECTION, df, fetch_date_range)




if __name__=='__main__':
    main()
