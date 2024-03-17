from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

client = OpenAI()



def text_to_speech(text, file_name="speech.mp3"):
    # Define the path for the audio file relative to this script's location
    speech_file_path = Path(__file__).parent / file_name

    # Use the OpenAI API to create speech audio from text
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text
    )
    # Stream the audio response to the file
    response.stream_to_file(str(speech_file_path))

    return speech_file_path


def transcribe_audio(audio_data):
    temp_file_path = Path("temp_audio.wav")
    with open(temp_file_path, "wb") as f:
        f.write(audio_data)

    # Open the temporary audio file in binary read mode
    with open(temp_file_path, "rb") as audio_file:
        # Call the OpenAI API to transcribe the audio file
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )

    # Delete the temporary file
    temp_file_path.unlink()

    transcription = transcription.text
    return transcription
