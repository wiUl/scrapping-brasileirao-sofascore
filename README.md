# Scraping Brasileirão SofaScore

Coleta de estatísticas detalhadas dos jogadores do Brasileirão Série A utilizando a API do SofaScore através da biblioteca `sofascore_api`.

## Funcionalidades

* Coleta de times do campeonato
* Coleta de jogadores dos times
* Coleta de estatísticas individuais dos jogadores
* Exportação dos dados para CSV
* Dataset completo do campeonato

---

## Tecnologias

* Python 3
* Pandas
* sofascore_api
* curl_cffi

---

## Instalação

Clone o repositório:

```bash
git clone https://github.com/wiUl/scrapping-brasileirao-sofascore.git
```

Entre na pasta do projeto:

```bash
cd scrapping-brasileirao-sofascore
```

Crie um ambiente virtual:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## Como executar

Execute o script principal:

```bash
python main.py
```

Os dados serão exportados para:

```text
data/brasileirao_2026_player_stats.csv
```

---

## Estrutura do Projeto

```text
scrapping-brasileirao-sofascore/
│
├── data/
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Dados coletados

Exemplos de estatísticas disponíveis:

* gols
* assistências
* expected goals (xG)
* dribles
* passes
* desarmes
* interceptações
* minutos jogados
* duelos ganhos
* rating SofaScore
* e mais..

---

## Observações

O endpoint público de ranking do SofaScore possui limitação de jogadores retornados.

Por isso, o projeto utiliza coleta individual das estatísticas de cada jogador para obter o dataset completo do campeonato.

---

## Autor

GitHub: https://github.com/wiUl
