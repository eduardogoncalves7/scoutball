def ranquear_jogadores(jogadores):
    return sorted(jogadores, key=lambda j: j.metricas["gols_por_90min"], reverse=True)
