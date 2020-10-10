final = []

numero = int(input("Insrte el numero de perfiles que registrara: "))
q = 0
w = 0
person = 1
puerta = 1
acumulador = 0
while acumulador<numero:
    a = str(input("Inserte nombre completo: "))
    b = str(input("Edad: "))
    c = str(input("Sexo: "))
    d = str(input("Estado civil: "))
    e = str(input("Inserte cargo en la empresa: "))
    f = str(input("Nacionalidad: "))
    g = str(input("Numero de Contacto: "))

    persona = [a,b,c,d,e,f,g]
    
    if(person == puerta):
        final.insert([q][w],persona)
        
    puerta = puerta + 1
    person = person + 1
    acumulador = acumulador + 1
    
print(final)
    
m = 1
s = 0
g = 1
while m <= numero:

    print("Escriba",g,"si usted quiere la informacion de",final[s][0])
    s += 1
    g += 1
    m += 1


p = 1
k = int(input())
h = 0
f = 0
while True:
    if(k == p):
        print("Nombre: ",final[h][f])
        f+=1
        print("Edad: ", final[h][f])
        f+=1
        print("Sexo: ", final[h][f])
        f+=1
        print("Estado civil: ", final[h][f])
        f+=1
        print("Cargo en la empresa: ", final[h][f])
        f+=1
        print("Nacionalidad: ", final[h][f])
        f+=1
        print("Numero de contacto: ", final[h][f])
        break
    else:
        p+=1
        h+=1
        

'''
El codigo representa una base de datos que por el momento solo recibe las caracteristicas de dos empleados, esto se puede cambiar
agregando un par de literales mas para que el proceso sea infinito, pero solo se reciben los datos, y al final solo se escribe el
numero relacionado con la persona y con esto se imprime toda la info.

Este codigo es casi igual que el pasado solo que le agregue un par de cosas para que tuviera un mejor funcionamiento, y para que 
este fuera totalmente automatico.
''' 

