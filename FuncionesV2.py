print("Más sobre funciones")
# aqui se escriben las funciones
def suma_ab(a,b):
    s=a+b
    return s

def resta_ab(a,b):
    r=a-b
    return r

def mul_ab(a,b):
    m=a*b
    return m


def div_ab(a,b):
    d=a/b
    return d

#llamando a funciones
print(" \n Calculando suma")
n1=int(input("ingresa el primer numero "))
n2=int(input("ingresa el segundo numero "))
suma=suma_ab(n1,n2)
print(f"La suma de {n1} + {n2} es: {suma}")

print(" \n Calculando resta")
n3=int(input("ingresa el primer numero "))
n4=int(input("ingresa el segundo numero "))
resta=resta_ab(n3,n4)
print(f"La resta de {n3} - {n4} es: {resta}")

print(" \n Calculando multiplicación")
n5=int(input("ingresa el primer numero "))
n6=int(input("ingresa el segundo numero "))
mul=mul_ab(n5,n6)
print(f"La multiplicación  de {n5} x {n6} es: {mul}")

print(" \n Calculando división")
n7=int(input("ingresa el primer numero "))
n8=int(input("ingresa el segundo numero "))
div=div_ab(n7,n8)
print(f"La división de {n7} entre {n8} es: {div}")