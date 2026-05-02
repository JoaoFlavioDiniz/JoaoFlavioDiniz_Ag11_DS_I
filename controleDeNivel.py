from colorama import Fore, Style, init

# Inicializa a biblioteca colorama
init() 


# Lista com os níveis e suas mensagens
niveis_reservatorio = [
    "Nível 1 - Muito baixo (CRÍTICO)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (ALERTA)"
]

# Função para definir a cor conforme o nível de agua muda de cor
def definir_cor_mensagem(nivel):
    
    if nivel == 1:
        return Fore.RED
    elif nivel== 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE
    
# Simulação de leitura do nível do reservatório, pede ao usuário que informe o nível
nivel_atual = int(input("Informe o nível do reservatório (1 a 5): "))

# Verificação do nível do reservatório entre 1 e 5
if 1 <= nivel_atual <= 5:

    cor = definir_cor_mensagem(nivel_atual)
    mensagem = niveis_reservatorio[nivel_atual - 1]

    print(cor + "Situação do Reservatório:")
    print(cor + mensagem)

else:
    print(Fore.WHITE + "Nível inválido. Informe um valor entre 1 e 5.")

# Restaura o estilo padrão do terminal para limpar o estilo do colorama
print(Style.RESET_ALL)
