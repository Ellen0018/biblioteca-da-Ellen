import csv
 
ARQUIVO = 'livros.csv'
def cadastro_livros(titulo, autor, codigo, ano, status= "disponivel"):
    livros = []
    livros.append ([titulo,autor,codigo,ano,status])

def menu():
    print("\n===== MENU DA BIBLIOTECA =====")
    print("1 - Cadastrar livro")
    print("2 - Emprestar livro")
    print("3 - Devolver livro")
    print("4 - Listar livros")
    print("5 - Buscar livro")
    print("6 - Ordenar livros")
    print("7 - Sair")

    opcao = input("Digite a opção desejada: ")

    return opcao
# Mantém o menu funcionando até o usuário escolher sair.
while True:
    opcao = menu()

    if opcao == "1":
        titulo = input("Digite o título: ")
        autor = input("Digite o autor: ")
        codigo = input("Digite o código: ")
        ano = input("Digite o ano: ")

        cadastro_livros(titulo, autor, codigo, ano)
        print("Livro cadastrado!")

    elif opcao == "7":
        print("Programa encerrado!")
        break

    else:
        print("Opção inválida!")