# Translator-NLP

This repository provides a simple Python script that translates text from English to French using a pre-trained model from Hugging Face's transformers library. 
The script is easy to use and can be customized for different languages or text inputs.

#### Description
The script leverages the "Helsinki-NLP/opus-mt-en-fr" model, which is a machine translation model designed to translate English text into French. 
This model is part of the MarianMT family, known for its efficiency and accuracy in translation tasks.

The main functionality of the script is to take a piece of English text, process it through the model, and return the translated text in French. 
This can be particularly useful for anyone needing quick translations in applications, testing, or other projects where English-to-French translation is required.

#### Requirements
To run the script, you will need: 
- Python 3.6 or higher
- Hugging Face's transformers library
- PyTorch

These dependencies can be installed using pip (pip install transformers torch)

#### Usage
This script is configured to translate English text to French by default. After setting up the environment, you can run the script, and it will output the translated text alongside the original English text.

#### Example Output
The script translates a predefined English phrase and displays both the source and translated text. This provides a quick demonstration of the script's functionality and output format.

#### Customization
You can customize the text to be translated or even change the languages by adjusting the variables within the script. This makes the script versatile for various translation needs beyond just English to French.

#### License
This project is licensed under the MIT License, allowing you to use, modify, and distribute the code freely under the terms of the license.

#### Acknowledgments
The script uses the transformers library by Hugging Face, a leading tool for working with transformer models.
The translation model, "Helsinki-NLP/opus-mt-en-fr", is developed by the Helsinki-NLP group, known for their contributions to natural language processing.
