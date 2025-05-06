# Solicita os dois números do usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Solicita a operação desejada
print("Escolha a operação:")
print("1 - Adição (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)")
operacao = input("Digite o símbolo da operação (+, -, *, /): ")

# Realiza a operação escolhida
if operacao == '+':
    resultado = num1 + num2
    print(f"{num1} + {num2} = {resultado}")
elif operacao == '-':
    resultado = num1 - num2
    print(f"{num1} - {num2} = {resultado}")
elif operacao == '*':
    resultado = num1 * num2
    print(f"{num1} * {num2} = {resultado}")
elif operacao == '/':
    if num2 != 0:
        resultado = num1 / num2
        print(f"{num1} / {num2} = {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Operação inválida. Por favor, escolha +, -, * ou /.")
