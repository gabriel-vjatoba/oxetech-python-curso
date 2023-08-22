salario = float(input("Digite seu salário: "))

if (salario <= 280):
    print(f'Anterior: {salario}, Aumento: 20% - {salario * 0.20}, Novo: {salario +  0.20 * salario}')
elif (salario <= 7000):
    print(f'Anterior: {salario}, Aumento: 15% - {salario * 0.15}, Novo: {salario +  0.15 * salario}')
elif (salario <= 1500):
    print(f'Anterior: {salario}, Aumento: 10% - {salario * 0.10}, Novo: {salario +  0.10 * salario}')
else:
    print(f'Anterior: {salario}, Aumento: 5% - {salario * 0.05}, Novo: {salario +  0.05 * salario}')
