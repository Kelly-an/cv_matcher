from datetime import date
from pathlib import Path
from os import getenv

TODAY = date.today().strftime("%Y-%m-%d")

# API
API_KEY = getenv('API_KEY')
API_SECRET = getenv('API_SECRET')
ACCESS_TOKEN_URL = 'https://entreprise.francetravail.fr/connexion/oauth2/access_token'
API_URL = 'https://api.francetravail.io/partenaire/offresdemploi/v2/offres/search/'
MAX_OFFRES = 3150

# Local

def get_filename(lower_range, upper_range, date=TODAY):
    FILEPATH = f'data/api_data/{date}'
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
RESUMES_COLLECTION = 'resumes'

#chat gpt
DEFAULT_RESUME_PATH='/Users/kellyanne/Documents/recherche_emploi/cv_en_test.pdf'
OPENAI_KEY = getenv('OPENAI_KEY')
def get_chatgpt_answer_filename(name, folder_name, date=TODAY):
    CHATGPT_REPLY_FILEPATH = f'data/chatgpt/{date}/{folder_name}'
    Path(CHATGPT_REPLY_FILEPATH).mkdir(parents=True, exist_ok=True)
    return f'{CHATGPT_REPLY_FILEPATH}/{name}.txt'
# def get_chatgpt_answer_filename_json(name, date=TODAY):
#     CHATGPT_REPLY_FILEPATH = f'data/chatgpt/{date}'
#     Path(CHATGPT_REPLY_FILEPATH).mkdir(parents=True, exist_ok=True)
#     return f'{CHATGPT_REPLY_FILEPATH}/{name}.json'

TITLE_PROMPT = Path('data/chatgpt/prompts/title_lang.txt')
EDUCATION_PROMPT = Path('data/chatgpt/prompts/education.txt')
EXPERIENCE_PROMPT = Path('data/chatgpt/prompts/experience.txt')
SKILLS_PROMPT = Path('data/chatgpt/prompts/skills.txt')
