from fastapi import APIRouter

router = APIRouter()

@router.get("/departments")
def get_departments():
    return {
        "departments": [
            {"name": "Cardiology", "floor": "2nd Floor", "block": "OPD Block B"},
            {"name": "Orthopedics", "floor": "3rd Floor", "block": "OPD Block A"},
            {"name": "ENT", "floor": "1st Floor", "block": "OPD Block C"},
            {"name": "Ophthalmology", "floor": "1st Floor", "block": "OPD Block D"},
            {"name": "Gastroenterology", "floor": "2nd Floor", "block": "OPD Block A"},
            {"name": "Dermatology", "floor": "Ground Floor", "block": "OPD Block B"},
            {"name": "Neurology", "floor": "3rd Floor", "block": "OPD Block B"},
            {"name": "Psychiatry", "floor": "4th Floor", "block": "OPD Block A"},
            {"name": "Gynecology", "floor": "2nd Floor", "block": "OPD Block C"},
            {"name": "Pediatrics", "floor": "1st Floor", "block": "OPD Block A"},
            {"name": "General Medicine", "floor": "Ground Floor", "block": "OPD Block A"},
            {"name": "Emergency", "floor": "Ground Floor", "block": "Emergency Block"}
        ]
    }