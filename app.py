from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
import requests
from dotenv import load_dotenv
import os

#load environment variables from .env file
load_dotenv()
API_KEY = os.getenv("BALLDONTLIE_API_KEY")

#initialize FastAPI app
app = FastAPI()

# Define the data model for team performance
class TeamPerformance(BaseModel):
    team_id: int
    team_name: str
    wins: int
    losses: int
    win_percentage: float


#get endpoint to fetch team performance
# @app.get("/team/{team_id}/performance")
# async def get_team_performance(team_id: int, season: int):
#     print(f"Fetching performance for team_id: {team_id}, season: {season}")
#     print("api key is", API_KEY)
#     #fetch data from the BallDontLie API
#     url = f"https://api.balldontlie.io/mlb/v1/standings?season={season}"
#     headers = {"Authorization": f"Bearer {API_KEY}"}
#     response = requests.get(url, headers=headers)
#     print(f"Response: {response}")


# #check if the response is successful    
#     if response.status_code != 200:
#         raise HTTPException(status_code=502, detail="Upstream API failure")    
#     #filter for matching team_id
#     data = response.json().get("data", [])
#     for team in data:
#         if team["team"]["id"] == team_id:
#             return TeamPerformance(
#                 team_id=team_id,
#                 team_name=team["team"]["full_name"],
#                 wins=team["wins"],
#                 losses=team["losses"],
#                 win_percentage=team["win_percentage"]
#             )
    
#     # Team not found
#     raise HTTPException(status_code=404, detail="Team not found for season")
import json
@app.get("/team/{team_id}/performance")
def get_team_performance(team_id: int, season: int):
    url = f"https://api.balldontlie.io/mlb/v1/teams/{team_id}"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response =  requests.get(url, headers=headers)
    print(f"Response: {response.json()}")
    # Check if the response is successful
    if response.status_code != 200:
        raise HTTPException(status_code=502, detail="Upstream API failure")
    
    #filter for matching team_id
    team =  response.json().get("data", {})
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


#asynchronous function to fetch team performance
