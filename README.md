# MLB Team Performance API

## Setup

1. Install virtual environment: `python3 -m venv <env_name>`
2. Activate virtual environment:
   - On macOS/Linux: `source <env_name>/bin/activate`
   - On Windows: `<env_name>\Scripts\activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Set API key from balldontlie.io

### How to Get API Key

- Visit [balldontlie.io](https://www.balldontlie.io/) and register on the homepage.
- Copy the API key from your account dashboard.

## Run

`uvicorn app:app --port 8000`

## Test

- Successful Request: `curl -i "http://localhost:8000/team/26/performance?season=2023"`
  - Expect: **200 OK**
  - JSON body: `{"team_id": 26, "team_name": "Oakland Athletics", "wins": 0, "losses": 0, "win_percentage": 0.0}`
- Team Not Found: `curl -i "http://localhost:8000/team/999/performance?season=2023"`
  - Expect: **404 Not Found**
  - JSON body: `{"detail": "Team not found for season"}`
- External API Failure: Unset API key (`unset BALLDONTLIE_API_KEY`) and run `curl -i "http://localhost:8000/team/26/performance?season=2023"`
  - Expect: **502 Bad Gateway**
  - JSON body: `{"detail": "Upstream API failure"}`

## Notes

- Using Free tier `/mlb/v1/teams` endpoint due to account pricing limitations. Wins, losses, and win_percentage are set to 0 as standings data requires ALL-STAR/GOAT tier.

Thank you

Aariv
