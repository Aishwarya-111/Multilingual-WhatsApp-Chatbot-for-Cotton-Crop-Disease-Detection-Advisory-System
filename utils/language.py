# Language Management Utility

# In-memory dictionary to store user language preference temporarily
# Key: WhatsApp Phone Number, Value: Language Code ('en', 'hi', 'te')
user_languages = {}

def set_user_language(phone_number, choice):
    """
    Sets the user's language preference based on their choice (1, 2, or 3).
    """
    mapping = {
        "1": "en",
        "2": "hi",
        "3": "te"
    }
    lang_code = mapping.get(str(choice), "en")
    user_languages[phone_number] = lang_code
    return lang_code

def get_user_language(phone_number):
    """
    Returns the user's preferred language code. Defaults to 'en'.
    """
    return user_languages.get(phone_number, "en")

def reset_user_language(phone_number):
    """
    Removes the user's language preference.
    """
    if phone_number in user_languages:
        del user_languages[phone_number]

def get_menu_text():
    """
    Returns the language selection menu.
    """
    return (
        "🌿 *Cotton Crop Advisory Bot* 🌿\n"
        "Welcome Farmer! Please choose your language:\n"
        "1️⃣ English\n"
        "2️⃣ हिन्दी (Hindi)\n"
        "3️⃣ తెలుగు (Telugu)"
    )

def get_confirmation_text(lang_code):
    """
    Returns a confirmation message in the selected language.
    """
    confirmations = {
        "en": "✅ Language selected successfully. Please send a cotton leaf image or ask your query.",
        "hi": "✅ भाषा का चयन सफलतापूर्वक हो गया। कृपया कपास की पत्ती की तस्वीर भेजें या अपना प्रश्न पूछें।",
        "te": "✅ భాష విజయవంతంగా ఎంపిక చేయబడింది. దయచేసి పత్తి ఆకు చిత్రాన్ని పంపండి లేదా మీ ప్రశ్నను అడగండి."
    }
    return confirmations.get(lang_code, confirmations["en"])
