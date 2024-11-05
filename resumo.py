import streamlit as st
import os

# Função para ler o contador de acessos
def read_counter():
    if os.path.exists('contador.txt'):
        with open('contador.txt', 'r') as f:
            count = int(f.read())
    else:
        count = 0
    return count

# Função para incrementar o contador de acessos
def increment_counter():
    count = read_counter() + 1
    with open('contador.txt', 'w') as f:
        f.write(str(count))
    return count

# Configuração da página
st.set_page_config(
    page_title="Resumos Nobrega Medtech",
    page_icon="📝",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Incrementa o contador de acessos
access_count = increment_counter()

# Título e descrição do aplicativo
st.title("📝 Resumos Nobrega Medtech")
st.write(f"Bem-vindo ao aplicativo de resumos médicos. Esta página foi acessada **{access_count}** vezes.")

# Obtém a lista de arquivos no diretório atual, excluindo o próprio script e arquivos ocultos
files = [f for f in os.listdir('.') if os.path.isfile(f)
         and f != os.path.basename(__file__)
         and not f.startswith('.')
         and f != 'contador.txt']

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

