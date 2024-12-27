from src.parse_resume.pdf_parser import extract_pdf_text
from src.parse_resume.chatgpt import extract_info, generate_prompt_chat
from src.parse_resume.data_transformer import read_data
from src.parse_resume.db_connector import insert_resume
from config.params import (
    DEFAULT_RESUME_PATH, TITLE_PROMPT,
    EDUCATION_PROMPT, EXPERIENCE_PROMPT, SKILLS_PROMPT, RESUMES_COLLECTION
)
from pathlib import Path
from src.parse_resume.nlp import extract_entities

def main():
    # Parsing resume
    text = extract_pdf_text(DEFAULT_RESUME_PATH)
    path = Path('data/resume/')
    path.mkdir(exist_ok=True, parents=True)
    with open(f'{path}/extract.txt', 'w') as f:
        f.write(text)

    cv_key = 'v7'

    #Use NLP
    # print(extract_entities(text))

    # Using chatGPT to extract info, BIG FAILURE
    for prompt, name in [
        (TITLE_PROMPT, 'title'),
        (EDUCATION_PROMPT, 'education'),
        (EXPERIENCE_PROMPT, 'experience'),
        (SKILLS_PROMPT, 'skills')
    ]:
        messages = generate_prompt_chat(prompt, text)
        # print(messages)
        output = extract_info(messages, cv_key, name)


    output = read_data(cv_key)

    insert_resume(RESUMES_COLLECTION, output, cv_key)


if __name__=='__main__':
    main()
