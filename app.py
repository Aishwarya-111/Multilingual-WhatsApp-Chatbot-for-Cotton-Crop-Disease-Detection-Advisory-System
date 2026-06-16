# ---------------------------------------------------------
# PROJECT: Multilingual AI WhatsApp Chatbot for Cotton Crop
# MAIN FILE: app.py
# ---------------------------------------------------------
# FILE ROLES:
# - app.py: Main Flask server & Twilio Webhook handler
# - data/disease_info.py: Multilingual advisory & Smart Query data
# - utils/predict.py: Model inference logic (MobileNetV2)
# - utils/gradcam.py: Grad-CAM Explainable AI logic
# - utils/language.py: User language preference management
# - test_webhook.py: Simulator for testing your bot locally
# ---------------------------------------------------------

import os
import static_ffmpeg
static_ffmpeg.add_paths()
from googletrans import Translator
import requests
from requests.auth import HTTPBasicAuth
import uuid
from pydub import AudioSegment
import speech_recognition as sr
from flask import Flask, request, send_from_directory, url_for
from twilio.twiml.messaging_response import MessagingResponse
# Import Master Advisory Data
from data.cotton_advisory import get_advisory, smart_queries, keyword_mapping

# --- TWILIO CREDENTIALS ---
# Paste your credentials from Twilio Console here if needed for secure media download
# (Optional for Sandbox, but recommended for Production)
import os

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

# Import project modules
from utils.predict import predict_disease, get_model
from utils.gradcam import generate_gradcam
from utils.language import (
    user_languages,
    get_user_language,
    set_user_language,
    reset_user_language,
    get_menu_text,
    get_confirmation_text
)
from utils.voice_utils import generate_voice_reply
# Data already imported above

app = Flask(__name__)

# Basic config
UPLOAD_FOLDER = os.path.join("static", "uploads")
VOICE_FOLDER = os.path.join("static", "voice")
VOICE_REPLY_FOLDER = os.path.join("static", "voice_replies")
GRADCAM_FOLDER = os.path.join("static", "gradcam_outputs")

for path in [UPLOAD_FOLDER, VOICE_FOLDER, VOICE_REPLY_FOLDER, GRADCAM_FOLDER]:
    if not os.path.exists(path):
        os.makedirs(path)

# Pre-load model to warm up
print("Loading model...")
get_model()
print("Model loaded successfully.")

@app.route("/static/<path:filename>")
def serve_static(filename):
    return send_from_directory("static", filename)

def classify_text_query(text, lang_code):
    """
    Classifies the text query into smart queries or disease-related.
    Uses translation to English for robust keyword matching (Google-powered).
    """
    orig_text = text.lower()
    
    # 1. Check for greeting/reset (Language agnostic)
    greetings = ["hi", "hello", "start", "restart", "नमस्ते", "హలో", "మీరు"]
    if any(greet in orig_text for greet in greetings):
        return "GREETING", None

    # 2. Translate to English for smarter internal processing
    try:
        translator = Translator()
        translated = translator.translate(orig_text, dest='en').text.lower()
    except:
        translated = orig_text # Fallback to original
    
    print(f"DEBUG: Internal Search (English): {translated}")

    # 3. Check for specific disease name matches (Smarter than generic guide)
    # Mapping specific keys to display names for dictionary lookup
    disease_keys = ["bacterial_blight", "curl_virus", "leaf_hopper_jassids", "leaf_reddening", "leaf_variegation"]
    
    for key in disease_keys:
        if any(kw in translated for kw in keyword_mapping[key]):
            # Get the actual advisory directly!
            return "ADVISORY", get_advisory(key, lang_code)

    # 4. Check for smart queries (farming advice)
    for key, keywords in keyword_mapping.items():
        if key in smart_queries["en"] and any(kw in translated for kw in keywords):
            return "SMART_QUERY", smart_queries[lang_code].get(key, smart_queries[lang_code]["default"])

    # 5. Check for generic disease Guide (asking for image)
    disease_keywords = ["disease", "problem", "spot", "leaf", "बीमारी", "रोग", "సమస్య", "ఆకు"]
    if any(kw in translated or kw in orig_text for kw in disease_keywords):
        guide = {
            "en": "I see you're asking about a disease. Please upload a clear image of the cotton leaf for accurate detection.",
            "hi": "मुझे लगता है कि आप किसी बीमारी के बारे में पूछ रहे हैं। कृपया सटीक पहचान के लिए कपास की पत्ती की एक साफ तस्वीर अपलोड करें।",
            "te": "మీరు వ్యాధి గురించి అడుగుతున్నట్లుగా కనిపిస్తోంది. ఖచ్చితమైన గుర్తింపు కోసం దయచేసి పత్తి ఆకు యొక్క స్పష్టమైన చిత్రాన్ని అప్‌లోడ్ చేయండి."
        }
        return "GUIDE_IMAGE", guide.get(lang_code, guide["en"])

    # 6. Fallback to generic smart advice
    return "UNKNOWN", smart_queries[lang_code]["default"]

