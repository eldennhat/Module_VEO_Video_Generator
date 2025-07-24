PROJECT_ID = "YOUR_PROJECT_ID"
LOCATION = "us-central1"
MODEL_ID = "veo-3.0-generate-preview"
API_URL = (
    f"https://{LOCATION}-aiplatform.googleapis.com/v1/"
    f"projects/{PROJECT_ID}/locations/{LOCATION}/publishers/google/"
    f"models/{MODEL_ID}:predict"
)
