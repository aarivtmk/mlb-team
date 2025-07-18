from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import aiohttp
from dotenv import load_dotenv
import os

# load environment variables from .env file
load_dotenv()
API_KEY = os.getenv("BALLDONTLIE_API_KEY")

# Initialize FastAPI app
app = FastAPI()

# Define the data model for team performance
class TeamPerformance(BaseModel):
    team_id: int
    team_name: str
    wins: int
    losses: int
    win_percentage: float

# get endpoint to fetch team performance
@app.get("/team/{team_id}/performance")
async def get_team_performance(team_id: int, season: int):
    url = f"https://api.balldontlie.io/mlb/v1/teams/{team_id}"
    headers = {"Authorization": f"Bearer {API_KEY}"}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            # Check if the response is successful
            if response.status != 200:
                raise HTTPException(status_code=502, detail="Upstream API failure")
            
            # Filter for matching team_id
            team_data = await response.json()
            team = team_data.get("data", {})
            if not team:
                raise HTTPException(status_code=404, detail="Team not found for season")
            
            # Return with placeholder values
            return TeamPerformance(
                team_id=team_id,
                team_name=team["display_name"],
                wins=0,
                losses=0,
                win_percentage=0.0
            )