from fastapi import FastAPI
from fastapi_users import FastAPIUsers
from sqlalchemy import select

from auth.auth import auth_backend
from auth.manager import get_user_manager
from auth.models import User
from auth.schemas import UserCreate, UserRead
from dealer_logic import decide, get_result

# from fastapi.middleware.cors import CORSMiddleware
from deck import card_generator
from schemas import GameSetBank, GetGame, WagerCreate

# just simple comment


app = FastAPI(title="easy blackjack")


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,  # type: ignore
    [auth_backend],
)


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

# app.add_middleware(CORSMiddleware)


available_game = ["blackjack"]

fake_users = [{"id": 1, "name": "ilya", "bank": 1000}]

game = {
    "id": 1,
    "dealer bank": 0,
    "user bank": 0,
    "wager": 0,
    "users cards": {
        "faces": [],
        "suits": [],
        "total cost": 0,
    },
    "dealers_cards": {
        "faces": [],
        "suits": [],
        "total cost": 0,
    },
    "status": "goes on",
}


@app.get("/")
def root():
    return "Hello user try the game"


@app.get("/blackjack")
def get_games():
    return available_game


@app.post("/blackjack", response_model=GetGame)
def start_new_game(gamebank: GameSetBank):
    user = [user for user in fake_users if user.get("id") == gamebank]
    if user[0]["bank"] >= gamebank:
        game["user bank"] = gamebank
        user[0]["bank"] -= gamebank
        game["dealer bank"] = 2000
        game["status"] = "begins"
        return {"status": 200, "your bank": user[0]["bank"]}
    else:
        return {"status": 200, "your bank": "you can not choose this amount"}


@app.get("/blackjack/game/hit")
def get_card():
    game_status = game["status"]
    user_cards = game["users cards"]
    random_card = next(card_generator)
    if game_status == "goes on":
        user_cards["faces"].append(random_card[0])
        user_cards["costs"].append(random_card[1])
        user_cards["suits"].append(random_card[2])
        user_cards["total cost"] += random_card[1]
    game["status"] = (
        "goes on" if user_cards["total cost"] < 21 else "user completed"
    )
    return {"status": 200, "game": game}


@app.get("/game/stand")
def dealers_turn():
    dealers_cards = game["dealers_cards"]
    card_sum = dealers_cards["total cost"]
    while decide(card_sum):
        random_card = next(card_generator)
        dealers_cards["faces"].append(random_card[0])
        dealers_cards["costs"].append(random_card[1])
        dealers_cards["suits"].append(random_card[2])
        dealers_cards["total cost"] += random_card[1]
        card_sum = dealers_cards["total cost"]
    game["status"] = "dealer completed"
    return {"status": 200, "game": game}


@app.get("/game/{game_id}/result")
def get_game_result():
    dealers_cards = game["dealers_cards"]
    dealers_total = dealers_cards["total cost"]
    users_cards = game["users cards"]
    users_total = users_cards["total cost"]
    if game["status"] == "dealer completed":
        game["status"] = get_result(users_total, dealers_total)
        if game["status"] == "dealer win":
            game["user bank"] -= game["wager"]
    return {"status": 200, "game": game}


@app.post("/blackjack/game/wager")
def place_wager(amount: int = 10):
    if game["status"] == "begins":
        game["wager"] = amount
        if game["user bank"] >= amount:
            game["user bank"] -= amount
            game["status"] = "goes on"
    return {"status": 200, "game": game}
