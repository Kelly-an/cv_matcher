import pandas as pd
from json import loads as json_loads
from config.params import get_chatgpt_answer_filename

def get_df_from_data(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()

    # Step 2: Remove the first and last lines (e.g., ```json and ```)
    cleaned_lines = lines[1:-1]  # Exclude the first and last lines
    cleaned_json = "".join(cleaned_lines)  # Combine the lines into a single string

    # Step 3: Parse the JSON
    data = json_loads(cleaned_json)
    return pd.DataFrame(data)

def read_data(folderpath, date=None):
    # ensure filepath is for a json
    output = {
        "id": folderpath,
    }
    for file in ['title', 'skills', 'experience', 'education']:
        if date is not None:
            file_name = get_chatgpt_answer_filename(file, folderpath, date)
        else:
            file_name = get_chatgpt_answer_filename(file, folderpath)
        print(file_name)
        df = get_df_from_data(file_name)
        if file == 'title':
            output["job_title"] = df["job_title"].iloc[0]
            output["languages"] = df['languages'].to_list()
        if file == 'experience':
            output["experience"] = df['experience'].to_list()
        if file == 'skills':
            output["skills"] = df['skills'].to_list()
        if file == 'education':
            output["education"] = df['education'].to_list()
            output["certification"] = df['certifications'].to_list()

    return output


if __name__ == '__main__':
    output = read_data('v7', date='2024-12-05')
    print(output)
