# Travel Agent App - 100% Built with Copilot for demo purposes 

An intelligent travel planning assistant that generates personalized daily itineraries using GPT. The app provides specific, actionable travel recommendations including actual places, attractions, and addresses for your destination.

## Features

- AI-powered itinerary generation with specific locations and addresses
- Simple REST API for requesting travel plans
- User-friendly web interface for easy interaction
- Customizable trip duration (1-5 days)

## Project Structure

```
travel-guide-app
├── src
│   ├── core
│   │   └── gpt_client.py    # GPT integration for intelligent recommendations
│   ├── models
│   │   └── schemas.py       # Data models for requests/responses
│   └── routers
│       └── itinerary.py     # API endpoints for itinerary generation
└── frontend
    ├── index.html          # Web interface
    ├── styles.css          # Styling
    └── script.js           # Frontend logic
```

## Setup

1. Clone and install dependencies:
```bash
git clone <repository-url>
cd travel-guide-app
pip install -r requirements.txt
```

2. Set your OpenAI API key in `.env`:
```
OPENAI_API_KEY=your_api_key_here
```

3. Start the server:
```bash
uvicorn src.app:app --reload
```

## Usage

### API

Send a POST request to `/itinerary`:
```json
{
  "destination": "Tokyo",
  "days": 3
}
```

### Web Interface

Open `frontend/index.html` in your browser, enter your destination and select number of days to generate an itinerary.

## License

MIT License
