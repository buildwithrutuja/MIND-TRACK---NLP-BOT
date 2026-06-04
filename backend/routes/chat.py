from fastapi import APIRouter

router = APIRouter()

# Department keyword dictionary
# These are the keywords we check in the user message
department_map = {
    "Cardiology": [
        "chest pain", "heart", "cardiac", "palpitation", "breathless",
        "seene mein dard", "dil", "heart attack", "BP", "blood pressure",
        "seene mein jalan", "mala chati dukhtay", "heart beat"
    ],
    "Orthopedics": [
        "bone", "joint", "fracture", "knee", "back pain", "spine",
        "haddi", "ghutna", "kamar dard", "haddi tooti", "mala gadulyat dukhtay",
        "shoulder pain", "ankle", "wrist"
    ],
    "ENT": [
        "ear", "nose", "throat", "hearing", "tonsil", "sinus",
        "kaan", "naak", "gala", "kaan dard", "kaan se pani",
        "gala dukhtay", "naak band"
    ],
    "Ophthalmology": [
        "eye", "vision", "blur", "itchy eyes", "red eye",
        "aankh", "aankhon mein", "dhundla", "aankh dard",
        "dola dukhtay", "dola lal"
    ],
    "Gastroenterology": [
        "stomach", "abdomen", "vomit", "nausea", "diarrhea",
        "pet mein dard", "ulti", "pet dard", "loose motion",
        "pot dukhtay", "jullub", "acidity", "gastric"
    ],
    "Dermatology": [
        "skin", "rash", "itching", "allergy", "acne",
        "khujli", "charm rog", "daane", "angavar pural",
        "skin allergy", "fungal"
    ],
    "Neurology": [
        "headache", "migraine", "seizure", "memory", "unconscious",
        "sar dard", "chakkar", "epilepsy", "stroke",
        "doke dukhtay", "chakkar yetay", "numbness"
    ],
    "Psychiatry": [
        "depression", "anxiety", "stress", "mental", "sleep",
        "neend nahi", "ghabrahat", "udaasi", "tension",
        "manasik", "takleef", "panic"
    ],
    "Gynecology": [
        "pregnancy", "period", "menstrual", "women", "discharge",
        "garbh", "mahavari", "pet mein dard mahila", "delivery",
        "prasav", "masik"
    ],
    "Pediatrics": [
        "child", "baby", "infant", "kids fever", "vaccination",
        "bachcha", "baal", "navajaata", "mulagacha tap",
        "lahan mulagacha", "bal rog"
    ],
    "General Medicine": [
        "fever", "cold", "cough", "weakness", "fatigue",
        "bukhar", "zukam", "khansi", "tap", "saradi",
        "khumari", "thakan", "body pain"
    ]
}

# Emergency keywords — these bypass normal classification
emergency_keywords = [
    "heart attack", "stroke", "unconscious", "not breathing",
    "severe bleeding", "chest pain severe", "accident",
    "behosh", "sans nahi", "zyada khoon", "emergency",
    "तत्काल", "khub tras hotay"
]

def detect_department(message: str):
    message_lower = message.lower()

    # Check emergency first
    for keyword in emergency_keywords:
        if keyword in message_lower:
            return "Emergency", True

    # Check each department
    for department, keywords in department_map.items():
        for keyword in keywords:
            if keyword in message_lower:
                return department, False

    # Nothing matched
    return "General Medicine", False


@router.post("/chat")
def chat(data: dict):
    user_message = data.get("user_message", "")

    if not user_message:
        return {"error": "Please enter your symptoms"}

    department, is_emergency = detect_department(user_message)

    if is_emergency:
        bot_response = "🚨 This sounds like an emergency! Please go to the EMERGENCY department immediately or call 112."
    else:
        bot_response = f"Based on your symptoms, please visit the {department} department."

    return {
        "user_message": user_message,
        "suggested_department": department,
        "bot_response": bot_response,
        "emergency": is_emergency,
        "disclaimer": "This is not a medical diagnosis. Please consult a doctor."
    }