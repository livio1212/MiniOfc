import os 
import requests
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

def perguntar_groq(pergunta):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama3-70b-8192",
        "messages": [
            {
                "role": "system",
                "content": "voce é um asssitente virtual que atende perguntas relacionadas ao ramo de cartorio de registros civis, deve responder de forma clara e objetiva cada pergunta feita sempre se baseando em dados reais e oficiais, como se trata de uma area juridica voce deve sempre sem embasar em fatos reais, voce nao respondera nada que nao seja relacionado ao assunto de cartorio de registros civis, voce deve sempre responder de forma clara e objetiva, nunca deve responder com emojis ou gírias, sempre deve responder com clareza e objetividade, nunca deve responder com ironia ou sarcasmo, nunca deve responder com piadas ou brincadeiras, nunca deve responder com respostas vagas ou incompletas, sempre deve responder com respostas completas e detalhadas. caso receba uma pergunta que nao e relacionaada ao assunto principal diga que nao esta autorizado a responder.",
            },
            {
                "role": "user",
                "content": pergunta
            }
        ],
        "temperature": 0.7,
    }
    response = requests.post(GROQ_API_URL, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return "Erro ao consultar base de conhecimento"

