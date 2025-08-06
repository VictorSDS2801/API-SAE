from flask import Flask, request, jsonify, render_template
from scrapper import pegar_atividades

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/atividades', methods=['POST'])
def atividades():
    data = request.get_json()

    usuario = data.get('usuario')
    senha = data.get('senha')

    if not usuario or not senha:
        return jsonify({"erro": "Erro ao acessar o SAE. Verifique usuário e senha."}), 500
    try:
        atividades = pegar_atividades(usuario, senha)
        return jsonify({"atividades": atividades})
    
    except Exception as e:
        return jsonify({"erro": str(e)}), 500
    
           


if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)