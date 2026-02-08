from fastapi import APIRouter, Request
import requests

router = APIRouter()

@router.get("/my-location/")
def get_user_location(request: Request):
    ip = request.client.host  # Gets user's IP (in dev it might show 127.0.0.1)
    
    # Free geolocation (no key)
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        
        if data.get("status") == "success":
            return {
                "ip": ip,
                "city": data.get("city", "Unknown"),
                "country": data.get("country", "Unknown"),
                "region": data.get("regionName", "Unknown"),
                "lat": data.get("lat"),
                "lon": data.get("lon")
            }
        else:
            return {"error": "Could not get location"}
    except:
        return {"error": "Location service unavailable"}