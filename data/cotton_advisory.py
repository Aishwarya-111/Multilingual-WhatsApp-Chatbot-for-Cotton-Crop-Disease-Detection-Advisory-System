# ---------------------------------------------------------
# PROJECT: Multilingual AI WhatsApp Chatbot for Cotton Crop
# DATA MODULE: cotton_advisory.py
# ROLE: Master dictionary for all multilingual responses
# ---------------------------------------------------------

# 1. DETAILED ADVISORY (For prediction results)
advisory = {
    "bacterial_blight": {
        "en": """🌿 *Bacterial Blight Detected*

*Symptoms:*
• Angular, water-soaked spots on leaves that turn brown or black.
• Black lesions on stems (Black arm stage).
• Water-soaked spots on bolls that can cause rot.

*Recommendations:*
• Spray Copper Oxychloride (3.0g/L) mixed with Streptocycline (0.1g/L).
• Remove and destroy infected plant debris.
• Avoid overhead irrigation to reduce moisture on leaves.
• Use certified, acid-delinted seeds for next season.""",

        "hi": """🌿 *बैक्टीरियल ब्लाइट (Bacterial Blight) पाया गया*

*लक्षण:*
• पत्तियों पर कोणीय, पानी से लथपथ धब्बे जो भूरे या काले हो जाते हैं।
• तनों पर काले घाव (ब्लैक आर्म चरण)।
• बॉल्स (डोरों) पर पानी से लथपथ धब्बे जो सड़न पैदा कर सकते हैं।

*उपाय:*
• कॉपर ऑक्सीक्लोराइड (3.0 ग्राम/लीटर) और स्ट्रेप्टोसाइक्लिन (0.1 ग्राम/लीटर) के मिश्रण का छिड़काव करें।
• संक्रमित पौधों के अवशेषों को हटा दें और नष्ट कर दें।
• पत्तियों पर नमी कम करने के लिए ओवरहेड सिंचाई से बचें।
• किसान अगली फसल के लिए प्रमाणित बीजों का उपयोग करें।""",

        "te": """🌿 *బ్యాక్టీరియల్ బ్లైట్ (Bacterial Blight) గుర్తించబడింది*

*లక్షణాలు:*
• ఆకులపై కోణీయ, నీటితో నిండిన మచ్చలు ఏర్పడి క్రమంగా గోధుమ లేదా నలుపు రంగులోకి మారుతాయి.
• కాండం మీద నల్లటి మచ్చలు (బ్లాక్ ఆర్మ్ స్టేజ్).
• కాయల మీద నీటి మచ్చలు ఏర్పడి కుళ్లిపోయే అవకాశం ఉంది.

*పరిష్కారాలు:*
• కాపర్ ఆక్సిక్లోరైడ్ (3.0 గ్రా/లీ) మరియు స్ట్రెప్టోసైక్లిన్ (0.1 గ్రా/లీ) కలిపి పిచికారీ చేయండి.
• సోకిన మొక్క భాగాలను తొలగించి కాల్చివేయండి.
• ఆకులపై తేమ తగ్గించడానికి పైనుండి నీరు పోయడం (Overhead irrigation) ఆపండి."""
    },

    "curl_virus": {
        "en": """🌿 *Cotton Leaf Curl Virus (CLCuV) Detected*

*Symptoms:*
• Upward or downward curling of leaf margins.
• Thickening of leaf veins.
• Stunted plant growth and reduced boll formation.

*Recommendations:*
• Control Whiteflies (the carriers) using Neem oil (5ml/L) or recommended insecticides like Imidacloprid.
• Remove and destroy infected 'Sida' and other weed hosts nearby.
• Use virus-resistant cotton hybrids.
• Avoid excessive nitrogenous fertilizers.""",

        "hi": """🌿 *लीफ कर्ल वायरस (Leaf Curl Virus) पाया गया*

*लक्षण:*
• पत्तियों के किनारों का ऊपर या नीचे की ओर मुड़ना।
• पत्ती की शिराओं (veins) का मोटा होना।
• पौधों की वृद्धि रुकना और बॉल्स (डोरों) का कम बनना।

*उपाय:*
• नीम के तेल (5 मिली/लीटर) या अनुशंसित कीटनाशकों (जैसे इमिडाक्लोप्रिड) का उपयोग करके सफेद मक्खियों को नियंत्रित करें।
• आस-पास के संक्रमित खरपतवारों को हटा दें और नष्ट कर दें।
• वायरस-प्रतिरोधी कपास संकरों (hybrids) का उपयोग करें।""",

        "te": """🌿 *ఆకు ముడత వైరస్ (Leaf Curl Virus) గుర్తించబడింది*

*లక్షణాలు:*
• ఆకుల అంచులు పైకి లేదా కిందికి ముడుచుకుపోతాయి.
• ఆకు ఈనెలు లావుగా మారుతాయి.
• మొక్క ఎదుగుదల ఆగిపోతుంది మరియు కాయలు తక్కువగా వస్తాయి.

*పరిష్కారాలు:*
• తెల్ల దోమను (వైరస్ వాహకం) నివారించడానికి వేప నూనె (5ml/L) లేదా ఇమిడాక్లోప్రిడ్ వంటి పురుగుమందులు వాడండి.
• సోకిన మొక్కలను మరియు పొలం గట్లపై ఉన్న కలుపు మొక్కలను తొలగించండి."""
    },

    "healthy_leaf": {
        "en": """✨ *Your Cotton Crop Looks Healthy!*

*Maintenance Tips:*
• Ensure balanced application of NPK fertilizers.
• Monitor the field every 3-4 days for early signs of pests.
• Maintain proper spacing between plants for good aeration.
• Provide irrigation at critical stages especially flowering and boll development.""",

        "hi": """✨ *आपकी कपास की फसल स्वस्थ दिख रही है!*

*रखरखाव के सुझाव:*
• NPK उर्वरकों का संतुलित उपयोग सुनिश्चित करें।
• कीटों के शुरुआती लक्षणों के लिए हर 3-4 दिनों में खेत की निगरानी करें।
• अच्छी हवा के लिए पौधों के बीच उचित दूरी बनाए रखें।
• मुख्य चरणों (विशेष रूप से फूल आने और डोडो के विकास) पर सिंचाई प्रदान करें।""",

        "te": """✨ *మీ పత్తి పంట ఆరోగ్యంగా ఉంది!*

*సూచనలు:*
• ఎరువులను (NPK) సమతుల్యంగా వాడండి.
• చీడపీడల గుర్తింపు కోసం ప్రతి 3-4 రోజులకు ఒకసారి పొలాన్ని గమనిండి.
• మొక్కల మధ్య తగినంత గాలి ప్రసరణ ఉండేలా చూసుకోండి.
• పూత మరియు కాయ దశలలో నీటి తడులు తప్పనిసరిగా ఇవ్వండి."""
    },

    "herbicide_growth_damage": {
        "en": """🌿 *Herbicide Damage Detected*

*Symptoms:*
• Distorted, narrow, or 'strappy' leaves.
• Chlorosis (yellowing) or necrosis of leaf tissues.
• Abnormal growth patterns not caused by pests.

*Recommendations:*
• Stop herbicide application immediately.
• Flush the field with light irrigation to dilute herbicide residue.
• Apply a light dose of Urea or growth promoters to help the plant recover.
• Ensure spray equipment is thoroughly cleaned before use.""",

        "hi": """🌿 *हर्बिसाइड (कीटनाशक) क्षति पाई गई*

*लक्षण:*
• विकृत, संकीर्ण या पट्टी जैसी पत्तियां।
• पत्ती के ऊतकों का पीला पड़ना या सूखना।
• कीटों के बिना भी असामान्य विकास पैटर्न।

*उपाय:*
• हर्बिसाइड का प्रयोग तुरंत बंद कर दें।
• अवशेषों को कम करने के लिए खेत में हल्की सिंचाई करें।
• पौधों को तेजी से ठीक होने में मदद करने के लिए यूरिया की हल्की खुराक दें।""",

        "te": """🌿 *కలుపు మందుల నష్టం (Herbicide Damage) గుర్తించబడింది*

*లక్షణాలు:*
• ఆకులు వంకర్లు తిరిగి, సన్నగా మారిపోతాయి.
• ఆకులు పసుపు రంగులోకి మారడం లేదా ఎండిపోవడం.

*పరిష్కారాలు:*
• కలుపు మందుల వాడకాన్ని వెంటనే ఆపండి.
• భూమిలో మందు సాంద్రత తగ్గించడానికి పొలానికి నీరు పెట్టండి.
• మొక్క త్వరగా కోలుకోవడానికి తక్కువ మోతాదులో యూరియా వాడండి."""
    },

    "leaf_hopper_jassids": {
        "en": """🌿 *Leaf Hopper / Jassid Attack Detected*

*Symptoms:*
• Leaves turn pale yellow and then brownish-red at the edges (Hopper burn).
• Downward curling of leaves.
• Stunted growth and presence of small, greenish insects under the leaves.

*Recommendations:*
• Spray Imidacloprid (0.5ml/L) or Acetamiprid (0.2g/L).
• Use yellow sticky traps (10-12 per acre) to monitor and capture adults.
• Avoid excessive use of Nitrogen as it attracts these pests.""",

        "hi": """🌿 *लीफ हॉपर / जैसीड (Jassid) का हमला पाया गया*

*लक्षण:*
• पत्तियां पहले हल्की पीली और फिर किनारों से भूरी-लाल हो जाती हैं।
• पत्तियों का नीचे की ओर मुड़ना।
• पत्तियों के नीचे छोटे, हरे रंग के कीड़े दिखाई देते हैं।

*उपाय:*
• इमिडाक्लोप्रिड (0.5 मिली/लीटर) या एसिटामिप्रिड (0.2 ग्राम/लीटर) का छिड़काव करें।
• कीटों की निगरानी के लिए पीले चिपचिपे जाल (Yellow sticky traps) लगाएं।""",

        "te": """🌿 *పచ్చ దీపపు పురుగు (Leaf Hopper/Jassids) గుర్తించబడింది*

*లక్షణాలు:*
• ఆకులు పసుపు రంగులోకి మారి, అంచులు ఎర్రబడతాయి.
• ఆకులు కిందికి ముడుచుకుపోతాయి.
• ఆకుల వెనుక భాగంలో చిన్న ఆకుపచ్చ పురుగులు కనిపిస్తాయి.

*పరిష్కారాలు:*
• ఇమిడాక్లోప్రిడ్ (0.5ml/L) లేదా ఎసిటామిప్రిడ్ (0.2g/L) పిచికారీ చేయండి.
• పసుపు జిగురు అట్టలను (Yellow sticky traps) ఎకరాకు 10-12 వరకు ఏర్పాటు చేయండి."""
    },

    "leaf_reddening": {
        "en": """🌿 *Leaf Reddening Detected*

*Symptoms:*
• Reddish coloration starting from older leaves.
• Often occurs due to Magnesium or Nitrogen deficiency or cold stress.
• Premature aging of the plant.

*Recommendations:*
• Spray 2% Magnesium Sulphate (MgSO4) and 1% Urea.
• Ensure proper soil moisture and avoid waterlogging.
• Add well-decomposed manure or compost to improve soil health.""",

        "hi": """🌿 *पत्तियों का लाल होना पाया गया*

*लक्षण:*
• पुरानी पत्तियों से शुरू होने वाला लाल रंग।
• अक्सर मैग्नीशियम या नाइट्रोजन की कमी या ठंड के कारण होता है।
• पौधे का समय से पहले बूढ़ा होना।

*उपाय:*
• 2% मैग्नीशियम सल्फेट (MgSO4) और 1% यूरिया का छिड़काव करें।
• उचित मिट्टी की नमी सुनिश्चित करें और जलभराव से बचें।
• मिट्टी के स्वास्थ्य में सुधार के लिए अच्छी तरह सड़ी हुई खाद डालें।""",

        "te": """🌿 *ఆకు ఎర్రబడటం (Leaf Reddening) గుర్తించబడింది*

*లక్షణాలు:*
• పాత ఆకులు ఎరుపు రంగులోకి మారుతాయి.
• మెగ్నీషియం లేదా నత్రజని లోపం వల్ల ఇది జరుగుతుంది.

*పరిష్కారాలు:*
• 2% మెగ్నీషియం సల్ఫేట్ మరియు 1% యూరియా కలిపి పిచికారీ చేయండి.
• పొలంలో నీరు నిల్వ ఉండకుండా చూసుకోండి.
• పశువుల ఎరువును భూమిలో వేయండి."""
    },

    "leaf_variegation": {
        "en": """🌿 *Leaf Variegation Detected*

*Symptoms:*
• Irregular green and white/yellow patches on leaves.
• Can be genetic or caused by micronutrient deficiencies like Zinc.
• Usually not a major disease unless affecting a large area.

*Recommendations:*
• Spray Zinc Sulphate (2.0g/L) if deficiency is suspected.
• Monitor the speed of spread; if it's slow, it might be genetic.
• Ensure balanced micronutrient application.""",

        "hi": """🌿 *पत्तियों में चितकबरापन (Variegation) पाया गया*

*लक्षण:*
• पत्तियों पर अनियमित हरे और सफेद/पीले धब्बे।
• यह आनुवंशिक (genetic) या सूक्ष्म पोषक तत्वों (जैसे जिंक) की कमी के कारण हो सकता है।

*उपाय:*
• यदि कमी का संदेह हो, तो जिंक सल्फेट (2.0 ग्राम/लीटर) का छिड़काव करें।
• संतुलित सूक्ष्म पोषक तत्वों का उपयोग सुनिश्चित करें।""",

        "te": """🌿 *ఆకు వైవిధ్యం (Leaf Variegation) గుర్తించబడింది*

*లక్షణాలు:*
• ఆకులపై అక్కడక్కడా తెలుపు లేదా పసుపు రంగు మచ్చలు.
• ఇది వంశపారంపర్యంగా లేదా జింక్ లోపం వల్ల రావచ్చు.

*పరిష్కారాలు:*
• జింక్ సల్ఫేట్ (2.0 గ్రా/లీ) పిచికారీ చేయండి.
• మొక్కకు అవసరమైన సూక్ష్మ పోషకాలను అందించండి."""
    }
}

