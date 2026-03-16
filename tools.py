def somar(a, b):
    print('Entrou somar')
    return a + b

def multiplicar(a, b):
    return a * b

def subtrair(a, b):
    return a - b

def dividir(a, b):
    return a / b

def celsius_para_fahrenheit(celsius):
    print('entrou celsius', celsius)
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

produtos = {
    "notebook": 4500,
    "mouse": 80,
    "teclado": 150
}

def buscar_produto(nome_produto: str):
    nome_produto = nome_produto.lower()

    if nome_produto in produtos:
        preco = produtos[nome_produto]
        return f"O preço do {nome_produto} é R${preco}"
    
    return f"O produto '{nome_produto}' não foi encontrado."

estoque = {
    "notebook": 5,
    "mouse": 20,
    "teclado": 8
}

def verificar_estoque(nome_produto: str):
    nome_produto = nome_produto.lower()

    if nome_produto in estoque:
        quantidade = estoque[nome_produto]
        return f"Temos {quantidade} unidades de {nome_produto}."
    
    return f"O produto '{nome_produto}' não existe."

eventos  = []

def criar_evento(titulo: str, data: str):
    titulo = titulo.strip()
    data = data.strip()

    eventos.append({
        "titulo": titulo,
        "data": data
    })

    return f"Evento '{titulo}' criado para {data}."

def listar_eventos():
    if not eventos:
        return "Nenhum evento cadastrado."
    
    resultado = "Eventos cadastrados:\n"
    for i, evento in enumerate(eventos, start=1):
        resultado += f"{i}. {evento['titulo']} - {evento['data']}\n"
    
    return resultado

def buscar_clima(cidade):

    clima = {
    "sao paulo": "24°C e nublado",
    "bauru": "30°C e ensolarado",
    "curitiba": "18°C e chuvoso"
    }
    
    cidade = cidade.lower()
    
    if cidade in clima:
        return f"O clima em {cidade} é {clima[cidade]}."
    
    return f"Não foi possível encontrar informações sobre o clima em {cidade}."