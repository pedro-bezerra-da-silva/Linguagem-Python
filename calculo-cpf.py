cpf_og = input("Digite o seu CPF sem pontuação: ")
# Criar uma variável para guardar os 9 primeiros digitos
cpf9 = ""
esp = 1

for i in cpf_og:
    if esp > 9:
        break
    esp = esp + 1
    cpf9 = cpf9 + i

# Vamos fazer a variável que guarda os pesos de 10 à 2
peso10 = 10
print(cpf9)
# Variável que irá guadar os resultados da multiplicação
resultado = 0
for x in cpf9:
    resultado = resultado + int((x)*peso10)
    peso10 = peso10 - 1
print(resultado)
# Variável para guardar o resto da divisão
resto = 0
resto = resultado % 11
cpf10 = cpf9
if resto < 2:
    cpf10 = cpf10 + "0"
else :
    cpf10= cpf10+ str(11-resto)
print(resto)



# Variável com 11, que irá até 2
peso11 = 11
print(cpf10)
# Zerar a Variável resultado para on novo cálculo
resultado = 0
for x in cpf10:
    resultado = resultado + (int(x) * peso11)
    peso11 = peso11 - 1

resto = resultado % 11
cpf_final = cpf10
print(resultado)
print(resto)
if resto < 2:
    cpf_final = cpf_final + "0"
else:
    cpf_final = cpf_final + str(11-resto)

# Verificar se o CPF digitado etá correto 
if cpf_og == cpf_final:
    print("CPF Correto!!")
else:
    print("CPF Inválido")