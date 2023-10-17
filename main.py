import openai
import os
import json

openai.api_key  = os.getenv('OPENAI_KEY')

def get_dados_pessoais(nome, sexo, idade, objetivos, peso, altura, dias):
  info = {
      "nome": nome,
      "sexo": sexo,
      "idade": idade,
      "objetivos": objetivos,
      "peso": peso,
      "altura": altura,
      "imc": peso/(altura**2),
      "dias": dias
  }
  return info

def conversation(dadosPessoais):

  messages=[
        {"role":"assistant", "content": json.dumps(dadosPessoais)},
        {"role": "user", "content": f"""
          Crie uma ficha de treino para {dadosPessoais["nome"]} em estrutura de tabela para {dadosPessoais["dias"]} dias
        """}
    ]
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0613",
    messages=messages,
    temperature=0,
  )
  return response.choices[0].message["content"]



# entrada
nome = "Fulano"
sexo = ["feminino", "masculino"]
idade = 14 
objetivos = ["perda de peso", "ganho de massa muscular", "melhoria da resistência cardiovascular","melhoria de flexibilidade", "melhoria de postura", "alívio de dores crônicas", "treinamento funcional"]
semanas = 2
dias = 3
condicao_med = ["doença cardíaca", "diabete", "asma ou doença respiratória", "obesidade", "gravidez"]
nivel_atual = ["sendentaria", "moderada", "ativo"]
peso = 45
altura = 1.65




dadosPessoais = get_dados_pessoais("Fulano", sexo[0],idade,objetivos[0],peso,altura,dias)
r = conversation(dadosPessoais)
print(r)