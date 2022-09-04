
class Persona:
    
    def __init__(self, nombre):
        self.nombre = nombre
    
    
    def avanza(self):
        print('Ando Caminando')
        
        
class Ciclisa(Persona):
    
    def __init__(self, nombre):
        super().__init__(nombre)
        
    def avanza(self):
        print('Ando moviendome en mi bicicleta')
        
        
        
class Motociclista(Persona):
    
    def __init__(self, nombre):
        super().__init__(nombre)
        
    def manejando(self):
        print('Voy manejando mi bicicleta')
        
        

class Patineta(Persona):
    
    def __init__(self, nombre):
        super() .__init__(nombre)
        
    def montado(self):
       print('voy montando mi panineta') 
        
        
def main():
    persona = Persona('David')
    persona.avanza()
    
    ciclista = Ciclisa('Daniel') 
    ciclista.avanza()   
    
    motociclista = Motociclista('Jorge')
    motociclista.manejando()   
    
    patineta = Patineta('Daniel')
    patineta.montado()

     
    
    
    

if __name__ == '__main__':
        main()
        