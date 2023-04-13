def selection_sort(arr):
    n = len(arr) # n receberá o tamanho do array 
    for i in range(n):
        # Encontra o índice do menor elemento restante
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
                
        # Troca o menor elemento encontrado com o primeiro elemento restante
        arr[i], arr[min_index] = arr[min_index], arr[i]
       
    return arr

# EXEMPLIFICANDO 

arr = [92, 36, 15, 22, 10]
selection_sort(arr)
print(arr)

#ordena lista  