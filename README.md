# Scraping Brasileirão — estatísticas de jogadores (SofaScore)

Script em Python que coleta as **estatísticas individuais de todos os jogadores do Campeonato Brasileiro Série A 2026** a partir da API do SofaScore (biblioteca `sofascore_api`) e as consolida em um único arquivo CSV.

## Resultado

O dataset coletado está versionado em [`data/brasileirao_2026_player_stats.csv`](data/brasileirao_2026_player_stats.csv):

| | |
| --- | --- |
| **Jogadores** | 566 linhas (um jogador por linha) |
| **Times** | 20 |
| **Colunas** | 118 |
| **Versionado em** | 02/06/2026 (data do commit; a rodada em que a coleta foi feita não está registrada no repositório) |

### Colunas

Cada coluna mantém o nome retornado pela API, sem renomeação nem tratamento posterior.

- **Identificação:** `player_id`, `player_name`, `player_slug`, `team_id`, `team_name`, `team_slug`.
- **Avaliação e volume de jogo:** `rating`, `totalRating`, `countRating`, `appearances`, `matchesStarted`, `minutesPlayed`, `totwAppearances`.
- **Ataque:** `goals`, `assists`, `expectedGoals`, `expectedAssists`, `totalShots`, `shotsOnTarget`, `bigChancesCreated`, `bigChancesMissed`, `successfulDribbles`, entre outras.
- **Passes e criação:** `accuratePasses`, `totalPasses`, `accuratePassesPercentage`, `keyPasses`, `accurateLongBalls`, `accurateCrosses`, entre outras.
- **Defesa e duelos:** `tackles`, `interceptions`, `clearances`, `groundDuelsWon`, `aerialDuelsWon`, `ballRecovery`, entre outras.
- **Disciplina:** `yellowCards`, `redCards`, `directRedCards`, `fouls`, `wasFouled`.
- **Goleiros:** `saves`, `cleanSheet`, `goalsConceded`, `goalsPrevented`, `penaltySave`, entre outras.

Colunas não aplicáveis ao jogador (por exemplo, as de goleiro para um atacante) ficam vazias ou zeradas conforme a resposta da API. A lista completa está no cabeçalho do CSV.

## Como funciona

O script [`scripts/scrapper.py`](scripts/scrapper.py):

1. Busca a classificação do torneio (`TOURNAMENT_ID = 325`, `SEASON_ID = 87678`, definidos no início do arquivo) para obter os times.
2. Lista os jogadores de cada time.
3. Consulta as estatísticas de cada jogador individualmente, com pausa de 0,5 s entre as chamadas.
4. Consolida tudo em um DataFrame do pandas e grava o CSV em `data/`.

**Por que jogador a jogador:** o endpoint público de ranking do SofaScore limita a quantidade de jogadores retornados; a coleta individual evita esse corte e permite obter o campeonato completo.

## Tecnologias

Python 3 · pandas · `sofascore_api` · curl_cffi

## Como executar

```bash
git clone https://github.com/wiUl/scrapping-brasileirao-sofascore.git
cd scrapping-brasileirao-sofascore

python -m venv venv
# Windows: venv\Scripts\activate
# Linux/Mac: source venv/bin/activate

pip install -r requirements.txt

cd scripts
python scrapper.py
```

O script usa um caminho relativo para gravar o resultado, por isso deve ser executado **de dentro da pasta `scripts/`**. O arquivo é gerado em `data/brasileirao_2026_player_stats.csv`. Como cada jogador é consultado separadamente, a execução leva vários minutos.

## Estrutura do repositório

```text
scrapping-brasileirao-sofascore/
├── data/
│   └── brasileirao_2026_player_stats.csv
├── scripts/
│   └── scrapper.py
├── requirements.txt
└── README.md
```

## Observações e limitações

- Os dados vêm de uma API não oficial do SofaScore, sujeita a mudanças. Os termos de uso do SofaScore devem ser consultados antes de redistribuir ou usar os dados comercialmente.
- O dataset é um retrato de um momento da temporada; para atualizá-lo, o script precisa ser executado novamente.
- Os valores não passam por validação ou limpeza neste repositório.

## Autor

Willian Gomes — https://github.com/wiUl
