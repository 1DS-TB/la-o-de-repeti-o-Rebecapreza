n = int(input("Digite um número para realizar a sequência de Fibonacci: "))
ult=1
pnt=1

if (n==1) or (n==2):
    print("1")
else:
    conta = 3
    while conta <= n:
        trm = ult + pnt
        pnt = ult
        ult = trm
        conta += 1
    print(trm)