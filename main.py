import openai
import os
import json

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
            A ficha deve estar estritamente estruturada em CSV, 
            com as colunas: 'Treino' (Letra), 'Exercício', 'Séries', 'Repetições' e 'Descanso (segundos)'.
        """}
    ]
    response = generate_response(messages)

    second_message = [
        {"role": "user", "content": f"""
         Ajuste esta ficha de treino para seguir o formato CSV com exatamente essas colunas:'Treino' (Letra), 'Exercício', 'Séries', 'Repetições' e 'Descanso (segundos)': """},
        {"role": "assistant", "content": response},
    ]


    second_responde = generate_response(second_message)
    return second_responde
