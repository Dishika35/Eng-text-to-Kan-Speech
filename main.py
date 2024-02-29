from googletrans import Translator
from gtts import gTTS
import os

# Function to translate English text to Kannada
def translate_to_kannada(english_text):
    translator = Translator()
    translation = translator.translate(english_text, src='en', dest='kn')
    return translation.text

# Function to convert Kannada text to speech
def text_to_speech(kannada_text):
    tts = gTTS(text=kannada_text, lang='kn')
    tts.save("output.mp3")
    os.system("start output.mp3")

# Main function
if __name__ == "__main__":
    english_text = input("Enter the English text: ")
    kannada_text = translate_to_kannada(english_text)
    print("Translated Kannada text:", kannada_text)
    text_to_speech(kannada_text)
