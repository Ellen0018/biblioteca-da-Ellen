import csv
 
ARQUIVO = 'livros.csv'
def cadastro_livros(titulo, autor, codigo, ano, status= "disponivel"):
    livros = []
    livros.append ([titulo,autor,codigo,ano,status])

def menu():
    print("Menu")
    print("1 - Cadastro de livros")
    opcao = int(input("Digite a opção selecionada: "))
    if  opcao == 1:
           titulo = input ("Digite o título: ")
           autor = input ("Digite o autor: ")
           codigo = input("Digite o código:")
           ano = input ("Digite o ano: ")
           cadastro_livros(titulo,autor,codigo,ano)
           print ("livro cadastrado!")
   
menu()
 