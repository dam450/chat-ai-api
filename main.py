from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
import uvicorn

from routers import chat, check, root

load_dotenv()

app = FastAPI(title="chat-ai-api", version="0.1.0", description="it is an Chat AI API")

origins = os.getenv("ALLOWED_HOSTS")

if origins is None:
    origins = ["*"]
else:
    origins = origins.split(",")
    origins = [origin.strip() for origin in origins]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(root.router)
app.include_router(check.router)
app.include_router(chat.router)


def main():
    print("Hello from chat-ai-api!")
    uvicorn.run("main:app", host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
