soma = 0
for i in range(1,11,1):
    num = int(input("Digite seu numero: "))
    soma = num + soma
    media = soma/10
print("A soma é: {}\n A media é: {}".format(soma, media))