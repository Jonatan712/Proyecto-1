print("Coloque el numero de kWh que necesita en su bateria:")

user1 = input()

def kWh_print(x):
    print(x*3393.56)
    
def Precio_return(x):
    return(x*3393.56)

kWh_print(1)

var = Precio_return(3393.56)
print(var)


user = int(input())
kWh_print(user)
var = Precio_return(user)

print("Precio en pesos mexicanos")


