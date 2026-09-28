idade = int(input("Qual a sua idade?: "))

if idade <= 11:
    print("você é uma : Criança")
elif idade >= 12 and idade <= 17:
    print("você é um : Adolescente")
elif idade >= 18 and idade <= 59:
    print("você é um : Adulto")
elif idade >= 60:
    print("você é um : Idoso")
else:
    print("você e um")