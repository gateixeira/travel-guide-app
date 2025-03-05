import openai
from src.config.settings import settings

class GPTClient:
    def __init__(self):
        openai.api_key = settings.OPENAI_API_KEY

    async def generate_itinerary(self, destination: str, days: int) -> list[str]:
        prompt = f"Create a {days}-day itinerary for {destination} with the most popular tourist attractions. Format as a day-by-day list."
        
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful travel guide. Please do not be generic, always provide names of places and addresses so that the user knows where exactly to go."},
                {"role": "user", "content": prompt}
            ]
        )
        
        return response.choices[0].message.content.split('\n')