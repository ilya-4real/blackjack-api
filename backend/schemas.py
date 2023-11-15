from pydantic import BaseModel

class GetGame(BaseModel):
    id: int
    user_bank: int
    wager: int
    sum_users_cards: int
    sum_dealers_cards: int
    status: int


class WagerCreate(BaseModel):
    amount: int


class GameSetBank(BaseModel):
    bank: int