@app.route("/api/v1/webhook", methods=["POST"])
def webhook():
    """
    Main webhook endpoint for Twilio WhatsApp.
    Handles Text, Image, and Voice inputs.
    """
    resp = MessagingResponse()
    msg = resp.message()
    
    try:
        incoming_msg = request.values.get("Body", "").strip()
        sender_phone = request.values.get("From", "")
        num_media = int(request.values.get("NumMedia", 0))
        media_type = request.values.get("MediaContentType0", "")

        # 1. HANDLE GREETINGS (Force reset)
        if any(greet in incoming_msg.lower() for greet in ["hi", "hello", "start", "restart"]):
            reset_user_language(sender_phone)
            msg.body(get_menu_text())
            return str(resp)

        # 2. HANDLE LANGUAGE SELECTION (if no language set)
        current_lang = get_user_language(sender_phone)
        
        # If user just sent 1, 2, or 3 and they haven't set language or want to change
        if incoming_msg in ["1", "2", "3"]:
            current_lang = set_user_language(sender_phone, incoming_msg)
            msg.body(get_confirmation_text(current_lang))
            return str(resp)

        # 3. HANDLE MEDIA (Images/Voice)
        if num_media > 0:
            media_url = request.values.get("MediaUrl0")
            print(f"DEBUG: Handling media from {media_url} (Type: {media_type})")
            
            # 3A. IMAGE HANDLING
            if "image" in media_type:
                try:
                    unique_id = str(uuid.uuid4())
                    img_path = os.path.join(UPLOAD_FOLDER, f"{unique_id}.jpg")
                    
                    print(f"DEBUG: Downloading image to {img_path}...")
                    auth = None
                    if (
                            TWILIO_ACCOUNT_SID
                            and TWILIO_AUTH_TOKEN
                            and TWILIO_ACCOUNT_SID.startswith("AC")
                        ):
                        auth = HTTPBasicAuth(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
                    
                    img_data = requests.get(media_url, auth=auth).content
                    with open(img_path, "wb") as f:
                        f.write(img_data)
                    
                    print("DEBUG: Image downloaded. Starting prediction...")
                    top_class, conf, top_2, is_reliable = predict_disease(img_path)
                    print(f"DEBUG: Prediction: {top_class} (Conf: {conf})")
                    
                    if not is_reliable:
                        err_msg = {
                            "en": "⚠️ Uncertain prediction. Please upload a clearer image.",
                            "hi": "⚠️ अनिश्चित भविष्यवाणी। कृपया एक साफ तस्वीर अपलोड करें।",
                            "te": "⚠️ అస్పష్టమైన గుర్తింపు. దయచేసి స్పష్టమైన చిత్రాన్ని అప్‌లోడ్ చేయండి."
                        }
                        msg.body(err_msg.get(current_lang, err_msg["en"]))
                        return str(resp)
                    
                    print("DEBUG: Fetching advisory...")
                    mapping = {
                        "herbicidegrowth_damage": "herbicide_growth_damage",
                        "leaf_reddning": "leaf_reddening"
                    }
                    advisor_key = mapping.get(top_class, top_class)
                    
                    # from data.cotton_advisory import get_advisory (already imported)
                    response_text = get_advisory(advisor_key, current_lang)
                    print(f"DEBUG: Advisory fetched: {response_text[:30]}...")
                    
                    msg.body(response_text)
                    
                    print("DEBUG: Generating Grad-CAM...")
                    model = get_model()
                    from utils.predict import class_names
                    class_index = class_names.index(top_class)
                    gradcam_filename = f"gradcam_{unique_id}.jpg"
                    gradcam_path = generate_gradcam(model, img_path, class_index, gradcam_filename)
                    print(f"DEBUG: Grad-CAM result: {gradcam_path}")
                    
                    if gradcam_path:
                        host = request.host_url
                        gradcam_url = f"{host}static/gradcam_outputs/{gradcam_filename}"
                        print(f"DEBUG: Sending Grad-CAM URL: {gradcam_url}")
                        msg.media(gradcam_url)
                    
                    return str(resp)
                except Exception as img_err:
                    print(f"DEBUG: Error inside image handler: {img_err}")
                    import traceback
                    print(traceback.format_exc())
                    raise img_err # Re-raise to be caught by main handler

            # 3B. VOICE HANDLING (NEW & IMPROVED)
            elif "audio" in media_type:
                unique_id = str(uuid.uuid4())
                ogg_path = os.path.join(VOICE_FOLDER, f"{unique_id}.ogg")
                wav_path = os.path.join(VOICE_FOLDER, f"{unique_id}.wav")
                
                # Download audio
                auth = None
                if (
                    TWILIO_ACCOUNT_SID
                    and TWILIO_AUTH_TOKEN
                    and TWILIO_ACCOUNT_SID.startswith("AC")
                ):
                    auth = HTTPBasicAuth(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
                
                audio_data = requests.get(media_url, auth=auth).content
                with open(ogg_path, "wb") as f:
                    f.write(audio_data)
                
                try:
                    # Convert to wav
                    audio = AudioSegment.from_ogg(ogg_path)
                    audio.export(wav_path, format="wav")
                    
                    # Speech to text
                    r = sr.Recognizer()
                    with sr.AudioFile(wav_path) as source:
                        audio_listened = r.record(source)
                        
                        # Use current language if set, else try all (Strict Multilingual Policy)
                        lang_map = {"en": "en-US", "hi": "hi-IN", "te": "te-IN"}
                        text = None
                        
                        # Logic: If user has explicitly selected a language, try that first.
                        # If no language selected or English (default), try ALL to see what matches best.
                        is_default_en = (current_lang == "en" and sender_phone not in user_languages)
                        langs_to_try = [current_lang] if not is_default_en else ["en", "hi", "te"]
                        
                        best_text = ""
                        detected_lcode = current_lang
                        
                        for lcode in langs_to_try:
                            try:
                                text = r.recognize_google(audio_listened, language=lang_map[lcode])
                                print(f"DEBUG: Voice match found in {lcode}: {text}")
                                best_text = text
                                detected_lcode = lcode
                                break # Stop at first successful match
                            except:
                                continue
                        
                        if not best_text:
                            # Final fallback
                            best_text = r.recognize_google(audio_listened, language="en-US")
                            detected_lcode = "en"
                        
                        current_lang = detected_lcode
                        incoming_msg = best_text
                        
                        # Auto-set the language preference based on detection
                        set_user_language(sender_phone, "1" if detected_lcode == "en" else ("2" if detected_lcode == "hi" else "3"))
                        
                        print(f"DEBUG: Voice Final: {incoming_msg} (Lang: {current_lang})")
                        
                        # Process query immediately to give voice reply
                        q_type, q_resp = classify_text_query(incoming_msg, current_lang)
                        
                        # Generate Voice Reply
                        reply_voice_filename = f"reply_{unique_id}.mp3"
                        reply_voice_path = os.path.join(VOICE_REPLY_FOLDER, reply_voice_filename)
                        
                        if generate_voice_reply(q_resp, current_lang, reply_voice_path):
                            host = request.host_url
                            voice_url = f"{host}static/voice_replies/{reply_voice_filename}"
                            print(f"DEBUG: Generated Voice Reply URL: {voice_url}")
                            msg.media(voice_url)
                        
                        msg.body(q_resp)
                        return str(resp)

                except Exception as e:
                    print(f"DEBUG: Voice processing error: {e}")
                    fail_msg = {
                        "en": "Could not understand audio. Please try again or send text.",
                        "hi": "ऑडियो समझ नहीं आया। कृपया पुनः प्रयास करें या टेक्स्ट भेजें।",
                        "te": "ఆడియో అర్థం కాలేదు. దయచేసి మళ్ళీ ప్రయత్నించండి లేదా టెక్స్ట్ పంపండి."
                    }
                    msg.body(fail_msg.get(current_lang, fail_msg["en"]))
                    return str(resp)

        # 4. HANDLE TEXT QUERY (incl. converted voice)
        if incoming_msg:
            # Auto-detect language for text query if it's long enough
            if len(incoming_msg) > 5:
                try:
                    from googletrans import Translator
                    translator = Translator()
                    detection = translator.detect(incoming_msg)
                    if detection.lang in ["hi", "te"]:
                        current_lang = set_user_language(sender_phone, "2" if detection.lang == "hi" else "3")
                except:
                    pass

            q_type, q_resp = classify_text_query(incoming_msg, current_lang)
            if q_type == "GREETING":
                reset_user_language(sender_phone)
                msg.body(get_menu_text())
            else:
                msg.body(q_resp)
            return str(resp)

        # FALLBACK for any other input
        fallback = {
            "en": "Sorry, I didn’t understand. Please try again or send 'hi' to restart.",
            "hi": "क्षमा करें, मुझे समझ नहीं आया। कृपया पुनः प्रयास करें या पुनः प्रारंभ करने के लिए 'hi' भेजें।",
            "te": "క్షమించండి, నాకు అర్థం కాలేదు. దయచేసి మళ్ళీ ప్రయత్నించండి లేదా రీస్టార్ట్ చేయడానికి 'hi' పంపండి."
        }
        msg.body(fallback.get(current_lang, fallback["en"]))
        return str(resp)

    except Exception as e:
        import traceback
        error_details = traceback.format_exc()
        print(f"--- SERVER ERROR LOG ---")
        print(error_details)
        print(f"------------------------")
        
        # Always return valid TwiML
        resp = MessagingResponse()
        resp.message("⚠️ An internal error occurred. Our team is looking into it. Please try again later.")
        return str(resp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
