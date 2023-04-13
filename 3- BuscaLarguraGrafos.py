from collections import deque

# classe para representar um nó do grafo
class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []


def bfs(noinicial, target_value):# função que realiza a busca em largura
   
    queue = deque() # fila para armazenar os nós a serem visitados
   
    visited = set() # conjunto para armazenar os nós já visitados

    
    queue.append(noinicial)# adiciona o nó inicial à fila e ao conjunto de visitados
    visited.add(noinicial)


    while queue:    # enquanto a fila não estiver vazia
        
        current_node = queue.popleft()# remove o próximo nó da fila

        
        if current_node.value == target_value:# verifica se é o nó que estamos procurando
            return current_node

      
        for neighbor in current_node.neighbors:  
            # adiciona os vizinhos do nó atual à fila, se ainda não foram visitados
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

    return None    # se não encontramos o nó procurado, retorna None


# cRIANDO OS nÓS DO GRAFO 
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

# conecta os nós do grafo
node1.neighbors = [node2, node3]
node2.neighbors = [node4]
node3.neighbors = [node4, node5]
node4.neighbors = [node5]

# busca o nó com valor 5 a partir do nó inicial (valor 1)
result_node = bfs(node2, 5)

# imprime o resultado
if result_node:
    print(f"Encontrado o nó com valor {result_node.value}")
else:
    print("Nó não encontrado")
