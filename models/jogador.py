class Jogador:
    def __init__(self, nome, idade, altura, pais, liga, clube, posicao, pe_bom, estatisticas, valor_estimado):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.pais = pais
        self.liga = liga
        self.clube = clube 
        self.posicao = posicao
        self.pe_bom = pe_bom
        self.estatisticas = estatisticas
        self.valor_estimado = valor_estimado
        self.metricas = self.calcular_metricas()

    def calcular_metricas(self):
        minutos = self.estatisticas.get("minutos", 1)
        gols = self.estatisticas.get("gols", 0)
        assists = self.estatisticas.get("assistencias", 0)
        return {
            "gols_por_90min": (gols / minutos) * 90,
            "participacoes_em_gols": gols + assists
        }

    def mostrar_info(self):       
        gols = self.estatisticas.get("gols", 0)
        assistencias = self.estatisticas.get("assistencias", 0)
        minutos = self.estatisticas.get("minutos", 0)
        partidas = round(minutos / 90, 1)

        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade} anos')
        print(f'Altura: {self.altura} cm')
        print(f'Posição: {self.posicao}')
        print(f'Pé dominante: {self.pe_bom}')
        print(f'País: {self.pais}')
        print(f'Liga: {self.liga}')
        print("\n📊 Estatísticas:")
        print(f'Partidas disputadas: {partidas}')
        print(f'Gols: {gols}')
        print(f'Assistências: {assistencias}')
        print(f'Minutos jogados: {minutos}')
        print(f'Média Gols por 90 min: {self.metricas["gols_por_90min"]:.2f}')
        print(f'Participações em gols: {self.metricas["participacoes_em_gols"]:.2f}')
        print("\n💰 Valores:")
        print(f'Valor estimado: €{self.valor_estimado:,}')
        print(f'Custo por participação de gol: €{self.custo_beneficio():,.2f}')

    def custo_beneficio(self):
        participacoes = self.metricas.get("participacoes_em_gols", 1)
        return self.valor_estimado / participacoes if participacoes > 0 else float('inf')
