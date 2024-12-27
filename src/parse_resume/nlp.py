import spacy

# Load pre-trained spaCy model
nlp = spacy.load("en_core_web_sm")

def extract_entities(text):
    doc = nlp(text)
    entities = {"names": [], "job_titles": [], "skills": []}
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            entities["names"].append(ent.text)
        elif ent.label_ == "ORG":
            entities["job_titles"].append(ent.text)
    return entities
