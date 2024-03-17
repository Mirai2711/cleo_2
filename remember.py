import requests
from dotenv import load_dotenv
import os


load_dotenv()

supabase_key = os.getenv("SUPABASE_KEY")


def fetch_user_data(user_name):
    user_name = user_name.lower()
    # Endpoint with query parameters for fetching data based on user name
    url = f'https://vztidciyobdxmlhtdexk.supabase.co/rest/v1/cleo_data_trial?name=eq.{user_name}&select=user_question,gpt_answer'

    # Your Supabase API keys (use your actual Anon key here)
    headers = {
        "apikey": supabase_key,
        "Authorization": f"Bearer {supabase_key}",
        "Range": "0-9"  # Adjust the range if you expect more results
    }

    # Make the GET request
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Return the JSON response if successful
        return response.json()
    else:
        # Return an error message if the request failed
        return f"Failed to fetch data: {response.status_code}"

