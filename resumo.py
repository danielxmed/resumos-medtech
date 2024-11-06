import streamlit as st
import os

# Configuração da página
st.set_page_config(
    page_title="Resumos Nobrega Medtech",
    page_icon="🛒",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Título e descrição do aplicativo
st.title("🛒 Resumos Nobrega Medtech")
st.write("Bem-vindo ao aplicativo de resumos médicos. Aqui você pode baixar resumos de diversos temas médicos.")

# Inserir banners de produtos na barra lateral
with st.sidebar:
    st.header("Publicidade - Produtos Amazon")
    
    # Banner do produto com link de afiliado
    st.markdown(
        """
        <a href="https://www.amazon.com.br?&linkCode=ll2&tag=99014451-20&linkId=ccd472bd1bab09517db7ce24f826b722&language=pt_BR&ref_=as_li_ss_tl" target="_blank">
            <img src="https://m.media-amazon.com/images/I/41NsOExj+QL._SY445_SX342_.jpg" alt="Produto Amazon" style="width:100%;border-radius:10px;">
        </a>
        """,
        unsafe_allow_html=True,
    )

    # Contador de acessos
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

# Lista de arquivos disponíveis
contador_file = 'contador.txt'  # Nome do arquivo de contador
script_file = os.path.basename(__file__)  # Nome do próprio script

excluded_files = [script_file, contador_file]

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
