# PAAA

1 SELECTION SORT

1.1	Definição
É um algoritmo de ordenação simples que percorre um array . Realiza a busca do menor elemento e o coloca na primeira posição , em seguida repete o processo até que o array fique completamente ordenado. 

1.3	Resumo

A Função selection_sort( ) receberá uma lista de números desordenados e irá retornar a mesma lista de forma ordenada em ordem crescente.


1.4	Análise de complexidade de tempo do algoritmo

a)	Expressão Matemática:Neste cenário, podemos fazer a análise de dois aspectos: Número de comparações e Número de trocas realizadas 


Número de Comparações: O número de comparações é dado por (n-1) + (n-2) + ... + 2 + 1, onde n é o tamanho do array. Isso pode ser simplificado como a soma dos primeiros n-1 números naturais, que é igual a n*(n-1)/2.

Para isso, obtemos: O(n^2)


Número de Trocas: Como o menor elemento é trocado no maximo uma vez com cada um dos outros elementos , temos n-1. 


Para isso, obtemos: O(n)

Observa-se que a analise de complexidade dominante neste caso é o O(n^2) o que implica que a execução deste algortimo aumenta quadraticamente com o tamanho do array.


b)	Cálculo da Função de Custo

O algoritmo executa n-1 iterações no loop externo, onde n é o numero de elementos no array. Já no loop interno executa n-i iterações para encontrar o menor elemento restante e realiza em seguida uma única troca se necessário.Logo, temos o número total de operações básicas expressa por:


T(n) = (n-1) * (n + (n-1) + (n-2) + ... + 2 + 1) + (n-1)
= (n-1) * ((n*(n+1))/2) + (n-1)
= (n^2 - n) / 2 + n - 1
= (n^2 + n - 2) / 2
T(n)= (n^2 + n - 2) / 2





c)	Indicação da Classe de Eficiência

O(n^2) . Pois o tempo de execução é o quadrado ao número de elementos. 


Observa-se que para N muito grande fica inviável utilizar este algoritmo  devido ao tempo de execução do algoritmo . Entretanto, as vezes pode ser interessante quando por exemplo, o espaço de memória é limitado ou quando ao se ter o conhecimento do array,  observa-se que o mesmo está quase ordenado.

2	SEQUENTIAL SEARCH 2

2.1	Definição
Um algoritmo Sequential Search ou Busca Sequencial em português, é uma técnica de busca que percorre uma lista de elementos, comparando-os com o valor que se deseja encontrar . Já o algoritmo Sequentialsearch2 é uma variação do Sequential Search com execução de buscas de forma recursiva.

2.2	 Implementação em Python
 










2.3 Resumo

A função sequentialsearch2 retorna o resultado da função recursiva sequentialsearch2_rec, passando como parâmetros a lista “lista”, o valor “valor” e o índice inicial 0

2.4 Análise de complexidade de tempo do algoritmo

a)	Expressão Matemática: É dada pelo numero de comparações necessárias para encontrar o valor “valor” na lista “lista” , onde no pior caso onde o valor não estiver presente na lista , serão feitas n comparações, onde n é o tamanho da lista. Como o número de chamadas recursivas é igual ao número de elementos na lista (n), a complexidade de tempo do algoritmo é O(n) 


Para isso, obtemos: T(n) = O(n)


b)	Cálculo da Função de Custo

Se assumirmos que  comparação entre dois valores na lista como operação básica, a função de custo é expressa por:

T(n) = c1 + T(n-1) 

Onde C1 representa o custo da compartação entre dois valores na lista e T(N-1) o tempo necvessário para buscar o valor na lista com n-1 elementos, logo temos:

T(n) = c1 + c1 + T(n-2)
T(n) = c1 + c1 + c1 + T(n-3)
...
T(n) = k*c1 + T(n-k)

onde k é o número de comparações realizadas até o momento, e T(0) = 0.

T(n) = n*c1 para o pior caso





c)	Indicação da Classe de Eficiência



 
FONTE: https://www.wolframalpha.com/


Sua complexidade O(n) é linear , onde n é o tamanho da lista. O tempo de execução do algoritmo cresce de forma proporcional ao tamanho da lista. No pior caso onde o valor procurado não estiver na lista é feita n comparações. Ideal para listas pequenas ou com poucos elementos.


