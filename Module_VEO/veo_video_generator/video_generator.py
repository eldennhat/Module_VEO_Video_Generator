from .prompt_cleaner import clean_prompt
from .prompt_formatter import format_prompt
from .veo_api_caller import call_veo_api
from .output_handler import extract_video_url

def generate_video(prompt: str) -> str:
    cleaned = clean_prompt(prompt)
    formatted = format_prompt(cleaned)
    response = call_veo_api(formatted)
    return extract_video_url(response)
