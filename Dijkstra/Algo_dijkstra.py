# Importando a biblioteca heapq para usar a fila de prioridade
import heapq

# Função para calcular o algoritmo de Dijkstra em um grafo
def calcular_dijkstra(grafo, origem):
    # Inicializa as distâncias de todos os vértices como infinito
    distancias = {vertice: float('infinity') for vertice in grafo}
    # A distância do vértice de origem para ele mesmo é 0
    distancias[origem] = 0
    # Cria uma fila de prioridade com a tupla (distância, vértice)
    fila = [(0, origem)]

    # Enquanto houver vértices na fila de prioridade
    while fila:
        # Remove o vértice com menor distância da fila
        distancia_atual, vertice_atual = heapq.heappop(fila)

        # Se a distância atual for maior do que a distância registrada para o vértice, pula para a próxima iteração
        if distancia_atual > distancias[vertice_atual]:
            continue

        # Itera pelos vizinhos do vértice atual
        for vizinho, peso in grafo[vertice_atual].items():
            # Calcula a nova distância até o vizinho
            distancia = distancia_atual + peso
            # Se a nova distância for menor do que a distância registrada para o vizinho, atualiza a distância
            # e adiciona o vizinho à fila de prioridade
            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                heapq.heappush(fila, (distancia, vizinho))

    # Retorna um dicionário contendo os menores caminhos até cada vértice
    return distancias

# Exemplo de uso:
# grafo_str = '{"A": {"B": 5, "C": 3, "D": 2}, "B": {"A": 5, "C": 2, "E": 4}, "C": {"A": 3, "B": 2, "D": 1}, "D": {"A": 2, "C": 1, "E": 7}, "E": {"B": 4, "D": 7}}'
# grafo = json.loads(grafo_str)  # Converte a string JSON em um dicionário Python
# resultado = calcular_dijkstra(grafo, 'A')  # Calcula o menor caminho a partir do vértice 'A'
# print(resultado)  # Imprime o resultado
