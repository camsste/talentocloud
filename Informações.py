def obter_informacoes_usuario():
    while True:
        nome = input("Digite seu nome completo: ")
        ano_nascimento = input("Digite seu ano de nascimento (entre 1922 e 2021): ")
        
        try:
            ano_nascimento = int(ano_nascimento)
            if 1922 <= ano_nascimento <= 2021:
                break
            else:
                print("Ano inválido. Por favor, insira um ano entre 1922 e 2021.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido para o ano de nascimento.")
    
    idade = 2022 - ano_nascimento
    print(f"Nome: {nome}, Idade: {idade}")

if __name__ == "__main__":
    obter_informacoes_usuario()
