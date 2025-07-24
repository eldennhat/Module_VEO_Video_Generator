def extract_video_url(api_response: dict) -> str:
    return api_response.get("predictions", [{}])[0].get("video_uri", "Không có URL")
