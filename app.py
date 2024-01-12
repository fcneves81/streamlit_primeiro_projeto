import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="Fernando Camargo", page_icon=":tada:", layout="wide")

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Meu CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</styel>", unsafe_allow_html=True)

local_css("style/style.css")

# Assets

lottie_animation = load_lottie("https://lottie.host/52a3d559-0f5c-446a-a75d-662a7cfa85ca/kfVf1sJ66u.json")
banner = Image.open("images/capa-github.png")

# HEADER

with st.container():
    st.subheader("Que bom ter você aqui 😉")
    st.image(banner)
    st.title("Engenheiro de Sotfware em formação")
    st.write("A cada dia, aprendendo mais sobre o maravilhoso mundo do Python e Java para enfrentar os desafios do dia a dia!")
    st.write("[Conheça meus projetos e aprendizado até aqui >](https://github.com/fcneves81)") 
 
# SOBRE MIM

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Minhas Competências")
        st.write("##")
        st.write(
            """
            HARD SKILLS:
            - Java
            - Python
                - Pandas
                - Seaborn
                - Django
                - Streamlit (que inclusive, está sendo usado neste projeto 🤩)
            - HTML, CSS e JavaScript
            - BootStrap
            - Banco de Dados Relacionais: MySQL, PostgreSQL e SQL Server
            - Banco de Dados não Relacionais: MongoDB
            - Git
            - Power BI
            
            SOFT SKILLS:
            - Ética
            - Empatia
            - Flexibilidade
            - Inteligência Emocional
            - Sou colaborativo
            - Organizado
            - Resiliente
            - Sei trabalhar sob pressão
            - Bom relacionamento interpessoal
            - Criatividade            
            
            """
        )
    with right_column:
        st_lottie(lottie_animation, height=800, key="coding")

# --- Contato
with st.container():
    st.write("---")
    st.header("Entre em contato comigo!")
    st.write("##")
    
    # Formulário utilizado: https://formsubmit.co/
    
    form_contato = """
    <form action="https://formsubmit.co/fcneves81@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Seu nome" required>
        <input type="email" name="email" placeholder="Seu email" required>
        <textarea name="message" placeholder="Sua mensagem" required></textarea>
        <button type="submit">Enviar</button>
    </form>
    """
    left_column, right_column = st.columns(2)    
    with left_column:
        st.markdown(form_contato, unsafe_allow_html=True)
    with right_column:
        st.empty()
    
    
    

