import streamlit as st
import os
import streamlit.components.v1 as components

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

# Inserir o link de afiliado da Amazon na barra lateral
with st.sidebar:
    st.header("Publicidade")
    amazon_affiliate_link = "https://www.amazon.com.br?&linkCode=ll2&tag=99014451-20&linkId=0990949aebff31b1838d3b03c331432d&language=pt_BR&ref_=as_li_ss_tl"

    # Exibir o link como um botão estilizado
    st.markdown(
        f"""
        <a href="{amazon_affiliate_link}" target="_blank">
            <button style="background-color:orange;color:white;padding:10px 20px;border:none;border-radius:5px;cursor:pointer;">
                🛒 Ver Ofertas da Amazon
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )

    # Função para atualizar o contador de acessos
    def update_counter():
        contador_file = 'contador.txt'  # Nome do arquivo de contador
        if 'visit_count' not in st.session_state:
            if os.path.exists(contador_file):
                with open(contador_file, 'r') as f:
                    try:
                        count = int(f.read())
                    except ValueError:
                        count = 0
            else:
                count = 0
            count += 1
            with open(contador_file, 'w') as f:
                f.write(str(count))
            st.session_state.visit_count = count
        return st.session_state.visit_count

    # Atualizar e exibir o contador
    visit_count = update_counter()
    st.sidebar.write(f"👁️ Número de acessos: {visit_count}")

# Definir lista de arquivos a serem excluídos
contador_file = 'contador.txt'  # Nome do arquivo de contador para exclusão
script_file = os.path.basename(__file__)  # Nome do próprio script

excluded_files = [script_file, contador_file]

# Se houver outros arquivos para excluir, adicione-os à lista
# excluded_files.append('visit_count.txt')

# Obtém a lista de arquivos no diretório atual, excluindo os indesejados
files = [
    f for f in os.listdir('.')
    if os.path.isfile(f)
    and f not in excluded_files
    and not f.startswith('.')
]

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
