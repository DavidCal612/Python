def run ():
    mi_diccionario ={
        'llave1' : 1,
        'llave2' : 2,
        'llave3' : 3,
        
    }
    
   # print(mi_diccionario['llave1])
   # print(mi_diccionario['llave2'])
   # print(mi_diccionario['llave3'])
    
    poblacion_paises = {
       'Argentina': 449387,
       'Brasil':  210147125,
       'Bolivia': 116700000,
       'Colombia': 50372424,
       'Chile': 191200000,
       'Mexico': 128900000,
       'Peru': 329700000,
       'Paraguay': 347400000,
       'Uruguay': 713300000
       
   }
    
    # print(poblacion_paises['Bolivia'])

    #for pais in poblacion_paises.keys():
     # print(pais)
     
   # for pais in poblacion_paises.values():
        #print(pais)         
    for pais, poblacion in poblacion_paises.items():
        print(pais + ' tiene ' + str(poblacion) + ' habitantes ')                                                    
     
if __name__ == '__main__':
    run()    