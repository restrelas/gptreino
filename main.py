import utils

import openai
import os
import json
import time

openai.api_key  = os.getenv('OPENAI_KEY')

def generate_response(messages, model="gpt-3.5-turbo-0613"):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]

def conversation(dadosPessoais):
    messages=[
        {"role":"assistant", "content": json.dumps(dadosPessoais)},
        {"role": "user", "content": f"""
            Você é um personal trainer e precisa criar uma ficha de treino para {dadosPessoais['nome']}
            A ficha deve ser dividida por letras para {dadosPessoais['dias']} dias.
            Numero de exercícios mínimos por treino = 6, máximo = 8.
            A ficha deve estar estruturada em CSV, 
            com as colunas: 'Treino' (Letra), 'Exercício', 'Séries', 'Repetições' e 'Descanso (segundos)'.
        """}
    ]
    response = generate_response(messages)
    return response

# entrada
nome = "Fulano"
sexo = ["feminino", "masculino"]
idade = 14 
objetivos = ["perda de peso", "ganho de massa muscular", "melhoria da resistência cardiovascular","melhoria de flexibilidade", "melhoria de postura", "alívio de dores crônicas", "treinamento funcional"]
dias = 4
condicao_med = ["doença cardíaca", "diabete", "asma ou doença respiratória", "obesidade", "gravidez"]
nivel_atual = ["sendentaria", "moderada", "ativo"]
peso = 45
altura = 1.65


dadosPessoais = utils.get_dados_pessoais(nome, sexo[0], idade, objetivos[0], peso, altura, dias)
inicio = time.time()
response = conversation(dadosPessoais)
fim = time.time()


print(response)
print("\ntempo: ", fim - inicio)

utils.generate_csv(response)
print("\nArquivo CSV criado")