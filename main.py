from utils.unificador import carregar_jogadores_unificados
from utils.filtro import buscar_jogadores_interativos

if __name__ == '__main__':
    jogadores = carregar_jogadores_unificados()
    buscar_jogadores_interativos(jogadores)
