aceleracion = float(input("Inserte aceleracion deseada de 0 - 100 km: "))
costo = float(input("Inserte costo en pesos MXN: "))
autonomia = float(input("Autonomia deseada en km: "))
asientos = float(input("Numero de Asientos: "))

roadster = 0
models = 0
modelx = 0
cybertruck = 0

if( aceleracion >= 0 and aceleracion <= 2.1):
    roadster = roadster + 1
    
elif( aceleracion >= 2.2 and aceleracion <= 2.5):
    models = models + 1
    
elif( aceleracion >= 2.6 and aceleracion <= 2.8):
    modelx = modelx + 1
    
elif( aceleracion >= 2.9 and aceleracion <= 6.5):
    cybertruck = cybertruck + 1
    
if( costo >= 0 and costo <= 875000):
    cybertruck = cybertruck + 1
    
elif( costo >= 875001 and costo <= 1500000):
    models = models + 1
    
elif( costo >= 1500001 and costo <= 2100000):
    modelx = modelx + 1
    
elif( costo >= 2100001 and costo <= 3840000):
    roadster = roadster + 1
    
if( autonomia >= 0 and autonomia <= 400):
    cybertruck = cybertruck + 1
    
elif( autonomia >= 401 and autonomia <= 490):
    modelx = modelx + 1
    
elif( autonomia >= 491 and autonomia <= 560):
    models = models + 1
    
elif( autonomia >= 561 and autonomia <= 1000):
    roadster = roadster + 1
    
if( asientos >= 0 and asientos <= 4):
    roadster = roadster + 1
    
elif( asientos > 4 and asientos < 6):
    cybertruck = cybertruck + 1
    models = models + 1

elif( asientos >= 6 and asientos <= 7):
    modelx = modelx + 1
    


    
if (roadster > models and roadster > modelx and roadster > cybertruck):
    print("El mejor modelo es = roadster")
elif (models > roadster and models > modelx and models > cybertruck):
    print("El mejor modelo es = models")
elif (modelx > models and modelx > roadster and modelx > cybertruck):
    print("El mejor modelo es = modelx")
elif (cybertruck > models and cybertruck > modelx and cybertruck > roadster):
    print("El mejor modelo es = cybertruck")

    
if (roadster == 2 ):
    print("Como segunda opcion seria = roadster")
    
if (models == 2):
    print("Como segunda opcion seria = models")
    
if (modelx == 2):
    print("Como segunda opcion seria = modelx")
    
if (cybertruck == 2):
    print("Como segunda opcion seria = cybertruck")
    
elif (models == 1 and roadster == 1 and modelx == 1 and cybertruck == 1):
    print("Error, intente ser más especifico en los datos")
    

'''    
print(modelx)
print(cybertruck)
print(models)
print(roadster)
'''

    
