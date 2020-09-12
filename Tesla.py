aceleracion = input("Inserte aceleracion deseada de 0 - 100 km: ")
costo = input("Inserte costo en pesos MXN: ")
Autonomia = input("Autonomia deseada en km: ")
Asientos = input("Numero de Asientos: ")

roadster = 0
models = 0
modelx = 0
cybertruck = 0

if( aceleracion > 0 and aceleracion < 2.1):
    roadster = roadster + 1
    
elif( aceleracion > 2.1 and aceleracion < 2.5):
    models = models + 1
    
elif( aceleracion > 2.5 and aceleracion < 2.8):
    modelx = modelx + 1
    
elif( aceleracion > 2.8 and aceleracion < 6.5):
    cybertruck = cybertruck + 1
    
if( costo > 0 and costo < 875000):
    cybertruck = cybertruck + 1
    
elif( costo > 875000 and costo < 1500000):
    models = models + 1
    
elif( costo > 1500000 and costo < 2100000):
    modelx = modelx + 1
    
elif( costo > 2100000 and costo < 3840000):
    roadster = roadster + 1
    
if( autonomia > 0 and autonomia < 400):
    cybertruck = cybertruck + 1
    
elif( autonomia > 400 and autonomia < 490):
    modelx = modelx + 1
    
elif( autonomia > 490 and autonomia < 560):
    models = models + 1
    
elif( autonomia > 560 and autonomia <1000):
    roadster = roadster + 1
    
if( asientos > 0 and asientos < 3):
    roadster = roadster + 1
    
elif( asientos > 3 and asientos < 5):
    cybertruck = cybertruck + 1
    models = models + 1

elif( aceleracion > 6 and aceleracion < 7):
    modelx = modelx + 1
    


    
if (roadster > models and roadster > modelx and roadster > cybertruck):
    print("roadster")
if (models > roadster and models > modelx and models > cybertruck):
    print("models")
if (modelx > models and modelx > roadster and modelx > cybertruck):
    print("modelx")
if (cybertruck > models and cybertruck > modelx and cybertruck > roadster):
    print("cybertruck")
