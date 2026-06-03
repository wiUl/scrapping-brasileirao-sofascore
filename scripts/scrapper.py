from sofascore_api import SofaScoreClient
import pandas as pd
import time

# =========================================================
# CONFIG
# =========================================================

TOURNAMENT_ID = 325
SEASON_ID = 87678

client = SofaScoreClient()

# =========================================================
# 1. PEGAR CLASSIFICAÇÃO (TIMES)
# =========================================================

print("Coletando times do Brasileirão...")

standings = client.get_tournament_standings(
    tournament_id=TOURNAMENT_ID,
    season_id=SEASON_ID
)

# estrutura do SofaScore
rows = standings["standings"][0]["rows"]

teams = []

for row in rows:

    team = row["team"]

    teams.append({
        "team_id": team["id"],
        "team_name": team["name"],
        "team_slug": team["slug"]
    })

print(f"Times encontrados: {len(teams)}")

# =========================================================
# 2. PEGAR TODOS OS JOGADORES
# =========================================================

print("\nColetando jogadores dos times...")

all_players = []

for team in teams:

    print(f"\nTime: {team['team_name']}")

    try:

        players = client.get_team_players(
            team["team_id"]
        )

        for p in players:

            player = p["player"]

            all_players.append({

                "player_id": player["id"],
                "player_name": player["name"],
                "player_slug": player["slug"],

                "team_id": team["team_id"],
                "team_name": team["team_name"],
                "team_slug": team["team_slug"]
            })

        print(f"Jogadores coletados: {len(players)}")

    except Exception as e:

        print(f"Erro no time {team['team_name']}: {e}")

# =========================================================
# 3. REMOVER DUPLICATAS
# =========================================================

players_df = pd.DataFrame(all_players)

players_df = players_df.drop_duplicates(
    subset=["player_id"]
).reset_index(drop=True)

print("\n==============================")
print("TOTAL DE JOGADORES")
print("==============================")

print(players_df.shape[0])

# =========================================================
# 4. PEGAR ESTATÍSTICAS INDIVIDUAIS
# =========================================================

print("\nColetando estatísticas individuais...")

dataset = []

total = len(players_df)

for idx, player in players_df.iterrows():

    print(
        f"[{idx+1}/{total}] "
        f"{player['player_name']}"
    )

    try:

        stats_response = client.get_player_statistics(
            player_id=player["player_id"],
            tournament_id=TOURNAMENT_ID,
            season_id=SEASON_ID
        )

        # payload principal
        stats = stats_response.get(
            "statistics",
            stats_response
        )

        # linha base
        row = {

            "player_id": player["player_id"],
            "player_name": player["player_name"],
            "player_slug": player["player_slug"],

            "team_id": player["team_id"],
            "team_name": player["team_name"],
            "team_slug": player["team_slug"]
        }

        # adiciona TODAS as estatísticas
        for key, value in stats.items():

            # evita objetos complexos
            if isinstance(value, (dict, list)):
                continue

            row[key] = value

        dataset.append(row)

        print("OK")

    except Exception as e:

        print(f"ERRO: {e}")

    # evita rate limit
    time.sleep(0.5)

# =========================================================
# 5. DATAFRAME FINAL
# =========================================================

df = pd.DataFrame(dataset)

# =========================================================
# 6. INFO FINAL
# =========================================================

print("\n==============================")
print("DATASET FINAL")
print("==============================")

print("\nShape:")
print(df.shape)

print("\nColunas:")
print(df.columns.tolist())

print("\nPreview:")
print(df.head())

print("\nValores não nulos:")
print(df.count().sort_values(ascending=False))

# =========================================================
# 7. EXPORTAÇÃO
# =========================================================

csv_name = "../data/brasileirao_2026_player_stats.csv"

df.to_csv(
    csv_name,
    index=False
)

print("\n==============================")
print("CSV SALVO")
print("==============================")

print(csv_name)