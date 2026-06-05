import os
from fastapi import FastAPI, HTTPException
import httpx
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Riot Telemetry API (Enterprise)", version="2.1.0")

RIOT_API_KEY = os.getenv("RIOT_API_KEY")
HEADERS = {"X-Riot-Token": RIOT_API_KEY}

@app.get("/")
async def root():
    return {"status": "Servidor de Inteligencia Ativo", "alvo": "Riot Games"}

@app.get("/api/v1/jogador/{game_name}/{tag_line}")
async def buscar_telemetria_basica(game_name: str, tag_line: str):
    account_url = f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(account_url, headers=HEADERS)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Falha ao localizar o Riot ID.")
        
        account_data = response.json()
        puuid = account_data.get("puuid")

        summoner_url = f"https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{puuid}"
        summoner_response = await client.get(summoner_url, headers=HEADERS)
        
        summoner_data = summoner_response.json() if summoner_response.status_code == 200 else {}

        return {
            "riot_id": f"{account_data.get('gameName')}#{account_data.get('tagLine')}",
            "puuid": puuid,
            "summoner_id": summoner_data.get("id"),
            "nivel": summoner_data.get("summonerLevel", 0)
        }

@app.get("/api/v1/competitivo/{game_name}/{tag_line}")
async def buscar_status_competitivo(game_name: str, tag_line: str):
    account_url = f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"
    
    async with httpx.AsyncClient() as client:
        acc_resp = await client.get(account_url, headers=HEADERS)
        if acc_resp.status_code != 200:
            raise HTTPException(status_code=404, detail="Jogador nao encontrado.")
        puuid = acc_resp.json().get("puuid")

        summ_resp = await client.get(f"https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{puuid}", headers=HEADERS)
        
        if summ_resp.status_code != 200:
            return {"mensagem": "Perfil de League of Legends nao encontrado para esta conta. (Conta exclusiva de Valorant?)"}
            
        summoner_id = summ_resp.json().get("id")
        
        # O ESCUDO DEFENSIVO: Se a Riot devolver null para o ID, abortamos a busca graciosamente
        if not summoner_id:
            return {"mensagem": "O jogador existe, mas nao possui um ID de Invocador ativo (Nivel baixo ou sem historico no LoL)."}

        ranked_url = f"https://br1.api.riotgames.com/lol/league/v4/entries/by-summoner/{summoner_id}"
        ranked_resp = await client.get(ranked_url, headers=HEADERS)
        
        if ranked_resp.status_code != 200:
            return {"mensagem": "Falha de comunicacao com os servidores de ranqueada da Riot."}
            
        ranked_data = ranked_resp.json()
        
        if not isinstance(ranked_data, list) or len(ranked_data) == 0:
            return {"mensagem": "O jogador nao possui partidas ranqueadas nesta temporada."}
            
        estatisticas = []
        for fila in ranked_data:
            vitorias = fila.get("wins", 0)
            derrotas = fila.get("losses", 0)
            total_jogos = vitorias + derrotas
            winrate = round((vitorias / total_jogos) * 100, 2) if total_jogos > 0 else 0
            
            estatisticas.append({
                "tipo_fila": fila.get("queueType"),
                "tier": fila.get("tier"),
                "rank": fila.get("rank"),
                "pontos_de_liga": fila.get("leaguePoints"),
                "vitorias": vitorias,
                "derrotas": derrotas,
                "winrate_percentual": winrate
            })
            
        return {"riot_id": f"{game_name}#{tag_line}", "historico_competitivo": estatisticas}