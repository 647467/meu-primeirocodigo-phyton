produto1 = float(input("Digite o valor do produto 1: "))
produto2 = float(input("Digite o valor do produto 2: "))
soma = desconto = produto1 + produto2

if produto1 >= 500:
    desconto15 = soma * 0.15
    print("Desconto: 15%", desconto15)

elif produto2 >= 300:
    desconto10 = soma * 0.10
    print("Desconto: 10%", desconto10)

elif soma >= 150:
    desconto0 = soma * 0.00
    print("Desconto: Sem desconto")
else:
    print("Nenhum desconto aplicado")