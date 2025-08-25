num_i=input("digite o 1º valor:  ")
num_f=input("Digte o 2º  valor:  ")
# Variável para contar os numeros pares
num_i = int(num_i)
num_f = int(num_f)
qtd = 0
while (num_i<=num_f):
    if num_i % 2 == 0:
        print(num_i)
        qtd = qtd + 1
    num_i =num_i + 1

print("---------------------------------------")
print("A Quantidade de pares"+str(qtd))