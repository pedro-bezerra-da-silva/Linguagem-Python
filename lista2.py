# obter os npumeros pares da lista e somá-los
num = [1,2,3,5,93,7,6,88]
rs = 0


for x in num:
    if x %2 == 0:
        rs = rs + x
        print(x)
print("--------------------------------------------------------------------------")
print("O resultado da soma é "+str(rs))
