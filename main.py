import csv
 
ARQUIVO = 'livros.csv'
livros = []
def cadastro_livros(titulo, autor, codigo, ano, status= "disponivel"):
    livros.append ([titulo,autor,codigo,ano,status])

def emprestar_livro(codigo):
     for livro in livros:
        if livro[2] == codigo:
            if livro[4] == "disponivel":
                livro[4] = "emprestado"
                return "Livro emprestado com sucesso!"
            else:
                return "Esse livro já está emprestado."

            return "Livro não encontrado."
        
def devolver_livro(codigo):
    for livro in livros:
        if livro[2] == codigo:
            if livro[4] == "emprestado":
                livro[4] = "disponivel"
                return "Livro devolvido com sucesso!"
            else:
                return "Esse livro já está disponível."

    return "Livro não encontrado."

def listar_livros():
 print("\n===== LIVROS CADASTRADOS =====")
 for livro in livros:
        print(f"Título: {livro[0]}")
        print(f"Autor: {livro[1]}")
        print(f"Código: {livro[2]}")
        print(f"Ano: {livro[3]}")
        print(f"Status: {livro[4]}")

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

    elif opcao == "2":
        codigo = input("Digite o código do livro: ")
        mensagem = emprestar_livro(codigo)
        print(mensagem)

    elif opcao == "3":
        codigo = input("Digite o código do livro: ")
        mensagem = devolver_livro(codigo)
        print(mensagem)
        
    elif opcao == "4":
        listar_livros()

    elif opcao == "7":
        print("Programa encerrado!")
        break

    else:
        print("Opção inválida!")
