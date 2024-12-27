from openai import OpenAI
from config.params import OPENAI_KEY, get_chatgpt_answer_filename
from json import dump as json_dump

client = OpenAI(
  api_key= OPENAI_KEY
)

# TODO: I may want to extract with 4 prompts:
# - job title, language
# - education, certification
# - experience,
# - skills

def generate_prompt(prompt_path, text):
    with open(prompt_path, 'r') as f:
        prompt = f.read()
    prompt += f'\n\n{text}'

    return prompt

def generate_prompt_chat(prompt_path, text):
    with open(prompt_path, 'r') as f:
        prompt = f.read()
    # prompt += f'\n\n{text}'
    messages = [
        {
            "role": "system",
            "content": prompt,
        },
        {
            "role": "user",
            "content": f"Extract from the following text:\n\n{text}",
        },
    ]

    return messages

def extract_info(messages, folder_name, title):
    # Define a prompt for extracting skills and experience
    # prompt = f"Extract the skills, experience, job title, certifications from the following resume text in json format:\n\n{text}"

    print('Calling model')
    response = client.chat.completions.create(
        model="gpt-4o",  # Use GPT-4 for better performance
        # prompt=prompt,
        messages=messages,
        max_tokens=2500,  # Adjust token limit based on expected output size
        temperature=0.5  # Lower temperature for more factual responses
    )
    # print(response)
    output = response.choices[0].message.content.strip()
    response.model_dump_json(indent=2)

    with open(get_chatgpt_answer_filename(title, folder_name), 'w') as f:
        f.write(output)
    # try:
    #     with open(get_chatgpt_answer_filename_json(title), 'w') as f:
    #         json_dump(f, output)
    # except:
    #     print('Could not dump json')

    return output


if __name__=='__main__':
    from config.params import EDUCATION_PROMPT
    print(generate_prompt(EDUCATION_PROMPT, 'My resume'))
