

def maleta(tamano_maleta, pesos, valores,  n):
    
    if n == 0 or tamano_maleta == 0:
        return 0
    
    if pesos[n - 1] > tamano_maleta:
        return maleta(tamano_maleta, pesos, valores, n - 1)
    
    return max(valores[n - 1] + maleta(tamano_maleta - pesos[n - 1], pesos, valores, n - 1),
               maleta(tamano_maleta, pesos, valores, n - 1))
    
    
if __name__  == '__main__':
    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    tamano_maleta = 320
    n = len(valores)
    
    resultados = maleta(tamano_maleta, pesos, valores, n)
    print(resultados)
