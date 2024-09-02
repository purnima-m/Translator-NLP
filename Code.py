from transformers import MarianMTModel, MarianTokenizer

model_name = "Helsinki-NLP/opus-mt-en-fr"
model = MarianMTModel.from_pretrained(model_name)
tokenizer = MarianTokenizer.from_pretrained(model_name)

def translate_text(text, source_lang, target_lang):
    # Tokenize the input text
    input_ids = tokenizer.encode(text, return_tensors='pt', src_lang=source_lang)
    
    # Generate translation
    translated_ids = model.generate(input_ids=input_ids,
                                    decoder_start_token_id=model.config.pad_token_id,
                                    num_beams=4,
                                    max_length=128,
                                    early_stopping=True)
    
    # Decode the translated tokens
    translated_text = tokenizer.decode(translated_ids[0], skip_special_tokens=True, clean_up_tokenization_spaces=False)
    
    return translated_text

# Example usage
source_text = "I love coding"
source_language = "en"
target_language = "fr"

translated_text = translate_text(source_text, source_language, target_language)

print(f"Source text ({source_language}): {source_text}")
print(f"Translated text ({target_language}): {translated_text}")
