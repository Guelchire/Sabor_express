import os

restaurantes = [{'nome':'Pastelito', 'categoria':'Pastel', 'ativo':False},
                {'nome':'Divino fogão', 'categoria':'Brasileira', 'ativo':True},
                {'nome':'Paulistinha', 'categoria':'Pizza', 'ativo':False}
]

def exibir_nome_do_programa():
    '''Exibir nome do programa'''
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    '''Exibir opções do sistema'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alterar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    ''' função para finalizar o app'''
    exibir_subtitulo("Finalizar app")
    
    
def voltar_ao_menu_principal():
    '''Função para voltar ao menu do sistema'''
    input("Digite uma tecla para voltar ao menu principal: ")
    main()
    
def opcao_invalida():
    '''Função para caso coloque alguma outra forma de escrita'''
    print("Opção invalida!\n")
    voltar_ao_menu_principal()
    

def exibir_subtitulo(texto):
    '''Função para apagar o terminal e estilizar'''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()
    
def cadastrar_novo_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante
    
    inputs:
    - Nome do restaurante
    - Categoria do restaurante
    
    outputs:
    - Adciona um novo restaurante a lista de restaurantes
    '''
    exibir_subtitulo("Cadastro de novos restaurantes")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f"Digite o nome da categoria do restaurante {nome_do_restaurante}: ")
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False }
    restaurantes.append(dados_do_restaurante)
    print(f"\nO restaurante {nome_do_restaurante} foi cadastrado com sucesso! \n")
    voltar_ao_menu_principal()
    
    
def listar_restaurantes():
    ''' Lista os restaurantes com o espaçamento devido'''
    
    exibir_subtitulo("Listando os restaurantes")
    
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}' )
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante["ativo"] else 'Desativado'
        print(f"- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}")
    
    voltar_ao_menu_principal()
    
def alternar_estado_restaurante():
    '''Função para alternar o estado do restuarante com laço de repetição.
    
    input: 
    - Digitar o nome do restaurante que deseja alterar o estado.
    
    outputs:
    - Mostra o restaurante que houve a troca de estado.
    
    '''
    exibir_subtitulo("Alternar estado do restaurante")
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
            
            
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')
    voltar_ao_menu_principal()

def escolher_opcao():
    '''Função para escolher as opções
    
    input:
    - Escolher alguma opção
    
    output:
    - Ir na opção escolhida
    '''
    try:
        opcao_escolhida = int(input('Escolha alguma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
        


def main():
    '''Função do menu principal'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
    
if __name__ == '__main__':
    main()
