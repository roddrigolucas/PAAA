
class Node:# Classe que representa um nó do grafo
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.adj_list = []

 
    def add_neighbor(self, neighbor):   # Adiciona um nó vizinho a este nó
        self.adj_list.append(neighbor)


    def get_neighbors(self):    # Retorna os vizinhos deste nó
        return self.adj_list


class Graph:# Classe que representa o grafo
    def __init__(self):
        self.nodes = []

    def add_node(self, node):  # Adiciona um nó ao grafo
        self.nodes.append(node)

    def get_nodes(self): # Retorna todos os nós do grafo
        return self.nodes

   
    def dfs(self, start_node): # Algoritmo de busca em profundidade
        stack = [start_node]

        while stack:
            node = stack.pop()
            node.visited = True

            print(node.name)

            for neighbor in node.adj_list:
                if not neighbor.visited:
                    stack.append(neighbor)


node1 = Node('A')
node2 = Node('B')
node3 = Node('C')
node4 = Node('D')
node5 = Node('E')

node1.add_neighbor(node2)
node1.add_neighbor(node3)
node2.add_neighbor(node4)
node4.add_neighbor(node5)

graph = Graph()
graph.add_node(node1)
graph.add_node(node2)
graph.add_node(node3)
graph.add_node(node4)
graph.add_node(node5)

graph.dfs(node1)
