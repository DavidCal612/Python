import random


def ordenamiento_de_burbuja(lista):
    n = len(lista)
    
    for i in range(n):
        for j in range(0, n - i - 1): # 0(n) * 0(n) = 0(n * n ) = 0 (n**)
            
            if lista[j] > lista [j + 1]:
                lista[j], lista [j + 1] = lista[j + 1], lista [j]
                
    return lista
        
if __name__ == '__main__':
    tamaño_de_lista = int(input('De que tamaño sera la lista'))
    
    lista = [random.randint(0, 100) for i in range(tamaño_de_lista)]
    print(lista)
    
    lista_ordenada = ordenamiento_de_burbuja(lista)
    print(lista_ordenada)