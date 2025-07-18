from models.leitor_csv import buscar_jogadores_construcao, buscar_jogadores_finalizacao
from models.jogador import Jogador

def carregar_jogadores_unificados():
    """
    Lê as duas planilhas (construção e finalização),
    combina as estatísticas para cada jogador
    e retorna uma lista unificada de objetos Jogador.
    """
    construcao = buscar_jogadores_construcao()
    finalizacao = buscar_jogadores_finalizacao()

    jogadores_dict = {}

    # Primeiro adiciona jogadores da construção
    for j in construcao:
        jogadores_dict[j.nome.strip().lower()] = j

    # Depois atualiza com estatísticas da finalização
    for j in finalizacao:
        chave = j.nome.strip().lower()

        if chave in jogadores_dict:
            jogador_existente = jogadores_dict[chave]
            # Atualiza o dicionário de estatísticas
            jogador_existente.estatisticas.update(j.estatisticas)
        else:
            # Caso o jogador não esteja na construção, adiciona direto
            jogadores_dict[chave] = j

    return list(jogadores_dict.values())
