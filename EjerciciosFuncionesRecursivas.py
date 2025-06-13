def contarDes(numero):
    print(numero)
    numero = numero - 1
    if( numero > 0):
        contarDes(numero)

contarDes(5)