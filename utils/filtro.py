def buscar_jogadores_interativos(jogadores):
    # Filtros Básicos
    nome = input("Nome: ").strip().lower()
    clube = input("Clube: ").strip().lower()
    pais = input("Nacionalidade: ").strip().lower()
    posicao = input("Posição: ").strip().lower()

    # Filtros numéricos
    try:
        gols_min = input("Gols mínimos (0 para avançar): ").strip()
        gols_min = int(gols_min) if gols_min else 0
    except ValueError:
        gols_min = 0
        print("⚠️ Valor inválido para gols mínimos, usando 0")

    try:
        idade_max = input("Idade máxima (0 para nenhum filtro): ").strip()
        idade_max = int(idade_max) if idade_max else 0
    except ValueError:
        idade_max = 0
        print("⚠️ Valor inválido para idade máxima, usando 0")

    # Aplicação dos filtros
    filtrados = jogadores

    if nome:
        filtrados = [j for j in filtrados if nome in j.nome.lower()]

    if clube:
        filtrados = [j for j in filtrados if clube in j.clube.lower()]

    if pais:
        filtrados = [j for j in filtrados if pais in j.pais.lower() or (len(pais) == 3 and j.pais.lower().startswith(pais))]

    if posicao:
        pos_map = {
            'defensor': 'df', 'zagueiro': 'df', 'lateral': 'df',
            'meia': 'mf', 'volante': 'mf', 'armador': 'mf',
            'atacante': 'fw', 'ponta': 'fw', 'centroavante': 'fw',
            'goleiro': 'gk'
        }
        pos_busca = pos_map.get(posicao, posicao)
        filtrados = [j for j in filtrados if pos_busca in [p.lower() for p in j.posicao]]

    # Filtros numéricos
    filtrados = [j for j in filtrados if j.estatisticas.get("gols", 0) >= gols_min]

    if idade_max > 0:
        filtrados = [j for j in filtrados if j.idade <= idade_max]

    # Ordenação dos resultados
    filtrados.sort(key=lambda x: (
        -x.estatisticas.get("gols", 0),
        -x.estatisticas.get("minutos", 0)
    ))

    if not filtrados:
        print("\n⚠️ Nenhum jogador encontrado com esses critérios.")
    else:
        print(f"\n✅ {len(filtrados)} jogador(es) encontrado(s):\n")
        for j in filtrados:
            j.mostrar_info()
            print("🔹" * 40 + "\n")
