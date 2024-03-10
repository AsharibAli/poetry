# fastapi_neon/main.py

from fastapi import FastAPI

app = FastAPI(
    title="Hello World API",
    version="0.0.1",
    servers=[
        {
            "url": "https://066c-119-73-102-23.ngrok-free.app/",  # ADD NGROK URL Here Before Creating GPT Action
            "description": "Development Server",
        }
    ],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}