# 2. SMART QUERIES (General advice & FAQs)
smart_queries = {
    "en": {
        "fertilizer": "Use NPK fertilizers in balanced amounts. For nitrogen boost, apply Urea. Zinc or Magnesium deficiency may need specific sprays.",
        "growth": "Ensure proper irrigation at flowering and boll stages. Avoid waterlogging.",
        "pests": "Monitor your field every few days. Use neem oil for minor pests or specific insecticides for major attacks.",
        "water": "Cotton needs regular water but cannot stand waterlogging. Ensure good drainage.",
        "medicine_source": "📍 *Where & How to buy:* You can purchase these medicines from local agricultural cooperatives (PACS), authorized pesticide dealers, or government-run agriculture extension centers (Raithu Bharosa Kendras).\n\n📝 *Acquisition Process:* Take a clear photo of the infected leaf to your local center or dealer. Show it to an agricultural official or authorized expert for verification. They will confirm the diagnosis and provide the exact medicine or a prescription for local purchase.",
        "application_process": "📝 *How to apply:* Use the exact dosage mentioned. Always wear protective gear (gloves/mask) while spraying. Spray during early morning (6-9 AM) or late evening (5-7 PM) for best results and to keep beneficial insects safe.",
        "default": "Please upload a leaf image or ask a more specific cotton-related query."
    },
    "hi": {
        "fertilizer": "NPK उर्वरकों का संतुलित उपयोग करें। यूरिया का उपयोग नाइट्रोजन की कमी पूरी करने के लिए करें।",
        "growth": "फूल आने और डोडो के विकास के समय सही सिंचाई सुनिश्चित करें।",
        "pests": "खेत की नियमित निगरानी करें। छोटे कीटों के लिए नीम तेल का प्रयोग करें।",
        "water": "कपास को नियमित पानी चाहिए पर जलभराव नहीं होना चाहिए।",
        "medicine_source": "📍 *कहां और कैसे खरीदें:* आप ये दवाएं स्थानीय कृषि सहकारी समितियों (PACS), अधिकृत कीटनाशक विक्रेताओं या सरकारी कृषि विस्तार केंद्रों से खरीद सकते हैं।\n\n📝 *खरीदने की प्रक्रिया:* अपनी फसल की संक्रमित पत्ती की फोटो स्थानीय कृषि केंद्र या विक्रेता को दिखाएं। कृषि अधिकारी या विशेषज्ञ इसे देखकर दवा की पुष्टि करेंगे और आपको सही दवा या स्थानीय विक्रेता के लिए पर्ची देंगे।",
        "application_process": "📝 *उपयोग कैसे करें:* बताई गई सही खुराक का उपयोग करें। छिड़काव करते समय हमेशा दस्ताने और मास्क पहनें। सर्वोत्तम परिणामों के लिए सुबह जल्दी (6-9) या देर शाम (5-7) को छिड़काव करें।",
        "default": "कृपया एक पत्ती की तस्वीर अपलोड करें या कपास से संबंधित प्रश्न पूछें।"
    },
    "te": {
        "fertilizer": "NPK ఎరువులను సమతుల్యంగా వాడండి। నత్రజని కోసం యూరియా వాడండి।",
        "growth": "పూత మరియు కాయ దశలలో నీటి తడులు తప్పనిసరిగా ఇవ్వండి।",
        "pests": "చీడపీడల కోసం పొలాన్ని గమనిస్తూ ఉండండి। వేప నూనె లేదా పురుగుమందులు వాడండి।",
        "water": "పత్తి పంటకు క్రమం తప్పకుండా నీరు కావాలి, కానీ నీరు నిల్వ ఉండకూడదు।",
        "medicine_source": "📍 *ఎక్కడ మరియు ఎలా కొనాలి:* మీరు ఈ మందులను స్థానిక వ్యవసాయ సహకార సంఘాలు (PACS), అధీకృత పురుగుమందుల డీలర్లు లేదా రైతు భరోసా కేంద్రాల నుండి కొనుగోలు చేయవచ్చు.\n\n📝 *పొందే విధానం:* సోకిన ఆకు ఫోటోను మరియు ఈ సమాచారాన్ని స్థానిక వ్యవసాయ అధికారికి లేదా డీలర్‌కు చూపించండి. వారు దాన్ని పరిశీలించి, మందుల మోతాదును ధృవీకరించి మీకు అవసరమైన మందులను అందజేస్తారు.",
        "application_process": "📝 *ఎలా వాడాలి:* సూచించిన సరైన మోతాదును మాత్రమే వాడండి. పిచికారీ చేసేటప్పుడు ఎల్లప్పుడూ రక్షణ కవచాలు (గ్లౌజులు/మాస్క్) ధరించండి. ఉదయం (6-9 గంటలు) లేదా సాయంత్రం వేళల్లో పిచికారీ చేయడం ఉత్తమం.",
        "default": "దయచేసి ఆకు చిత్రాన్ని అప్‌లోడ్ చేయండి లేదా పత్తికి సంబంధించిన ప్రశ్న అడగండి।"
    }
}

