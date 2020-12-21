from fastapi import APIRouter

router = APIRouter()


@router.get("/consent")
async def consent():
    return {}
