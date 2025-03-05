from fastapi import APIRouter, HTTPException
from src.models.schemas import TravelRequest, Itinerary
from src.core.gpt_client import GPTClient

router = APIRouter()
gpt_client = GPTClient()

@router.post("/itinerary", response_model=Itinerary)
async def create_itinerary(request: TravelRequest):
    try:
        daily_plans = await gpt_client.generate_itinerary(
            request.destination, 
            request.days
        )
        
        return Itinerary(
            destination=request.destination,
            days=request.days,
            daily_plans=daily_plans
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))