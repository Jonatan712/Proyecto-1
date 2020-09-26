print("Costo vestiduras de piel 10,000 ")
print("Costo llantas premiun 15,000")
print("Costo vinilo en cualquier modelo 20,000")
print("Costo de una bateria 100,000")
print(".")
print("Colocar los montos sin comas")
print(".")
print("Para finalizar los cargos, coloca un 0 como dato para obtener el precio final")
      
cf = 0
m = float(input())

while m != 0:
    if m < 0:
        print("Monto no valido")
    else:
        cf += m
    m = float(input())
if cf > 100000:
    cf -= cf*0.1
    
print("Costo con descuento ;)", cf)

"""
El objetivo de este codigo es crear una base de cobro para asistentes de ventas de carros, un tipo de servicio privado para poder
adquirir elementos de lujo, se colocan las cantidas a agregar y se finaliza con un 0, si los montos finales son mayores a 100,000
se le aplica un 10% de descuento
"""