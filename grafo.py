# Importa as bibliotecas necessárias
from flask import Flask, render_template, request, jsonify
from Dijkstra.Algo_dijkstra import calcular_dijkstra  # Importa a função calcular_dijkstra do módulo Algo_dijkstra
import json

# Inicializa a aplicação Flask
app = Flask(__name__)


# Rota principal que renderiza o template "grafo_entrada.html"
@app.route('/')
def index():
    return render_template('grafo_entrada.html')


# Rota para calcular o menor caminho em um grafo recebido como JSON
@app.route('/calcular', methods=['POST'])
def calcular():
    try:
        # Obtém o grafo como uma string JSON do formulário e converte para um dicionário Python
        grafo_str = request.form['grafo']
        grafo = json.loads(grafo_str)

        # Chama a função calcular_dijkstra para calcular o menor caminho no grafo
        resultado = calcular_dijkstra(grafo, 'A')

        # Retorna o resultado como uma resposta JSON
        return jsonify(resultado)
    except json.JSONDecodeError:
        # Se houver um erro de decodificação JSON, retorna um erro 400 Bad Request como uma resposta JSON
        return jsonify({'erro': 'Formato JSON inválido'}), 400


# Inicializa a aplicação Flask para execução
if __name__ == '__main__':
    # Permite acesso externo à aplicação na porta 4000 e ativa o modo de depuração
    app.run(host="0.0.0.0", port=4000, debug=True)
