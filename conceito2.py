nota1 = input("Digite a primeira nota: ")
nota2 = input("Digite a segunada nota: ")
nota3 = input("Digite a terceira nota: ")
nota4 = input("Digite a quarta nota: ")

# Vamos as variáveis de nota para o tipo float
nota1 = float(nota1)
nota2 = float(nota2)
nota3 = float(nota3)
nota4 = float(nota4)

media = (nota1 + nota2 + nota3 + nota4) / 4
# Se a nota média do aluno for igual ou maior que 7, -> Aprovado.
# senão se  a nota média do aluno for  menor ou igual a 4, -> Reprovado
# senão, ->  Recuperação
if media >= 7:
    print("sua nota média é: "+ str(media) +", você etsá Aprovado!!")
elif media <= 4:
    print("Sua nota média: "+ str(media) +", você está Reprovado!!")
else:
    print("Sua nota média é: "+ str(media) +" você está de Recuperação!!")
