def calculadora():
    while True:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação   (+, -, *, /): ")

        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            if num2 == 0:
                print("Erro:.")
            else:
                resultado = num1 / num2
        else:
            print("Operação inválida.")
            continue

        print("Resultado:", resultado)

        continuar = input("Deseja continuar? (s/n): ")
        if continuar.lower() != 's':
            break

calculadora()