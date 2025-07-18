import pandas as pd
from models.jogador import Jogador
from datetime import datetime

def buscar_jogadores_construcao():
    caminho = r"C:\Users\uxe1675.FSFX\Desktop\scoutball\data\fbref\planilha_construcao.csv"
    jogadores = []
    ano_atual = datetime.now().year

    colunas = [
        "Rk", "Player", "Nation", "Pos", "Squad", "Age", "Born", "90s",
        "SCA", "SCA90", "PassLive", "PassDead", "TO", "Sh", "Fld", "Def",
        "GCA", "GCA90", "PassLive.1", "PassDead.1", "TO.1", "Sh.1", "Fld.1", "Def.1"
    ]

    

    try:
        df = pd.read_csv(caminho, names=colunas, header=None, encoding='latin1')
        

        
        def extrair_idade(born):
            try:
                ano = int(float(born))  # cobre casos como 1997.0 ou '1997.0'
                return datetime.now().year - ano
            except Exception:
                return 0


        for _, row in df.iterrows():
            try:
                if not row.get("Player") or pd.isna(row["Player"]):
                    continue

                nome = str(row["Player"]).strip()
                pais = str(row["Nation"]).strip().split()[-1].lower()
                clube = str(row["Squad"]).strip()
                posicao = [str(row["Pos"]).strip().lower()]
                born = row.get("Born", "")
                idade = extrair_idade(born)
                minutos_jogados = pd.to_numeric(row["90s"], errors='coerce') * 90 if row["90s"] else 0

                estatisticas = {
                    "minutos": float(minutos_jogados) if not pd.isna(minutos_jogados) else 0,
                    "sca": pd.to_numeric(row["SCA"], errors='coerce'),
                    "sca90": pd.to_numeric(row["SCA90"], errors='coerce'),
                    "gca": pd.to_numeric(row["GCA"], errors='coerce'),
                    "gca90": pd.to_numeric(row["GCA90"], errors='coerce'),
                    "passlive": pd.to_numeric(row["PassLive"], errors='coerce'),
                    "passdead": pd.to_numeric(row["PassDead"], errors='coerce'),
                    "to": pd.to_numeric(row["TO"], errors='coerce'),
                    "sh": pd.to_numeric(row["Sh"], errors='coerce'),
                    "fld": pd.to_numeric(row["Fld"], errors='coerce'),
                    "def": pd.to_numeric(row["Def"], errors='coerce'),
                }

                jogador = Jogador(
                    nome=nome,
                    idade=idade,
                    pais=pais,
                    liga="Série A",
                    clube=clube,
                    posicao=posicao,
                    estatisticas=estatisticas
                )

                jogadores.append(jogador)
                

            except Exception as e:
                print(f"⚠️ Erro ao processar jogador (construção): {row.get('Player', 'Desconhecido')} -> {e}")

    except Exception as e:
        print(f"❌ Erro ao ler CSV de construção: {e}")


    return jogadores




def buscar_jogadores_finalizacao():
    caminho = r"C:\Users\uxe1675.FSFX\Desktop\scoutball\data\fbref\planilha_finalizacao.csv"
    jogadores = []
    ano_atual = datetime.now().year

    colunas = [
        "Rk", "Player", "Nation", "Pos", "Squad", "Age", "Born", "90s", "Gls",
        "Sh", "SoT", "SoT%", "Sh/90", "SoT/90", "G/Sh", "G/SoT", "Dist", "FK", "PK", "PKatt"
    ]

    try:

        df = pd.read_csv(caminho, names=colunas, header=None, encoding='latin1')
        
        

        def extrair_idade(born):
            try:
                ano = int(float(born))  # cobre casos como 1997.0 ou '1997.0'
                return datetime.now().year - ano
            except Exception:
                return 0



        for _, row in df.iterrows():
            try:
                if not row.get("Player") or pd.isna(row["Player"]):
                    continue

                nome = str(row["Player"]).strip()
                pais = str(row["Nation"]).strip().split()[-1].lower()
                clube = str(row["Squad"]).strip()
                posicao = [str(row["Pos"]).strip().lower()]
                born = row.get("Born", "")
                idade = extrair_idade(born)
                minutos_jogados = pd.to_numeric(row["90s"], errors='coerce') * 90 if row["90s"] else 0
                gols = pd.to_numeric(row["Gls"], errors='coerce')

                estatisticas = {
                    "minutos": float(minutos_jogados) if not pd.isna(minutos_jogados) else 0,
                    "gols": int(gols) if not pd.isna(gols) else 0,
                    "sh": pd.to_numeric(row["Sh"], errors='coerce'),
                    "sot": pd.to_numeric(row["SoT"], errors='coerce'),
                    "dist": pd.to_numeric(row["Dist"], errors='coerce'),
                    "pk": pd.to_numeric(row["PK"], errors='coerce')
                }

                jogador = Jogador(
                    nome=nome,
                    idade=idade,
                    pais=pais,
                    liga="Série A",
                    clube=clube,
                    posicao=posicao,
                    estatisticas=estatisticas
                )
                jogadores.append(jogador)
                

            except Exception as e:
                print(f"⚠️ Erro ao processar jogador (finalização): {row.get('Player', 'Desconhecido')} -> {e}")

    except Exception as e:
        print(f"❌ Erro ao ler CSV de finalização: {e}")

    return jogadores
