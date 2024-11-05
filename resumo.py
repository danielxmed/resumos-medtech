import streamlit as st
import os

# Configuração da página
st.set_page_config(
    page_title="Resumos Nobrega Medtech",
    page_icon="📝",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Título e descrição do aplicativo
st.title("📝 Resumos Nobrega Medtech")
st.write("Bem-vindo ao aplicativo de resumos médicos. Aqui você pode baixar resumos de diversos temas médicos.")

# Obtém a lista de arquivos no diretório atual
files = [f for f in os.listdir('.') if os.path.isfile(f) and f != os.path.basename(__file__) and not f.startswith('.')]

if not files:
    st.write("Nenhum arquivo disponível para download.")
else:
    st.subheader("Resumos Disponíveis:")
    for file in files:
        with open(file, 'rb') as f:
            file_contents = f.read()
            st.markdown(f"**{file}**")
            st.download_button(
                label="📥 Baixar",
                data=file_contents,
                file_name=file,
                mime='application/octet-stream'
            )
            st.write("---")
