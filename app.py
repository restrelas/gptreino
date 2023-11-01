import utils
import main

from flask import Flask, make_response, redirect, render_template, request, url_for

import csv
from io import BytesIO
import io
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors



app = Flask(__name__)
session = {}


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/receber-dados', methods=['POST'])
def receber_dados():
    nome = request.form.get('nome')
    sexo = request.form.get('sexo')
    idade = request.form.get('idade')
    peso = int(request.form.get('peso'))
    altura = int(request.form.get('altura'))
    tipo_treino = request.form.get('tipo_treino')
    divisao_treino = request.form.get('divisao_treino')
    condicao_med = request.form.get('condicao_med[]')
    nivel_atual = request.form.get('nivel_atual')

    if condicao_med == None:
        condicao_med = "nenhum"

    dadosPessoais = utils.get_dados_pessoais(nome, sexo, idade,  peso, altura, tipo_treino, divisao_treino, condicao_med, nivel_atual)

    csv_data = main.conversation(dadosPessoais)

    session['csv_data'] = csv_data

    return redirect(url_for('mostrar_ficha_treino'))


@app.route('/mostrar_ficha_treino')
def mostrar_ficha_treino():
    csv_data = session.get('csv_data') 

    csv_lines = csv_data.split('\n')
    csv_reader = csv.reader(csv_lines, delimiter=',')
    
    # Converta os dados CSV em uma lista de dicionários
    data = []
    first_line = True

    for row in csv_reader:
        if first_line:
            first_line = False
            continue  # Pule a primeira linha

        data.append({'Treino': row[0], 'Exercicio': row[1], 'Series': row[2], 'Repeticoes': row[3], 'Descanso': row[4]})

    return render_template('ficha_treino.html', data=data)


@app.route('/gerar-pdf', methods=['GET'])
def gerar_pdf():
    data = session.get('csv_data')

    if data:
        data = data.strip()
        csv_data = BytesIO(data.encode('utf-8'))
        reader = csv.DictReader(io.TextIOWrapper(csv_data, encoding='utf-8'))

        pdf_data = BytesIO()
        doc = SimpleDocTemplate(pdf_data, pagesize=letter)
        styles = getSampleStyleSheet()
        elements = []

        # Cabeçalho
        header = Paragraph("<b>Ficha de Treino</b>", styles['Title'])

        # Dados da tabela
        data_list = [['Treino', 'Exercício', 'Séries', 'Repetições', 'Descanso (segundos)']] 
        for row in reader:
            treino = row['Treino']
            exercicio = row['Exercício']
            serie = row['Séries']
            repeticao = row['Repetições']
            descanso = row['Descanso (segundos)']
            data_list.append([treino, exercicio, serie, repeticao, descanso])

        table = Table(data_list)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))


        elements.append(header)
        elements.append(Spacer(1, 12))
        elements.append(table)
        doc.build(elements)

        pdf_data.seek(0)  # Volte para o início do objeto BytesIO

        response = make_response(pdf_data.read())
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'inline; filename=usuario.pdf'

        return response
    
    return "Nenhum dado disponível para gerar o PDF."


if __name__ == '__main__':
    app.run(debug=True)