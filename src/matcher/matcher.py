import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import spacy
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load spaCy model for NLP
nlp = spacy.load("en_core_web_sm")

# Sample DataFrame for job offers and resumes
offers = pd.DataFrame([
    {
        "job_title": "Data Scientist",
        "skills_required": ["Python", "Machine Learning", "Data Analysis", "SQL"],
        "languages": ["English", "French"],
        "education_required": ["Bachelor's in Computer Science"],
        "certifications_required": ["AWS Certified Machine Learning"],
        "job_type": "Full-time",
        "salary_range": "€40,000 - €60,000"
    },
    {
        "job_title": "Data Analyst",
        "skills_required": ["SQL", "Data Analysis", "Excel", "R"],
        "languages": ["English"],
        "education_required": ["Bachelor's in Data Science"],
        "certifications_required": ["Google Data Analytics"],
        "job_type": "Full-time",
        "salary_range": "€35,000 - €50,000"
    }
])

resume = {
    "job_title": "Data Scientist",
    "skills": ["Python", "SQL", "Machine Learning"],
    "languages": ["English", "Spanish"],
    "education": ["Bachelor's in Computer Science"],
    "certifications": ["AWS Certified Machine Learning"]
}

# Function to calculate fuzzy matching score between two lists of strings
def fuzzy_match_lists(list1, list2):
    score = 0
    for item in list1:
        matches = process.extract(item, list2, scorer=fuzz.partial_ratio)
        score += max([match[1] for match in matches])  # take the best match score
    return score

# Function to calculate semantic similarity using spaCy embeddings
def semantic_similarity(list1, list2):
    # Convert text to spaCy docs
    doc1 = nlp(" ".join(list1))
    doc2 = nlp(" ".join(list2))

    # Calculate cosine similarity of the embeddings
    return doc1.similarity(doc2)

# Function to match resume with job offers
def match_job_offer_advanced(resume, job_offer):
    score = 0
    max_score = 0

    # Match Job Title (Fuzzy Matching and Semantic Similarity)
    job_title_score = fuzzy_match_lists([resume["job_title"]], [job_offer["job_title"]])
    score += job_title_score
    max_score += 100  # We assume a job title match can give us up to 100 points

    # Match Skills (Fuzzy Matching + Semantic Similarity)
    skills_score = fuzzy_match_lists(resume["skills"], job_offer["skills_required"])
    skills_similarity = semantic_similarity(resume["skills"], job_offer["skills_required"])
    score += skills_score * 0.5 + skills_similarity * 0.5
    max_score += len(job_offer["skills_required"]) * 10  # Adjusted for the number of skills

    # Match Languages
    language_score = fuzzy_match_lists(resume["languages"], job_offer["languages"])
    score += language_score * 2  # Give more weight to language matching
    max_score += len(job_offer["languages"]) * 5  # Weight based on number of required languages

    # Match Education
    education_score = fuzzy_match_lists(resume["education"], job_offer["education_required"])
    score += education_score * 2
    max_score += len(job_offer["education_required"]) * 5

    # Match Certifications
    certifications_score = fuzzy_match_lists(resume["certifications"], job_offer["certifications_required"])
    score += certifications_score * 3
    max_score += len(job_offer["certifications_required"]) * 5

    # Normalize score
    return round((score / max_score) * 100, 2) if max_score > 0 else 0

# Calculate the match score for each job offer
job_offer_scores = offers.apply(lambda job_offer: match_job_offer_advanced(resume, job_offer), axis=1)

# Add the match score to the offers DataFrame
offers['match_score'] = job_offer_scores

# Display the result
print(offers[['job_title', 'match_score']])
