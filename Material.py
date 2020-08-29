print("Elija primero que tipo de material utilizara:")

print("Tipos de Materiales: ")
print("Acero ")
print("Fibra de Vidrio ")
print("Aluminio ")
print("Fibra de Carbono ")
print("Vidrio ")

Acero = 40
Fibra_de_Vidrio = 30
Aluminio = 25
Fibra_de_Carbono = 400
Vidrio = 10

user1 = input()

print("Inserte la cantidad de material en Kg")

q = int(input())
    
if(user1 == "Acero"):
    print(q*Acero)
elif(user1 == "Fibra de Vidrio"):
    print(q*Fibra_de_Vidrio)
elif(user1 == "Aluminio"):
    print(q*Aluminio)
elif(user1 == "Fibra de Carbono"):
    print(q*Fibra_de_Carbono)
elif(user1 == "Vidrio"):
    print(q*Vidrio)

print("Precio en pesos mexicanos")
    