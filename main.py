from services.api_futebol import buscar_jogadores_teste_api
from utils.estatisticas import ranquear_jogadores
from utils.filtro import filtrar_jogadores
#from models.jogador import Jogador

if __name__ == '__main__': 
    jogadores = buscar_jogadores_teste_api()   
    ranking = ranquear_jogadores(jogadores)

nome = input("Buscar por nome (Enter para ignorar)")
liga = input("Liga: ")
pais = input("Nacionalidade: ")
idade_str = input("Idade exata: ")
posicao = input("Posição: ")
valor_str = input("Valor máximo (em euros): ")

idade = int(idade_str) if idade_str.strip().isdigit() else None
valor_max = int(valor_str) if valor_str.strip().isdigit() else None

# for i, jogador in enumerate(ranking[:5], 1):
#      print(f"{i}. Nome: {jogador.nome} – Clube: {jogador.clube} - Liga: {jogador.liga} \n {jogador.metricas['gols_por_90min']:.2f} gols/90min – Valor: €{jogador.valor_estimado:,}")

resultados = filtrar_jogadores(jogadores,nome,liga,pais,idade,posicao,valor_max)

if not resultados:
    print("Nenhum jogador encontrado.")
else:
    print(f"{len(resultados)} Jogadores encontrados:")
    for j in resultados:
        print("🔹" * 30)
        print(f"👤 Nome: {j.nome}")
        print(f"🎯 Posição: {', '.join(j.posicao)}")
        print(f"🦶 Pé dominante: {j.pe_bom}")
        print(f"🎂 Idade: {j.idade} anos")
        print(f"📏 Altura: {j.altura} cm")
        print(f"🏟️ Clube: {j.clube}")
        print(f"🏆 Liga: {j.liga}")
        print(f"💰 Valor estimado: €{j.valor_estimado:,}")
        print("🔹" * 30 + "\n")
