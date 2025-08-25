# obter os npumeros pares da lista e somá-los
num = [1,2,3,5,93,7,6,88]
num_par = []
for x in num:
    if x % 2 == 0:
        num_par.append(x)

# exibir os valores pares que estão dentro da lista num_par
for i in num_par:
    print(i)

