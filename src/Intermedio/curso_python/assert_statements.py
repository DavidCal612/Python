def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors     

def run():
        
     num = input("Ingresa un numero:  ")
     assert num.isnumeric(), "Debes ingresar un numero"
     print(divisors(int(num)))
     print("Termino mi programa") 
        
    
    
if __name__ ==   '__main__':
    run()