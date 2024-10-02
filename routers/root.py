from fastapi import APIRouter
from fastapi.responses import RedirectResponse


router = APIRouter()


@router.get("/")
async def root():
    """
    Redirect to the API documentation.

    Returns a 307 redirect to "/docs".
    """
    return RedirectResponse(url="/docs", status_code=307)
