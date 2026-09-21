print ("calculadora")

valor01 = float(input("Digite o primeiro valor:"))
valor02 = float(input("Digite o segundo valor:"))
resultadosoma = valor01 + valor02
print("Resultado da soma:", resultadosoma)

valor03 = float(input("Digite o terceiro valor:"))
valor04 = float(input("Digite o quarto valor:"))

resultadosubtracao = valor01 - valor02
print("Resultado da subtração:", resultadosubtracao)

valor05 = float(input("Digite o quinto valor:"))
valor06 = float(input("Digite o sexto valor:"))

resultadodivisao = valor05 / valor06
print("Resultado da divisão:", resultadodivisao)

if resultadosoma > resultadosubtracao:
    print("O resultado da soma é maior que o resultado da subtração")
elif resultadosoma < resultadosubtracao:
    print("O resultado da soma é menor que o resultado da subtração")
else:
    print("Os resultados são iguais.")