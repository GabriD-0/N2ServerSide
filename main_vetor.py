# Importando bibliotecas necessárias
import time
from flask import Flask, render_template, request, redirect, url_for, jsonify
from Vetor import vetor  # Importa o módulo "vetor" que contém a função "mergeSort"

# Inicializando a aplicação Flask
app = Flask(__name__)


# Rota principal que renderiza o template "vetor.html"
@app.route("/")
def index():
    return render_template('vetor.html')


# Rota que recebe parâmetros e retorna uma resposta JSON
@app.route('/success/<name>/<tempo>')
def success(name, tempo):
    # Cria um dicionário com os dados de ordenação e tempo
    response = {
        'ordenado': name,
        'tempo': tempo
    }
    # Converte o dicionário para JSON e retorna como resposta
    return jsonify(response)


# Rota para lidar com a ordenação do vetor
@app.route("/rotaOrdenacao", methods=['POST'])
def ordenacao():
    if request.method == 'POST':
        # Obtém os números do formulário e converte para uma lista de inteiros
        any_numbers = request.form.get('ordenacao')
        any_numbers_list = list(map(int, any_numbers.split(",")))

        # Mede o tempo de execução da ordenação usando o algoritmo mergeSort
        inicio = time.time()
        vetor.mergeSort(any_numbers_list)
        fim = time.time()

        # Calcula o tempo de execução em milissegundos
        tempo_execucao = (fim - inicio) * 1000

        # Redireciona para a rota 'success' passando os dados de ordenação e tempo
        return redirect(url_for('success', name=any_numbers_list, tempo=tempo_execucao))


# Inicializa a aplicação Flask na porta 3000 e permite acesso externo (host="0.0.0.0")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
