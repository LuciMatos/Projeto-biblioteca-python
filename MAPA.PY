biblioteca = []
cod = 0

while True:
    print('-=' * 30)
    print("Opções\n"
    "[1] Inserir um novo cadastro\n"
    "[2] Mostrar todos os cadastros\n"
    "[0] Encerrar!")
    opcao = int(input("Escolha uma opção:"))

    if opcao == 1:
        if len(biblioteca) < 5:

            livro = dict()
            cod = cod + 1

            autor = str(input("Digite o nome do autor:"))
            obra = str(input("Digite  nome da obra:"))
            editora = str(input("Digite o nome da editora:"))

            livro['cod'] = cod
            livro['autor'] = autor
            livro['obra'] = obra
            livro['editora'] = editora

            biblioteca.append(livro)
        else:
            print("ERRO! Sistema de cadastro lotado.")
    elif opcao == 2:
        if len(biblioteca) == 0:
            print('-=' * 30)
            print("Lista Vazia!")
        else:
            print(biblioteca)
    elif opcao == 0:
        print('-=' * 30)
        print("Programa encerrado!")
        break
    else:
        print("ERRO!Opção Inválida!")

print('-=' * 30)