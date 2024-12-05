import pandas as pd
from json import load as json_load
from config.params import get_filename

def read_data(filepath):
    # ensure filepath is for a json
    with open(filepath, 'r') as f:
        data = json_load(f)

    df = pd.DataFrame(data['resultats'])

    return df

def format_datetime_columns(df, columns_list=['dateCreation', 'dateActualisation']):
    for col in columns_list:
        df[col] = pd.to_datetime(df[col])
    return df

def expand_column(df, col):
    # Expect df with lieuTravail column
    expanded_columns = df[col].apply(pd.Series)
    expanded_columns = expanded_columns.add_prefix(f"{col}_")
    return pd.concat([df.drop(columns=[col]), expanded_columns], axis=1)

def get_company_name(df):
    df['entreprise'] = df['entreprise'].apply(pd.Series)['nom']
    return df


# permis, langues, formations, competences, salaire, contact, qualitesProfessionnelles
def expand_list_fields(df, col):
    df_col = df[col].apply(pd.Series)
    df_col = df_col.stack().reset_index(level=1, drop=True).apply(pd.Series).join(df['id'])
    df_col.reset_index(drop=True, inplace=True)
    # If permis is NA put False, else True
    df[col] = df[col].notna()
    return df, df_col

def get_main_table_columns():
    return [
        'id', 'intitule', 'description', 'dateCreation', 'dateActualisation',
        'romeCode', 'romeLibelle', 'entreprise', 'typeContrat', 'natureContrat',
        'experienceExige', 'experienceLibelle', 'dureeTravailLibelleConverti',
        'alternance', 'nombrePostes', 'qualificationCode', 'codeNAF',
        'secteurActiviteLibelle', 'permis', 'formations', 'langues',
        'lieuTravail_commune', 'lieuTravail_latitude', 'lieuTravail_longitude'
    ]

def simple_transfo(df):
    df = format_datetime_columns(df)
    df = expand_column(df,'lieuTravail')
    df = expand_column(df,'salaire')
    df = expand_column(df,'contact')
    df = get_company_name(df)
    return df


if __name__ == '__main__':
    df = read_data(get_filename(0,49))
    df = format_datetime_columns(df)
    df = expand_column(df,'lieuTravail')
    df = expand_column(df,'salaire')
    df = expand_column(df,'contact')
    df = get_company_name(df)
    print(df.head(2))
    print('formations')
    df, df_formations = expand_list_fields(df, 'formations')
    print(df_formations.head(5))
    print(df[['id', 'formations']].head(15))
