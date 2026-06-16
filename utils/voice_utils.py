# Voice Processing Utility (Text-to-Speech)
from gtts import gTTS
import os

def generate_voice_reply(text, lang_code, output_path):
    """
    Converts text to speech and saves it as an MP3 file.
    
    Args:
        text (str): The response text to convert.
        lang_code (str): The language code ('en', 'hi', 'te').
        output_path (str): Full path where the MP3 should be saved.
        
    Returns:
        bool: True if successful, False otherwise.
    """
    try:
        # Mapping our internal lang codes to gTTS codes
        # gTTS uses 'en' for English, 'hi' for Hindi, 'te' for Telugu
        tts = gTTS(text=text, lang=lang_code, slow=False)
        tts.save(output_path)
        return True
    except Exception as e:
        print(f"Error generating voice reply: {e}")
        return False
