import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

API_URL = "https://tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com/"
GET_NFL_BOX_SCORE = "getNFLBoxScore"
GET_NFL_STATS_SP = "getNFLGamesForPlayer"
GET_DAILY_SCOREBOARD = "getNFLScoresOnly"
FANTASY_POINT_PROJECTIONS = "getNFLProjections"
GET_PLAYER_INFO = "getNFLPlayerInfo"

_API_CONSTS = (
    API_URL, GET_NFL_BOX_SCORE,
    GET_NFL_STATS_SP, GET_DAILY_SCOREBOARD,
    FANTASY_POINT_PROJECTIONS, GET_PLAYER_INFO
)