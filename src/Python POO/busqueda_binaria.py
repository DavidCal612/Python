import random

def busqueda_binaria(Lista, comienzo, final, objetivo):
    print(f'buscando {objetivo} entre {Lista[comienzo]} y {Lista[final - 1]}')
    
    if comienzo > final:
        return False
    
    medio = (comienzo + final  ) // 2
    
    if Lista(medio) == objetivo:
        return True
    elif Lista(medio) < objetivo:
        return busqueda_binaria(Lista, medio + 1, final, objetivo )
    else:
      return busqueda_binaria(Lista, comienzo, medio - 1 , objetivo )
    
    
    
if __name__ == '__main__':
    tamaño_de_lista = int(input('¿De que tamaño es la lista? '))
    objetivo = int(input('¿Que numero quieres encontrar? '))
    
    Lista = sorted([random.randint(0, 100) for i in range(tamaño_de_lista)])
    encontrado = busqueda_binaria(Lista, 0, len(Lista), objetivo)
    
    
    print(Lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
    