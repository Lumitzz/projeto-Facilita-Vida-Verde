from chatbot import chain
from fastapi import FastAPI
from langserve import add_routes

app = FastAPI(title="Meu app de IA",  description="Faça sua pergunta referente a chás e ervas")


add_routes(app, chain, path="/duvidas")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)