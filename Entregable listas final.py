final = [[],[],[],[],[],[],[]]

q = 0
w = 0
person = 1
puerta = 1
acumulador = 0
while acumulador<2:
    a = str(input("Inserte nombre completo: "))
    b = int(input("Edad: "))
    c = str(input("Sexo: "))
    d = str(input("Estado civil: "))
    e = str(input("Inserte cargo en la empresa: "))
    f = str(input("Nacionalidad: "))
    g = int(input("Numero de Contacto: "))

    persona = [a,b,c,d,e,f,g]
    
    if(person == puerta):
        final.insert([q][w],persona)
        
    puerta = puerta + 1
    person = person + 1
    acumulador = acumulador + 1
    
print("Escriba 1 si usted quiere la informacion de",final[0][0])
print("Escriba 2 si usted quiere la informacion de",final[1][0])
k = int(input())
if(k == 1):
    print("Nombre: ",final[0][0])
    print("Edad: ", final[0][1])
    print("Sexo: ", final[0][2])
    print("Estado civil: ", final[0][3])
    print("Cargo en la empresa: ", final[0][4])
    print("Nacionalidad: ", final[0][5])
    print("Numero de contacto: ", final[0][6])
elif(k == 2):
    print("Nombre: ",final[1][0])
    print("Edad: ", final[1][1])
    print("Sexo: ", final[1][2])
    print("Estado civil: ", final[1][3])
    print("Cargo en la empresa: ", final[1][4])
    print("Nacionalidad: ", final[1][5])
    print("Numero de contacto: ", final[1][6])
else:
    print("Error")

'''
El codigo representa una base de datos que por el momento solo recibe las caracteristicas de dos empleados, esto se puede cambiar
agregando un par de literales mas para que el proceso sea infinito, pero solo se reciben los datos, y al final solo se escribe el
numero relacionado con la persona y con esto se imprime toda la info.
''' 


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
