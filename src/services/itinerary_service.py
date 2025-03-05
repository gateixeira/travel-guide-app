def generate_itinerary(destination: str, days: int) -> dict:
    from src.core.gpt_client import GptClient

    gpt_client = GptClient()
    itinerary_data = gpt_client.generate_itinerary(destination, days)
    
    return itinerary_data