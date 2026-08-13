import csv

ARQUIVO = 'livros.csv'
livros = []


# Função para cadastrar livros, com status padrão "disponivel".
def cadastro_livros(titulo, autor, codigo, ano, status="disponivel"):
    livro = {"titulo": titulo,"autor": autor,"codigo": codigo,"ano": ano,"status": status}

    with open(ARQUIVO,'a',encoding='UTF-8',newline='') as arquivo:
        cabecalho = ["titulo","autor","codigo","ano","status"]
        escritor = csv.DictWriter(arquivo,fieldnames=cabecalho)
        escritor.writerow(livro)



# Função para emprestar livros e mostrar o status.
def emprestar_livro(codigo):
    with open(ARQUIVO,'r',encoding='UTF-8',newline='') as arquivo:
            cabecalho = ["titulo","autor","codigo","ano","status"]
            leitor = csv.DictReader(arquivo,fieldnames=cabecalho)
            livros.clear()
            for livro in leitor:
                livros.append(livro)
                
    for livro in livros:
        if livro['codigo'] == codigo:
            if livro['status'] == "disponivel":
                livro['status'] = "emprestado"
                with open(ARQUIVO,'w',encoding='UTF-8',newline='') as arquivo:
                    cabecalho = ["titulo","autor","codigo","ano","status"]
                    escritor = csv.DictWriter(arquivo,fieldnames=cabecalho)
                    escritor.writeheader()
                    escritor.writerows(livros)
                        
                return "Livro emprestado com sucesso!"
            else:
                return "Esse livro já está emprestado."

    return "Livro não encontrado."

# Função para devolver livros e mostrar o status.
# Função para devolver livros e mostrar o status.
def devolver_livro(codigo):
    with open(ARQUIVO, 'r', encoding='UTF-8', newline='') as arquivo:
        leitor = csv.DictReader(arquivo)

        livros.clear()

        for livro in leitor:
            livros.append(livro)

    for livro in livros:
        if livro['codigo'] == codigo:
            if livro['status'] == "emprestado":
                livro['status'] = "disponivel"

                with open(ARQUIVO, 'w', encoding='UTF-8', newline='') as arquivo:
                    cabecalho = ["titulo", "autor", "codigo", "ano", "status"]
                    escritor = csv.DictWriter(arquivo, fieldnames=cabecalho)
                    escritor.writeheader()
                    escritor.writerows(livros)

                return "Livro devolvido com sucesso!"
            else:
                return "Esse livro já está disponível."

    return "Livro não encontrado."

# Função para listar livros cadastrados, mostrando título, autor, código, ano e status.
def listar_livros():
    with open(ARQUIVO, 'r', encoding='UTF-8', newline='') as arquivo:
        cabecalho = ["titulo", "autor", "codigo", "ano", "status"]
        leitor = csv.DictReader(arquivo, fieldnames=cabecalho)

        livros.clear()

        for livro in leitor:
            livros.append(livro)

    print("\n===== LIVROS CADASTRADOS =====")

    for livro in livros:
        print(f"Título: {livro['titulo']}")
        print(f"Autor: {livro['autor']}")
        print(f"Código: {livro['codigo']}")
        print(f"Ano: {livro['ano']}")
        print(f"Status: {livro['status']}")

# Função para buscar livros pelo título ou autor.
def buscar_livro(tipo, nome):
    with open(ARQUIVO,'r',encoding='UTF-8',newline='') as arquivo:
        cabecalho = ["titulo","autor","codigo","ano","status"]
        leitor = csv.DictReader(arquivo,fieldnames=cabecalho)
        for livro in leitor:
            livros.append(livro)

    for livro in livros:
        if tipo == "titulo" and livro['titulo'] == nome:
            return livro
        elif tipo == "autor" and livro['autor'] == nome:
            return livro

    return "Livro não encontrado."

    # Função para ordenar os livros por título, autor ou ano.
def ordenar_livros(tipo):
    with open(ARQUIVO, 'r', encoding='UTF-8', newline='') as arquivo:
        cabecalho = ["titulo", "autor", "codigo", "ano", "status"]
        leitor = csv.DictReader(arquivo, fieldnames=cabecalho)

        livros.clear()

        for livro in leitor:
            livros.append(livro)

    livros_ordenados = livros.copy()

    for i in range(len(livros_ordenados)):
        for j in range(i + 1, len(livros_ordenados)):

            if tipo == "titulo" and livros_ordenados[i]["titulo"] > livros_ordenados[j]["titulo"]:
                troca = livros_ordenados[i]
                livros_ordenados[i] = livros_ordenados[j]
                livros_ordenados[j] = troca

            elif tipo == "autor" and livros_ordenados[i]["autor"] > livros_ordenados[j]["autor"]:
                troca = livros_ordenados[i]
                livros_ordenados[i] = livros_ordenados[j]
                livros_ordenados[j] = troca

            elif tipo == "ano" and livros_ordenados[i]["ano"] > livros_ordenados[j]["ano"]:
                troca = livros_ordenados[i]
                livros_ordenados[i] = livros_ordenados[j]
                livros_ordenados[j] = troca

    for livro in livros_ordenados:
        print(f"Título: {livro['titulo']}")
        print(f"Autor: {livro['autor']}")
        print(f"Código: {livro['codigo']}")
        print(f"Ano: {livro['ano']}")
        print(f"Status: {livro['status']}")
        print()

# Função para exibir o menu e receber a opção do usuário.
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

    elif opcao == "5":
        tipo = input("Digite titulo ou autor: ")
        nome = input("Digite o título ou autor: ")
        resultado = buscar_livro(tipo, nome)
        print(resultado)

    elif opcao == "6":
         tipo = input("Digite titulo, autor ou ano: ")
         ordenar_livros(tipo)  

    elif opcao == "7":
        print("Programa encerrado!")
        break

    else:
        print("Opção inválida!")