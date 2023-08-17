# Verificar se um número é maior ou menor que 0
numero = int(input("Digite o número: "))

if (numero > 0):
    print(f"{numero} é positivo.")
elif (numero < 0):
    print(f"{numero} é negativo.")
else:
    print("O número é igual a 0")