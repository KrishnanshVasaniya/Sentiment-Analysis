import os
from datetime import datetime
from gtts import gTTS
from langdetect import detect
from transformers import pipeline

# Initialize the sentiment analysis pipeline with a pre-trained model
sentiment_analyzer = pipeline("sentiment-analysis")

# Responses dictionary for multilingual support
response_dict = {
    'en': {"POSITIVE": "I'm glad to hear that! Keep it up!",
           "NEGATIVE": "I'm sorry to hear that. I hope things get better soon.",
           "NEUTRAL": "Thank you for sharing that."},
    'fr': {"POSITIVE": "Je suis heureux de l'apprendre ! Continuez comme ça !",
           "NEGATIVE": "Je suis désolé d'entendre cela. J'espère que ça ira mieux bientôt.",
           "NEUTRAL": "Merci de partager cela."},
    'es': {"POSITIVE": "¡Me alegra escuchar eso! ¡Sigue así!",
           "NEGATIVE": "Lamento escuchar eso. Espero que las cosas mejoren pronto.",
           "NEUTRAL": "Gracias por compartir eso."},
}

# Function to detect language
def detect_language(text):
    try:
        lang = detect(text)
        return lang if lang in response_dict else 'en'
    except Exception:
        return 'en'

# Function to play audio response
def play_audio_response(response_text, language):
    tts = gTTS(text=response_text, lang=language)
    tts.save("response.mp3")
    os.system("mpg321 response.mp3 -quiet")

# Function to play date and accuracy audio
def play_additional_audio(text, language):
    tts = gTTS(text=text, lang=language)
    tts.save("additional_response.mp3")
    os.system("mpg321 additional_response.mp3 -quiet")

# Main function
def main():
    # User input
    text = input("Please enter a text for sentiment analysis: ")

    # Language detection
    language = detect_language(text)

    # Sentiment analysis using the pre-trained model
    result = sentiment_analyzer(text)
    sentiment = result[0]['label']  # POSITIVE, NEGATIVE, or NEUTRAL
    confidence = result[0]['score']

    # Prepare responses
    response_text = response_dict[language].get(sentiment, "Thank you for sharing that.")
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Print outputs
    print(f"Sentiment Detected: {sentiment}")
    print(f"Response: {response_text}")
    print(f"The current date is {current_date}.")
    print(f"The sentiment confidence is {confidence:.2f}.")

    # Play audio responses
    play_audio_response(response_text, language)
    play_additional_audio(f"The current date is {current_date}.", language)
    play_additional_audio(f"The sentiment confidence is {confidence:.2f}.", language)

if __name__ == "__main__":
    main()

