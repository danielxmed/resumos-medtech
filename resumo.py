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

# Inserir Google Ads na barra lateral
with st.sidebar:
    st.header("Publicidade")
    ad_code = """
    <!-- Código do Google AdSense -->
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4467862565929473"
     crossorigin="anonymous"></script>
    <!-- Bloco de anúncio -->
    <ins class="adsbygoogle"
         style="display:block"
         data-ad-client="ca-pub-4467862565929473"
         data-ad-slot="SEU_AD_SLOT_ID"
         data-ad-format="auto"
         data-full-width-responsive="true"></ins>
    <script>
         (adsbygoogle = window.adsbygoogle || []).push({});
    </script>
    """
    components.html(ad_code, height=300)

# Função para atualizar o contador de acessos
def update_counter():
    if 'visit_count' not in st.session_state:
        if os.path.exists('visit_count.txt'):
            with open('visit_count.txt', 'r') as f:
                count = int(f.read())
        else:
            count = 0
        count += 1
        with open('visit_count.txt', 'w') as f:
            f.write(str(count))
        st.session_state.visit_count = count
    return st.session_state.visit_count

# Atualizar e exibir o contador
visit_count = update_counter()
st.sidebar.write(f"👁️ Número de acessos: {visit_count}")

# Obtém a lista de arquivos no diretório atual
files = [f for f in os.listdir('.') if os.path.isfile(f) and f != os.path.basename(__file__) and not f.startswith('.') and f != 'visit_count.txt']

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

