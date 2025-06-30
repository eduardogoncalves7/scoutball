
ScoutBall ⚽📊

ScoutBall é um projeto simples de análise de jogadores de futebol que tem como objetivo localizar atletas promissores ou veteranos que ainda podem agregar valor a um time. A proposta foi inspirada no filme Moneyball, focando na identificação de talentos por meio de estatísticas e eficiência, mesmo fora dos holofotes tradicionais.

🚀 Funcionalidades

- Exibe estatísticas detalhadas dos jogadores:
  - Nome, posição, idade, altura, clube, liga
  - Pé dominante
  - Gols, assistências
  - Média por 90 minutos
  - Custo por participação em gol
- Organiza as informações de forma clara no terminal

📷 Exemplo de saída no terminal

Neymar Jr | Posição: ATA | Pé: Direito | 31 anos | 175 cm
Al-Hilal | Liga Saudita
Valor estimado: €75M
Gols: 12 | Assistências: 9 | Média: 1.80/90min
Custo por participação em gol: €3,9M

📁 Estrutura do projeto

scoutball/
├── jogadores.csv           # Dados dos jogadores
├── filtro.py               # Código principal de análise
├── utils.py                # Funções auxiliares (se houver)
├── README.md               # Este arquivo

🧠 Aprendizados

Este projeto foi desenvolvido como prática dos seguintes conceitos:

- Manipulação de arquivos e dados com Python
- Cálculos estatísticos simples
- Estruturação de código em módulos
- Simulação de scouting (observação técnica)
- Boas práticas com Git e GitHub

🛠 Tecnologias utilizadas

- Python 3.10+
- Editor: VS Code
- Terminal / Prompt de Comando

💡 Próximos passos

- [ ] Implementar filtros personalizados (por posição, idade, etc.)
- [ ] Exportar relatórios em CSV ou PDF
- [ ] Interface gráfica com Tkinter ou versão Web com Flask
- [ ] Integração com API para buscar dados de jogadores reais

📚 Créditos e inspiração

Projeto desenvolvido como parte do aprendizado pessoal, inspirado por:

- O filme Moneyball (2011)
- Estatísticas de futebol e fantasy games
- Modos de jogo como FIFA Career Mode e Ultimate Team

📌 Como executar

1. Clone o repositório:
git clone https://github.com/SEU_USUARIO/scoutball.git

2. Entre na pasta do projeto:
cd scoutball

3. Execute o script principal:
python filtro.py

📄 Licença

Este projeto é de uso educacional e não possui licença comercial. Sinta-se livre para estudar, adaptar ou evoluir.
