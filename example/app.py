import io
from datetime import datetime

import numpy as np
import pandas as pd
import streamlit as st

# 1. Títulos e Texto
titulo = "Aula Introdutória ao Streamlit"
st.title(titulo)
cabecalho = "Aprendendo os Principais Métodos"
st.header(cabecalho)

# Exibição de Texto
subcabecalho_texto = "Métodos de Exibição de Texto"
st.subheader(subcabecalho_texto)

# Texto simples
texto_simples = (
    "Streamlit facilita a criação de aplicações web interativas com Python."
)
st.text(texto_simples)

# Texto em markdown
texto_markdown = "### Este é um texto em **markdown**!"
st.markdown(texto_markdown)

# Fórmula em LaTeX
formula_latex = r""" e^{i\pi} + 1 = 0 """
st.latex(formula_latex)

# Código
codigo_exemplo = "x = 42"
st.code(codigo_exemplo)

# 2. Exibição de Dados
subcabecalho_dados = "Exibição de Dados"
st.subheader(subcabecalho_dados)

# Dados do DataFrame
data = {"A": [1, 2, 3, 4], "B": [10, 20, 30, 40]}
df = pd.DataFrame(data)
st.dataframe(df)

# JSON
json_exemplo = {"name": "Streamlit", "type": "Web Framework"}
st.json(json_exemplo)

# CSV como string
csv_exemplo = df.to_csv(index=False)

# Lista
lista_exemplo = [1, 2, 3, 4, 5]
st.write(lista_exemplo)

# 3. Métricas
subcabecalho_metricas = "Métricas"
st.subheader(subcabecalho_metricas)

col1, col2 = st.columns(2)

# Métricas com delta
with col1:
    temperatura = {"label": "Temperatura", "value": "70 °F", "delta": "1.2 °F"}
    st.metric(label="Temperatura",
            value= "70 °F",
            delta= "-1.2 °F")
with col2:
    umidade = {"label": "Umidade", "value": "60%", "delta": "-5%"}
    st.metric(label="Umidade",
            value= "60%",
            delta= "-5%")

vento = {"label": "Velocidade do Vento", "value": "15 km/h", "delta": "2 km/h"}
ruido = {"label": "Nível de Ruído", "value": "40 dB", "delta": "1.5 dB"}
pressao = {
    "label": "Pressão Atmosférica",
    "value": "1013 hPa",
    "delta": "2 hPa",
}

# Métrica sem delta
populacao = {"label": "População", "value": "8 bilhões"}

# 4. Gráficos
subcabecalho_graficos = "Gráficos"

# Dados dos gráficos
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.line_chart(chart_data)
st.area_chart(chart_data)
st.bar_chart(chart_data)


# Mais exemplos de gráficos
mais_graficos = "Mais Exemplos de Gráficos"
st.subheader(mais_graficos)  # Exibe um subcabeçalho


# Dados do gráfico de dispersão
scatter_data = pd.DataFrame(np.random.randn(100, 2), columns=["x", "y"])
st.plotly_chart(
    {
        "data": [
            {
                "x": scatter_data["x"],
                "y": scatter_data["y"],
                "type": "scatter",
                "mode": "markers",
            }
        ],
        "layout": {"title": "Gráfico de Dispersão"},
    }
)  # Exibe um gráfico de dispersão

# Dados do histograma
hist_data = np.random.randn(1000)
st.plotly_chart(
    {
        "data": [{"x": hist_data, "type": "histogram"}],
        "layout": {"title": "Histograma"},
    }
)  # Exibe um histograma

# 5. Mapas
subcabecalho_mapas = "Mapas"

# Dados do mapa
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=["lat", "lon"],
)
st.map(map_data)  # Exibe um mapa com pontos aleatórios

# 6. Mídia
subcabecalho_midia = "Mídia"

# URL da imagem
imagem_url = "https://www.streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png"
imagem_legenda = "Streamlit Logo"
st.image(imagem_url, caption=imagem_legenda)

# URL do áudio
audio_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
st.audio(audio_url)

# URL do vídeo
video_url = "https://www.youtube.com/watch?v=B2iAodr0fOo"
st.video(video_url)

# 7. Widgets
subcabecalho_widgets = "Widgets"
st.subheader(subcabecalho_widgets)

# Botão
botao = "Clique aqui"
botao_mensagem = "Botão clicado!"

if st.button("botao"):
    st.text(botao_mensagem)

# Checkbox
checkbox_label = "Eu aceito os termos e condições"
bool_aceite = st.checkbox("voce aceita os termos?")

st.write(bool_aceite)

# Radio
radio_label = "Escolha uma opção"
radio_options = ("Opção 1", "Opção 2", "Opção 3")

opcao_radio = st.radio("Escolha uma opção", ("Opção 1", "Opção 2", "Opção 3"))
st.write("Opção escolhida:", opcao_radio)  # Exibe a opção selecionada


# Selectbox
selectbox_label = "Selecione uma opção"
selectbox_options = ["Opção A", "Opção B", "Opção C"]

# Multiselect
multiselect_label = "Selecione múltiplas opções"
multiselect_options = ["Opção 1", "Opção 2", "Opção 3"]

# Slider
slider_label = "Selecione um valor"
slider_min = 0
slider_max = 100
slider_default = 50

# Select Slider
select_slider_label = "Selecione um intervalo"
select_slider_options = ["a", "b", "c", "d"]
select_slider_default = ("b", "c")

# Text Input
text_input_label = "Digite seu nome"

# Number Input
number_input_label = "Selecione um número"
number_input_min = 0
number_input_max = 100

# Text Area
text_area_label = "Escreva um texto"

# Date Input
date_input_label = "Selecione uma data"
date_input_default = datetime.now()

# Sidebar
sidebar_title = "Barra Lateral"
sidebar_button_label = "Botão na Barra Lateral"
sidebar_button_message = "Botão na barra lateral clicado!"

# Carregar CSV
subcabecalho_csv = "Carregar CSV"
file_uploader_label = "Escolha um arquivo CSV"
file_uploader_type = "csv"


# Função para converter DataFrame para Parquet
@st.cache_data
def convert_df_to_parquet(df):
    output = io.BytesIO()
    df.to_parquet(output, index=False)
    return output.getvalue()


download_button_label_parquet = "Baixar dados como Parquet"
download_button_filename_parquet = "dados.parquet"
download_button_mime_parquet = "application/octet-stream"