from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

app = FastAPI()

# Permitir acesso do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, substitua pelo domínio do seu site GitHub Pages
    allow_methods=["*"],
    allow_headers=["*"],
)

class Credenciais(BaseModel):
    email: str
    senha: str

@app.post("/gerar-token")
def gerar_token(credenciais: Credenciais):
    url = "https://ediapi.onlineapp.com.br/toolkit/api/Autenticacao/AutenticarUsuario"
    payload = {
        "email": credenciais.email,
        "senha": credenciais.senha
    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text)