3	BUSCA EM LARGURA PARA GRAFOS
3.1	Definição
Um algoritmo de busca em largura para Grafos , é usado para percorrer todos os nós de um grafo de forma sistemática e em camadas, visitando cada nó uma única vez, até encontrar um nó com um determinado valor ou até que todos os nós tenham sido visitados.

3.2	 Implementação em Python
 



 






3.3	Resumo


O algoritmo começa visitando o nó inicial e depois visita todos os seus vizinhos. Em seguida, visita os vizinhos desses vizinhos, e assim por diante, até que todos os nós do grafo tenham sido visitados ou o nó procurado tenha sido encontrado.

O algoritmo utiliza uma fila para armazenar os nós a serem visitados e um conjunto para armazenar os nós já visitados, garantindo que cada nó seja visitado no máximo uma vez. Como o algoritmo visita todos os nós em uma camada antes de passar para a próxima camada, ele é garantido de encontrar o caminho mais curto entre o nó inicial e qualquer outro nó no grafo






3.4	Análise de complexidade de tempo do algoritmo

a)	Expressão Matemática: É dada em termos do número de nos (|V|) e arestas (|E|) do grafo. Cada nó é visitado e, em seguida, seus vizinhos são adicionados à fila. Portanto, cada nó é visitado e adicionado à fila exatamente uma vez. Além disso, cada aresta é percorrida exatamente duas vezes: uma vez quando é adicionada à lista de vizinhos de um nó e outra vez quando o nó correspondente é visitado 


Para isso, obtemos: O(|V| + |E|)

b)	Cálculo da Função de Custo


A função de custo C(n) do algoritmo de busca em largura para grafos é a quantidade de operações elementares realizadas pelo algoritmo ao visitar um nó n e seus vizinhos. Isso inclui adicionar o nó n à lista de visitados, adicionar seus vizinhos à fila e remover o nó da fila quando ele é visitado.

C(n) = O(1)






c)	Indicação da Classe de Eficiência

O(|V| + |E|), onde |V| é o número de nós do grafo e |E| é o número de arestas.

O(n), onde n é o tamanho do grafo. Essa classe de eficiência indica que o algoritmo é bastante eficiente e pode ser usado para encontrar o caminho mais curto entre dois nós em grafos grandes.


 

4	BUSCA EM PROFUNDIDADE PARA GRAFOS
4.1	Definição

O algoritmo utiliza uma pilha para manter uma lista de nós a serem visitados e um loop enquanto a pilha não estiver vazia. A cada iteração, o nó no topo da pilha é removido e marcado como visitado, e seus vizinhos não visitados são adicionados à pilha.
4.2	Implementação em Python
 





 






4.3	Resumo


O algoritmo utiliza uma pilha para manter uma lista de nós a serem visitados e um loop enquanto a pilha não estiver vazia. A cada iteração, o nó no topo da pilha é removido e marcado como visitado, e seus vizinhos não visitados são adicionados à pilha. 














4.4	Análise de complexidade de tempo do algoritmo

d)	Expressão Matemática: o tempo de execução do algoritmo de busca em profundidade é proporcional ao número de nós e arestas no grafo, e é uma função linear do tamanho do grafo. Em outras palavras, quanto maior o grafo, mais tempo o algoritmo levará para executar, mas a taxa de crescimento do tempo de execução será linear.


Para isso, obtemos: T(V, E) = O(V + E)

e)	Cálculo da Função de Custo


Podemos calcular a função custo da seguinte forma:

Percorrer todos os V nós do grafo: O(V)
Para cada nó, percorrer todos os seus E vizinhos não visitados: O(E)
Realizar as operações de adicionar e remover elementos da pilha: O(1)
Verificar se um nó foi visitado ou não: O(1)
Imprimir o nome do nó visitado: O(1)

Para isso encontramos:

T(V, E) = O(V + E)





f)	Indicação da Classe de Eficiência

O(V + E), onde V é o número de nós do grafo e E é o número de arestas.


É um algoritmo  considerado eficiente para grafos de tamanho moderado e pequeno, pois, em grafos grandes pode levar um tempo significativo para ser executado. 


