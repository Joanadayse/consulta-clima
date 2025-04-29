import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

def buscar_clima(cidade):
    url=f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&units=metric&lang=pt_br"
    resposta= requests.get(url)
    if resposta.status_code==200:
        dados= resposta.json()
        return{
            "temperatura": dados['main']['temp'],
            "descricao": dados['weather'][0]['description'],
            "umidade": dados['main']['humidity'],
            "vento":dados['wind']['speed'],
            "cidade":dados['name']
        }
    else:
        return None
    