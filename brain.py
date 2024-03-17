from openai import OpenAI
from dotenv import load_dotenv
from memory import add_user_question_and_answer
from remember import fetch_user_data
from voice import text_to_speech
load_dotenv()

client = OpenAI()

def ask_cleopatra(user_question, user_name):


    message_history_from_supabase = fetch_user_data(user_name)
    print(message_history_from_supabase)


    gpt_format_history = convert_context_to_gpt_format(message_history_from_supabase)

    system_message = "You are a famous personality. First, ask the user who you should be and then answer question as that person. Respond as if you are talking to a 7 year old"
    system_message = {'role': 'system', 'content': system_message}
    user_question = {'role': 'user', 'content': user_question}



    messages = [system_message]+gpt_format_history+[user_question]

    print(messages)




    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=1,
        max_tokens=150,
    )

    bot_response = response.choices[0].message.content
    print (bot_response)
    user_name = user_name.lower()

    add_user_question_and_answer(user_name, user_question, bot_response)

    voice_response = text_to_speech(bot_response)

    return bot_response, voice_response


def convert_context_to_gpt_format(context_history):
    gpt_formatted_messages = []

    # Iterate through each entry in the context history
    for entry in context_history:
        # Convert the user question part
        user_message = {
            "role": "user",
            "content": entry['user_question']
        }
        gpt_formatted_messages.append(user_message)

        # Convert the GPT answer part
        gpt_message = {
            "role": "assistant",
            "content": entry['gpt_answer']
        }
        gpt_formatted_messages.append(gpt_message)

    return gpt_formatted_messages
