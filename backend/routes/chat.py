from fastapi import APIRouter

router = APIRouter()

@router.post("/chat")
def chat(data: dict):
    user_message = data.get("user_message", "")

    # For now returning fake response
    # Member 3 will plug in the real NLP here later
    return {
        "user_message": user_message,
        "detected_language": "en",
        "suggested_department": "General Medicine",
        "confidence_score": 0.5,
        "bot_response": "Please visit General Medicine — Ground Floor, OPD Block A.",
        "emergency": False,
        "disclaimer": "This is not a medical diagnosis. Please consult a doctor."
    }