import requests
import json
from dotenv import load_dotenv
import os


load_dotenv()
supabase_key = os.getenv("SUPABASE_KEY")


def add_user_question_and_answer(user_name, question, answer):
    url = 'https://vztidciyobdxmlhtdexk.supabase.co/rest/v1/cleo_data_trial'
    payload = {
        "name": user_name,
        "user_question": question,
        "gpt_answer": answer
    }
    headers = {
        "apikey": supabase_key,  # Replace with your actual Supabase Anon key
        "Authorization": f"Bearer {supabase_key}",  # Replace with your actual Supabase Anon key
        "Content-Type": "application/json",
        "Prefer": "return=minimal"
    }

    response = requests.post(url, data=json.dumps(payload), headers=headers)

    if response.status_code == 200 or response.status_code == 201:
        print("Data added successfully.")
    else:
        print(f"Failed to add data. Status code: {response.status_code}, Response: {response.text}")
