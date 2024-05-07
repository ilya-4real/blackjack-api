from fastapi import APIRouter

router = APIRouter(prefix="/players", tags=["players"])


@router.post("/")
async def register_player(): ...


@router.get("/me")
async def get_player(): ...


@router.post("token")
async def refresh_token():
    return {"status": 200}
