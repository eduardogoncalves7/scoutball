def filtrar_jogadores(jogadores, nome =None, liga=None,clube = None,pais = None, idade=None,altura=None,pe_bom=None, posicao=None,valor_max=None):
    filtrados = jogadores
    if nome:
        filtrados = [j for j in filtrados if nome.lower() in j.nome.lower()]
    if liga:
        filtrados = [j for j in filtrados if liga.lower() in j.liga.lower()]
    if clube:
        filtrados = [j for j in filtrados if clube.lower() in j.clube.lower()]
    if pais:
        filtrados = [j for j in filtrados if pais.lower() in j.pais_nascimento.lower()]
    if idade:
        filtrados = [j for j in filtrados if j.idade == idade]
    if altura:
        filtrados = [j for j in filtrados if j.altura == altura]
    if pe_bom:
        if pe_bom.upper() == 'E':
            filtrados = [j for j in filtrados if j.pe_bom.lower() == "esquerdo"]
        elif pe_bom.upper() == 'D':
            filtrados = [j for j in filtrados if j.pe_bom.lower() == "direito"]
    if posicao:
        filtrados = [j for j in filtrados if posicao.lower() in [p.lower() for p in j.posicao]]
    if valor_max:
        filtrados = [j for j in filtrados if j.valor_estimado <= valor_max]

    return filtrados