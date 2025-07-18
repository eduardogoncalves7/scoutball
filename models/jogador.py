class Jogador:
    def __init__(self, nome, idade, pais, liga, clube, posicao, estatisticas):
        self.nome = nome
        self.idade = idade
        self.pais = pais
        self.liga = liga
        self.clube = clube
        self.posicao = posicao
        self.estatisticas = estatisticas
        self.metricas = self.calcular_metricas()

    def calcular_metricas(self):
        minutos = self.estatisticas.get("minutos", 0)
        gols = self.estatisticas.get("gols", 0)
        gols_por_90min = (gols / minutos) * 90 if minutos > 0 else 0

        return {
            "gols_por_90min": gols_por_90min
        }

    def mostrar_info(self):
        # Traduções legíveis
        posicao_legivel = {
            'fw': 'Atacante',
            'mf': 'Meio-Campista',
            'df': 'Defensor',
            'gk': 'Goleiro'
        }

        pais_legivel = {
            'br': 'Brasil', 'bra': 'Brasil',
            'uru': 'Uruguai', 'arg': 'Argentina',
            'eng': 'Inglaterra', 'fra': 'França',
            'por': 'Portugal', 'col': 'Colômbia',
            'ven': 'Venezuela', 'chi': 'Chile',
            'per': 'Peru'
        }

        # Posição
        posicoes_formatadas = []
        for pos in self.posicao:
            pos_lower = pos.strip().lower()
            posicoes_formatadas.append(posicao_legivel.get(pos_lower, pos.capitalize()))
        posicoes_str = ", ".join(posicoes_formatadas)

        # Nacionalidade
        pais_codigo = self.pais.strip().lower()
        pais_str = pais_legivel.get(pais_codigo, self.pais.upper())

        # Estatísticas básicas
        gols = self.estatisticas.get("gols", 0)
        minutos = self.estatisticas.get("minutos", 0)
        partidas = round(minutos / 90, 1) if minutos > 0 else 0

        print("📌 Informações do Jogador:")
        print(f"🧑 Nome: {self.nome}")
        print(f"🎂 Idade: {self.idade} anos")
        print(f"🌍 País: {pais_str}")
        print(f"🏟️ Clube: {self.clube} | Liga: {self.liga}")
        print(f"🎯 Posição: {posicoes_str}")
        print(f"\n📊 Estatísticas em campo:")
        print(f"⏱️ Minutos: {minutos:.0f} | Partidas estimadas: {partidas}")
        print(f"⚽ Gols: {gols}")
        print(f"📈 Gols por 90 minutos: {self.metricas['gols_por_90min']:.2f}")
        print("🔹" * 40 + "\n")
