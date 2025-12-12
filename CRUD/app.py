import streamlit as st
from database import *

st.set_page_config(page_title="CRUD com Streamlit", layout="centered")


create_table()

st.title("CRUD Streamlit")

menu = ["Cadastrar", "Listar", "Atualizar", "Excluir"]
escolha = st.sidebar.selectbox("Menu", menu)


if escolha == "Cadastrar":
    st.subheader("Cadastrar Usuário")

    nome = st.text_input("Nome")
    email = st.text_input("Email")

    if st.button("Salvar"):
        add_user(nome, email)
        st.success("Usuário cadastrado com sucesso!")


elif escolha == "Listar":
    st.subheader("Lista de Usuários")

    usuarios = get_users()
    if usuarios:
        for u in usuarios:
            st.write(f"**ID:** {u[0]} | **Nome:** {u[1]} | **Email:** {u[2]}")
            st.markdown("---")
    else:
        st.info("Nenhum usuário cadastrado.")


elif escolha == "Atualizar":
    st.subheader("Atualizar Usuário")

    usuarios = get_users()
    ids = [u[0] for u in usuarios]

    user_id = st.selectbox("Selecione o usuário pelo ID", ids)

    novo_nome = st.text_input("Novo nome")
    novo_email = st.text_input("Novo email")

    if st.button("Atualizar"):
        update_user(user_id, novo_nome, novo_email)
        st.success("Usuário atualizado com sucesso!")


elif escolha == "Excluir":
    st.subheader("Excluir Usuário")

    usuarios = get_users()
    ids = [u[0] for u in usuarios]

    user_id = st.selectbox("Selecione o usuário pelo ID", ids)

    if st.button("Excluir"):
        delete_user(user_id)
        st.error("Usuário removido com sucesso!")
