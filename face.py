import streamlit as st
from brain import ask_cleopatra
from st_audiorec import st_audiorec
from voice import transcribe_audio

def main():
    st.set_page_config(page_title="Cleo", layout="wide")




    # Use st.markdown and some HTML/CSS to inject a simple background
    background_style = """
    <style>
    .stApp {
                background-image: url("https://vztidciyobdxmlhtdexk.supabase.co/storage/v1/object/public/cleo_image/cleo%20amazing(love).webp");
        background-color: #f5f5dc;  /* A light beige background, resembling parchment */
    }
    .stTextInput, .stTextArea, .stButton > button {
        background-color: #f8eedc;  /* A slightly darker shade for input boxes and button */
        border: 1px solid #e6d8b8;
        border-radius: 5px;
        padding: 5px;
    }
    .stTextInput > div > div > input, .stTextArea > div > textarea {
        color: #5C3D2E;  /* Dark brown text color for readability */
        font-family: 'Times New Roman', Times, serif;  /* Serif font for a classic look */
    }
    .stButton > button {
        color: white;
        background-color: #8b4513;  /* A darker brown for the button */
        font-family: 'Times New Roman', Times, serif;
    }
    /* Additional styles to adjust spacing and alignment */
    .stTextInput, .stTextArea {
        margin-bottom: 10px;  /* Add space between the widgets */
    }
    </style>
    """
    st.markdown(background_style, unsafe_allow_html=True)

    st.title("Cleo")

    # Field for entering a name
    name = st.text_input("Hello, what's your name?:", help="Type your name here")

    # Field for typing and speaking questions

    wav_audio_data = st_audiorec()
    question_from_audio = ""

    if wav_audio_data is not None:
        question_from_audio = transcribe_audio(wav_audio_data)
        print(question_from_audio)
        st.text_area("transcription", question_from_audio)

    if question_from_audio:
        question = question_from_audio
    else:
        question = st.text_input("Ask your question here", help="Type your question here")

    # A button to submit the question
    if st.button("Submit"):
        bot_response, audio_output = ask_cleopatra(user_question=question, user_name=name)
        # Display the answer in a styled text area
        st.text_area("Answer:", value=bot_response)
        with open(audio_output, 'rb') as audio_file:
            st.audio(audio_file, format='audio/mp3')

if __name__ == "__main__":
    main()
