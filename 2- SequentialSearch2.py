def sequentialsearch2(lista, valor):
    
    def sequentialsearch2_rec(lista, valor, i): 

        #lista= lista a ser buscada 
        #valor=valor a ser encontrado
        #i= índice i do elemento a ser comparado naquele momento

        
        if i >= len(lista):  # se o índice i ultrapassar tamanho da lista e o valor não foi encontrado
            return None
        
        elif lista[i] == valor:  # o valor "valor" foi encontrado na posição i
            return i
        else:
            return sequentialsearch2_rec(lista, valor, i+1)  # recursão
        #o valor "valor" não foi encontrado na posição i da lista,
        #  portanto, é necessário continuar a busca recursivamente no próximo elemento da lista,
        #  passando o índice i+1 como parâmetro.

    return sequentialsearch2_rec(lista, valor, 0) #índice do elemento encontrado ou None, caso contrário

#EXEMPLO

lista=[1,2,20,10,30,40]
valor=10

imprime=sequentialsearch2(lista, valor)

print(imprime)