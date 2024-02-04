# pip install --upgrade googlet rans==4.0.0-rc1
import googletrans  # Import the googletrans module
from googletrans import Translator  # Import the Translator class from googletrans

# Get the list of available languages supported by Google Translate
available_languages = googletrans.LANGUAGES

# Create a Translator object to perform translations
translator = Translator()

# Prompt the user to enter the source language, destination language, and text to translate
source_language = input("Enter the language you want to translate from (e.g., English => en): ").strip().lower()
destination_language = input("Enter the language you want to translate to (e.g., French => fr): ").strip().lower()
text_to_translate = input("Enter the text you want to translate: ")

# Check if the source language is available for translation
if source_language not in available_languages:
    print(f"Error: {source_language} is not an available language")
    exit()

# Check if the destination language is available for translation
if destination_language not in available_languages:
    print(f"Error: {destination_language} is not an available language")
    exit()

# Perform the translation using the Translator object
translation = translator.translate(text_to_translate, src=source_language, dest=destination_language)

# Print the translated text
print(translation.text)






