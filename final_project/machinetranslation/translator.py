""" Uses IBM Watson to translate text from English to French and vice versa """

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
VERSION = "2018-05-01"

authenticator = IAMAuthenticator(f'{apikey}')
language_translator = LanguageTranslatorV3(
    version=f'{VERSION}',
    authenticator=authenticator
)

language_translator.set_service_url(f'{url}')


def english_to_french(english_text):
    """ Translates text from English to French """
    if english_text is None:
        return None
    result = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    french_text = result['translations'][0]['translation']
    return french_text


def french_to_english(french_text):
    """ Translates text from French to English """
    if french_text is None:
        return None
    result = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    english_text = result['translations'][0]['translation']
    return english_text
