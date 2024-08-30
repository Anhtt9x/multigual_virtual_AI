import speech_recognition as sr
import google.generativeai as genai
from gtts import gTTS
import os 
from dotenv import load_dotenv

load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")
os.environ['GOOGLE_API_KEY']= google_api_key


def voice_input():
    r=sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)
    
    try:
        text = r.recognize_google_cloud(audio)
        print("You said: ",text)
        return text
    
    except sr.UnknownValueError:
        print("Sorry, could not understand the audio")
    
    except sr.RequestError as e:
        print(f"Could not request result from google {e}")


def llm_model(user_text):
    genai.configure(api_key=google_api_key)

    model =genai.GenerativeModel(model_name="gemini-1.5-pro")

    result = model.generate_content(user_text).text

    return result


def text_to_speech(text):
    tts = gTTS(text=text,lang="vi")

    tts.save("speech.mp3")