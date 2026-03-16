import os
import json
from openai import OpenAI
from tools import somar, subtrair, multiplicar, dividir, celsius_para_fahrenheit, fahrenheit_para_celsius, buscar_produto, verificar_estoque, criar_evento, listar_eventos, buscar_clima
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
client = Groq()

tools = [
    {
        "type": "function",
        "function": {
            "name": "somar",
            "description": "Somar dois números",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "number"},
                    "b": {"type": "number"}
                },
                "required": ["a", "b"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "multiplicar",
            "description": "Multiplicar dois números",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "number"},
                    "b": {"type": "number"}
                },
                "required": ["a", "b"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "subtrair",
            "description": "Subtrair dois números",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "number"},
                    "b": {"type": "number"}
                },
                "required": ["a", "b"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "dividir",
            "description": "Dividir dois números",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "number"},
                    "b": {"type": "number"}
                },
                "required": ["a", "b"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "celsius_para_fahrenheit",
            "description": "Converter Celsius para Fahrenheit",
            "parameters": {
                "type": "object",
                "properties": {
                    "celsius": {"type": "number"},
                },
                "required": ["celsius"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "fahrenheit_para_celsius",
            "description": "Converter Fahrenheit para Celsius",
            "parameters": {
                "type": "object",
                "properties": {
                    "fahrenheit": {"type": "number"},
                },
                "required": ["fahrenheit"]
            }
        }
    },
    {
    "type": "function",
    "function": {
        "name": "buscar_produto",
        "description": "Buscar o preço de um produto pelo nome",
        "parameters": {
            "type": "object",
            "properties": {
                "nome_produto": {"type": "string"}
            },
            "required": ["nome_produto"]
        }
    }
    },
    {
        "type": "function",
        "function": {
            "name": "verificar_estoque",
            "description": "Verificar se existe um produto no estoque",
            "parameters": {
                "type": "object",
                "properties": {
                    "nome_produto": {"type": "string"}
                },
                "required": ["nome_produto"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "criar_evento",
            "description": "Criar um evento com nome e data",
            "parameters": {
                "type": "object",
                "properties": {
                    "titulo": {"type": "string"},
                    "data": {"type": "string"}
                },
                "required": ["titulo", "data"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "listar_eventos",
            "description": "Listar os eventos", 
            "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "buscar_clima",
            "description": "Buscar o clima em determinada cidade",
            "parameters": {
                "type": "object",
                "properties": {
                    "cidade": {"type": "string"},
                },
                "required": ["cidade"]
            }
        }
    },
]

functions = {
            "somar": somar,
            "subtrair": subtrair,
            "multiplicar": multiplicar,
            "dividir": dividir,
            "celsius_para_fahrenheit": celsius_para_fahrenheit,
            "fahrenheit_para_celsius": fahrenheit_para_celsius,
            "buscar_produto": buscar_produto,
            "verificar_estoque": verificar_estoque,
            "criar_evento": criar_evento,
            "listar_eventos": listar_eventos,
            "buscar_clima": buscar_clima
        }

def perguntar(pergunta: str):
    response = client.chat.completions.create(
        # model="gpt-4o-mini",
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "system", "content": "Você é um assistente que decide qual função usar."},
            {"role": "user", "content": pergunta}
        ],
        tools=tools,
        tool_choice="auto",
        temperature=0
    )

    # print('response:', response)

    message = response.choices[0].message

    if message.tool_calls:
        tool_call = message.tool_calls[0]
        tool_name = tool_call.function.name
        args = json.loads(tool_call.function.arguments)

        print(f"Tool chamada: {tool_name}")
        print(f"Argumentos: {args}")

        func = functions.get(tool_name)

        if func:
            return func(**args)        

    return message.content


print(perguntar("Criar evento reunião amanhã"))
print(perguntar("liste os eventos"))