import streamlit as st
from streamlit_ace import st_ace, THEMES, LANGUAGES

st.title("Editor de Texto")


c1, c2 = st.columns([3, 1])

with c2:
    tema = st.selectbox("Tema", options=THEMES, index=0)
    fonte = st.slider("Fonte", 5, 24, 14)
    linguagem = st.selectbox("Linguagem", options=LANGUAGES, index=121)
    tab_size = st.slider("Tab size", 1, 8, 4)

with c1:
    content = st_ace(
        theme=tema,
        font_size=fonte,
        language=linguagem,
        tab_size=tab_size,
        min_lines=30,
    )


st.write("### Conteúdo Atual")
st.code(content or "", language=linguagem)
