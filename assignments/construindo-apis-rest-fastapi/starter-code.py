# Código inicial para Construindo APIs REST com o framework FastAPI

# Para executar este código, você precisa instalar FastAPI e Uvicorn:
# pip install fastapi uvicorn

from fastapi import FastAPI

app = FastAPI()

# TODO: Adicione seus endpoints aqui

@app.get("/")
def read_root():
    return {"message": "Bem-vindo ao FastAPI"}

# Para executar o servidor: uvicorn starter_code:app --reload