import streamlit as st
import requests

st.set_page_config(page_title="Riot Analytics Elite", layout="centered")

st.image("https://logodownload.org/wp-content/uploads/2019/12/riot-games-logo-1.png", width=150)
st.title("⚡ Telemetria Tática: Riot Games")
st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    game_name = st.text_input("Riot ID (Nome)", "Black12")
with col2:
    tag_line = st.text_input("Tagline", "BR1")

if st.button("Executar Varredura", use_container_width=True):
    with st.spinner("Interceptando servidores da Riot..."):
        # O Frontend (Streamlit) batendo no Backend (FastAPI local)
        api_url = f"http://127.0.0.1:8000/api/v1/competitivo/{game_name}/{tag_line}"
        
        try:
            resposta = requests.get(api_url)
            dados = resposta.json()
            
            if resposta.status_code == 200:
                if "mensagem" in dados:
                    st.warning(dados["mensagem"])
                else:
                    st.success(f"Alvo Localizado: {dados['riot_id']}")
                    st.markdown("### Histórico Competitivo")
                    
                    for fila in dados.get("historico_competitivo", []):
                        st.markdown(f"**Fila:** {fila['tipo_fila']}")
                        c1, c2, c3, c4 = st.columns(4)
                        c1.metric("Tier", f"{fila['tier']} {fila['rank']}")
                        c2.metric("PDL", fila['pontos_de_liga'])
                        c3.metric("Vitórias", fila['vitorias'])
                        c4.metric("Winrate", f"{fila['winrate_percentual']}%")
                        st.markdown("---")
            else:
                st.error("Falha ao comunicar com o servidor de inteligência.")
        except requests.exceptions.ConnectionError:
            st.error("O Motor da API está desligado! Ligue o Uvicorn no terminal primeiro.")