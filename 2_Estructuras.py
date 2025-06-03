#if
def dividir():
    a = 2
    b = 2
    if b != 0:
        print(a / b)
#elif y else
def cualNumeroEs(a):
    if a == 5:
        print("Es 5")
    elif a==6:
        print("Es 6")
    elif a==7:
        print("Es 7")
    else:
        print("Es otro numero")

#OperadorTernario /[código si se cumple] if [condición] else [código si no se cumple]
def ternario(a):
    print("Es 5" if a == 5 else "No es 5")


#imprimiendo ejercicios
print (dividir())
print (cualNumeroEs(5))
print (ternario(5))