import requests
from .api_config import VEO_API_KEY, VEO_API_URL

def call_veo_api(prompt: str) -> dict:
    headers = {
        "Authorization": f"Bearer {VEO_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "instances": [{"prompt": prompt}],
        "parameters": {
            "duration_seconds": 5,
            "aspect_ratio": "16:9"
        }
    }

    response = requests.post(VEO_API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API Error {response.status_code}: {response.text}")
