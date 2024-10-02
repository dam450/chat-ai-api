from duckduckgo_search import DDGS
from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/chat/", tags=["chat"])
async def chat(query: str, ai_model: str = "gpt-4o-mini", timeout: int = 30):
    """
    Perform a chat query on the DuckDuckGo AI.

    :param query: The query string to send to the AI
    :param ai_model: The AI model to use for the query: "gpt-4o-mini", "claude-3-haiku", "llama-3.1-70b", "mixtral-8x7b". Defaults to "gpt-4o-mini"..

    :param timeout: The timeout in seconds for the query. Defaults to 30.
    :return: JSON response with the AI's response.
    """
    response = DDGS().chat(query, model=ai_model, timeout=timeout)
    return JSONResponse(content={"response": response})
