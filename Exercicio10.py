inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

for n in range(inicio, fim + 1):
    if n == 1:
        print(1)
    else:
        quadrado = n ** 2
        n_str = str(quadrado)
        digito = len(str(n))

        esq = n_str[:-digito] if n_str[:-digito] else "0"
        dir = n_str[-digito:]

        if dir.strip("0") != "":
            if int(esq) + int(dir) == n:
                print(n)
