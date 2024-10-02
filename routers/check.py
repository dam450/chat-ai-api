from fastapi import APIRouter
from fastapi.responses import Response

router = APIRouter()


@router.get("/healthz")
def healthz():
    """
    Simple health check endpoint. Returns a 204 No Content response.
    """
    return Response(content=None, status_code=204)
