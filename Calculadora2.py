def calculadora():
    while True:
        print("\nSelecione a operação:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        try:
            operacao = int(input("Digite o número da operação: "))
        except ValueError:
            print("Essa opção não existe.")
            continue

        if operacao == 0:
            print("Saindo...")
            break
        elif operacao not in [1, 2, 3, 4]:
            print("Essa opção não existe.")
            continue

        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite números válidos.")
            continue

        if operacao == 1:
            resultado = num1 + num2
            print(f"Resultado: {num1} + {num2} = {resultado}")
        elif operacao == 2:
            resultado = num1 - num2
            print(f"Resultado: {num1} - {num2} = {resultado}")
        elif operacao == 3:
            resultado = num1 * num2
            print(f"Resultado: {num1} * {num2} = {resultado}")
        elif operacao == 4:
            if num2 != 0:
                resultado = num1 / num2
                print(f"Resultado: {num1} / {num2} = {resultado}")
            else:
                print("Erro: Divisão por zero")

if __name__ == "__main__":
    calculadora()
