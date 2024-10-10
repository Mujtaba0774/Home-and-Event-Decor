import os
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def suggest_style_openai(event_type: str, user_preferences: list = None):
    prompt = f"Suggest a decoration style for a {event_type} event."
    if user_preferences:
        preferences = ', '.join(user_preferences)
        prompt += f" The user prefers {preferences}."
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        temperature=0.7)
    
    return response.choices[0].text.strip()

def suggest_layout_openai(event_type: str, room_size: int = None):
    prompt = f"Suggest a decoration layout for a {event_type} event."
    if room_size:
        prompt += f" The room size is {room_size} square meters."
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        temperature=0.7)
    
    return response.choices[0].text.strip()