# 3. KEYWORD MAPPING
keyword_mapping = {
    "fertilizer": ["fertilizer", "khad", "urea", "npk", "खाद", "ఎరువులు"],
    "growth": ["growth", "increase", "yield", "बढ़त", "ఎదుగుదల"],
    "pests": ["pest", "insect", "worm", "bug", "कीड़े", "పురుగులు"],
    "water": ["water", "irrigation", "rain", "पानी", "నీరు"],
    "medicine_source": ["buy", "purchase", "shop", "get", "store", "obtain", "procure", "where can i", "how to get", "कहां", "मिलेगी", "मिलेगा", "मिले", "खरीदें", "कहां से", "प्राप्त", "దొరుకుతాయి", "కొనుగోలు", "కొనాలి", "ఎక్కడ", "దొరుకుతుంది", "దొరుకును", "పొందాలి"],
    "application_process": ["process", "apply", "how to", "use", "spray", "procedure", "कैसे", "उपयोग", "कैसे लगाएं", "तरीका", "प्रक्रिया", "ఎలా", "వాడాలి", "పద్ధతి", "విధానం"],
    
    # Specific disease mapping
    "bacterial_blight": ["blight", "bacterial", "spots", "బ్లైట్"],
    "curl_virus": ["curl", "virus", "wrinkled", "ముడత"],
    "leaf_hopper_jassids": ["jassid", "hopper", "పురుగులు"],
    "leaf_reddening": ["reddening", "red leaf", "ఎర్రబడటం"],
    "leaf_variegation": ["variegation", "వైవిధ్యం"]
}

# 4. HELPER FUNCTIONS
def get_advisory(disease, language="en"):
    if language not in ["en", "hi", "te"]:
        language = "en"
    
    if disease in advisory:
        return advisory[disease][language]
    
    return advisory.get("healthy_leaf", {}).get(language, "Healthy leaf.")
