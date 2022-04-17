import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# authenticate
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

# en-fr translate
def english_to_french(english_text):
    if english_text is None:
        print("Input must not be null")
        return None
    french_text = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    return french_text

# fr-en translate
def french_to_english(french_text):
    if french_text is None:
        print("Input must not be null")
        return None
    english_text = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    return english_text