for numero in range(1, 10001):
    soma_divisores = 0

    for i in range(1, numero):
        if numero % i == 0:
            soma_divisores += i
    if soma_divisores == numero:
        print(numero)
