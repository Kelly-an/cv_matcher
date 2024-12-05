from datetime import date
from pathlib import Path
from os import getenv

# API
API_KEY = getenv('API_KEY')
API_SECRET = getenv('API_SECRET')
ACCESS_TOKEN_URL = 'https://entreprise.francetravail.fr/connexion/oauth2/access_token'
API_URL = 'https://api.francetravail.io/partenaire/offresdemploi/v2/offres/search/'
MAX_OFFRES = 3150

# Local
FILEPATH = f'data/{date.today().strftime("%Y-%m-%d")}'

def get_filename(lower_range, upper_range):
    Path(FILEPATH).mkdir(parents=True, exist_ok=True)
    return f'{FILEPATH}/raw_data_{lower_range}_{upper_range}.json'

# DB
MONGO_URL = getenv('MONGO_DB_URL')
DB_NAME = getenv('DB_NAME')

OFFERS_COLLECTION = 'offers'
LANGUES_COLLECTION = 'langues'
FORMATIONS_COLLECTION = 'formations'
PERMIS_COLLECTION = 'permis'
COMPETENCES_COLLECTION = 'competences'
QUALITES_PROFESSIONNELLES_COLLECTION = 'qualitesProfessionnelles'
