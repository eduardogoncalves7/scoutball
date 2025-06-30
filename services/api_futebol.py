from models.jogador import Jogador

def buscar_jogadores_teste_api():
    return[
                Jogador(
            nome="Gabriel Barbosa",
            idade=27,
            altura=181,
            pais="Brasil",
            liga="Brasileirão Série A",
            clube="Cruzeiro",
            posicao=["Centroavante", "Falso 9"],
            pe_bom="Esquerdo",
            estatisticas={"gols": 9, "assistencias": 4, "minutos": 1650},
            valor_estimado=10000000
        ),
        Jogador(
            nome="Luka Modric",
            idade=38,
            altura=172,
            pais="Croácia",
            liga="La Liga",
            clube="Real Madrid",
            posicao=["Meio-campista", "Armador"],
            pe_bom="Direito",
            estatisticas={"gols": 3, "assistencias": 6, "minutos": 2100},
            valor_estimado=3000000
        ),
        Jogador(
            nome="Idrissa Diallo",
            idade=19,
            altura=175,
            pais="Senegal",
            liga="Ligue 1",
            clube="Olympique de Marseille",
            posicao=["Ponta Direita", "Atacante"],
            pe_bom="Esquerdo",
            estatisticas={"gols": 7, "assistencias": 2, "minutos": 1200},
            valor_estimado=5500000
        )
    ]



