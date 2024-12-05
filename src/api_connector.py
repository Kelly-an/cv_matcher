from json import dump as json_dump, load as json_load
from pathlib import Path
from requests import get, post
from config.params import get_filename, API_KEY, API_SECRET, API_URL, ACCESS_TOKEN_URL, MAX_OFFRES

def get_access_token():
    url = ACCESS_TOKEN_URL
    payload = {
        "grant_type": "client_credentials",
        "client_id": API_KEY,
        "client_secret": API_SECRET,
        "scope": "api_offresdemploiv2 o2dsoffre"
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    response = post(url, headers=headers, data=payload, params={"realm": "/partenaire"})

    return response.json()

def get_from_url(lower_range, upper_range, access_token):
    offre_url = API_URL
    access_token = get_access_token()['access_token']
    headers = {
        "Accept": "application/json",
        "Authorization": f'Bearer {access_token}'
    }
    params = {
        "range": f"{lower_range}-{upper_range}"
    }
    response = get(offre_url, headers=headers, params=params)

    with open(get_filename(lower_range, upper_range), 'w') as f:
        json_dump(response.json(), f, indent=4)

    return response.json()

def get_offres(lower_range, upper_range, access_token=None):
    result = None
    filepath = get_filename(lower_range, upper_range)
    try:
        my_file = Path(filepath)
        if my_file.is_file():
            with open(filepath, 'r') as f:
                result = json_load(f)
    except Exception as e:
        print(e)
    if result is None:
        print('Fetching from url')
        if access_token is None:
            access_token = get_access_token()
        result = get_from_url(lower_range, upper_range, access_token)

    print(f'Fetched {len(result["resultats"])} rows: {lower_range} - {upper_range}')

def get_all_offers():
    access_token = get_access_token()
    #TODO if not exactly 50, round up
    for i in range(MAX_OFFRES//150):
        r = i*150
        get_offres(r, r+149, access_token)



if __name__ == '__main__':
    for i in range(3):
        r = i*50
        get_offres(r, r+49)
