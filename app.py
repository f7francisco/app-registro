from flask import Flask, request, send_file, render_template
from datetime import datetime
import pandas as pd

app = Flask(__name__)
registros = []

@app.route('/')
def index():
    return render_template('index.html', registros=registros)

@app.route('/inserir', methods=['POST'])
def inserir():
    nome = request.form.get('nome')
    endereco = request.form.get('endereco')
    latitude = request.form.get('latitude') or 'N/A'
    longitude = request.form.get('longitude') or 'N/A'
    data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    registros.append({
        'Nome': nome,
        'Endereço': endereco,
        'Data/Hora': data_hora,
        'Latitude': latitude,
        'Longitude': longitude
    })

    return render_template('index.html', registros=registros)

@app.route('/exportar')
def exportar():
    if not registros:
        return "Nenhum registro para exportar."
    df = pd.DataFrame(registros)
    arquivo = 'registros.xlsx'
    df.to_excel(arquivo, index=False)
    return send_file(arquivo, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
@app.route('/limpar')
def limpar():
    registros.clear()
    return render_template('index.html', registros=registros)

