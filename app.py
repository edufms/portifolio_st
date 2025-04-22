import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
import base64
from streamlit_option_menu import option_menu
import time

# Configuração da página
st.set_page_config(
    page_title="Eduardo Machado | Analista de Dados",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado
def local_css():
    st.markdown("""
    <style>
        /* Cores personalizadas */
        :root {
            --primary-color: #1E40AF;
            --accent-color: #60A5FA;
            --background-dark: #0F172A;
            --text-color: #F1F5F9;
        }
        
        /* Personalizando a cor de fundo principal */
        .stApp {
            background-color: var(--background-dark);
            color: var(--text-color);
            background-image: radial-gradient(#64748b 0.5px, transparent 0.5px);
            background-size: 15px 15px;
        }
        
        /* Cabeçalhos */
        h1, h2, h3 {
            color: white;
        }
        
        /* Cards */
        .css-1r6slb0, .css-keje6w {
            background-color: rgba(30, 64, 175, 0.2);
            border-radius: 10px;
            padding: 20px;
            border: 1px solid rgba(96, 165, 250, 0.3);
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .css-1r6slb0:hover, .css-keje6w:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 25px -5px rgba(59, 130, 246, 0.4);
        }
        
        /* Customização do sidebar */
        .css-1d391kg {
            background-color: rgba(15, 23, 42, 0.9);
        }
        
        /* Botões */
        .stButton>button {
            background-color: var(--primary-color);
            color: white;
            border: none;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            transition: background-color 0.3s;
        }
        
        .stButton>button:hover {
            background-color: var(--accent-color);
        }
        
        /* Barra de progresso */
        .stProgress > div > div {
            background-color: var(--primary-color);
        }
        
        /* Containers com bordas */
        .highlight-container {
            background-color: rgba(30, 64, 175, 0.2);
            border-radius: 10px;
            padding: 20px;
            border: 1px solid rgba(96, 165, 250, 0.3);
            margin-bottom: 20px;
        }
        
        /* Menu do sidebar */
        .nav-link {
            background-color: transparent !important;
            color: var(--text-color) !important;
            text-align: left !important;
            font-weight: normal !important;
            padding: 0.5rem 1rem !important;
        }
        
        .nav-link:hover {
            background-color: rgba(96, 165, 250, 0.2) !important;
            color: white !important;
        }
        
        .nav-link-selected {
            background-color: var(--primary-color) !important;
            color: white !important;
            font-weight: bold !important;
        }
        
        /* Tabelas */
        .stDataFrame {
            background-color: rgba(30, 64, 175, 0.2);
            border-radius: 10px;
            border: 1px solid rgba(96, 165, 250, 0.3);
        }
        
        /* Animação fade-in */
        @keyframes fadeIn {
            from {opacity: 0;}
            to {opacity: 1;}
        }
        
        .fade-in {
            animation: fadeIn 1s ease;
        }
        
        /* Badge/Tags para habilidades */
        .badge {
            background-color: rgba(96, 165, 250, 0.3);
            color: white;
            padding: 5px 10px;
            border-radius: 5px;
            margin-right: 5px;
            font-size: 0.8rem;
        }
        
        /* Linha divisória */
        .divider {
            width: 80px;
            height: 4px;
            background-color: var(--primary-color);
            margin: 10px 0 20px 0;
        }
        
        /* Icones com cores */
        .icon-blue {
            color: var(--accent-color);
            font-size: 2rem;
            margin-right: 10px;
        }
        
        /* Foto de perfil circular */
        .profile-pic {
            border-radius: 50%;
            border: 3px solid var(--accent-color);
        }
        
    </style>
    """, unsafe_allow_html=True)

# Função para criar badges de habilidades
def create_badge(text):
    return f'<span class="badge">{text}</span>'

# Função para criar divisor
def create_divider():
    return '<div class="divider"></div>'

# Função para carregar dados de exemplo
def load_example_data():
    # Dados de exemplo para visualização
    data = {
        'Mês': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
        'Vendas': [12500, 13000, 15000, 14500, 16000, 18000, 19500, 17500, 20000, 21500, 22000, 24000],
        'Marketing': [5000, 5200, 5500, 5300, 5800, 6200, 6500, 6000, 6700, 7000, 7200, 7500],
        'Custos': [8000, 8100, 8300, 8200, 8500, 8700, 9000, 8800, 9200, 9400, 9500, 9800]
    }
    return pd.DataFrame(data)

# Função para mostrar barra de habilidades
def show_skill_bar(label, percentage):
    st.markdown(f"**{label}**")
    st.progress(percentage/100)

# Função para criar container com animação
def animated_container(content, key):
    with st.container():
        st.markdown(f'<div class="highlight-container fade-in">{content}</div>', unsafe_allow_html=True)

# Aplicar CSS
local_css()

# Navegação na barra lateral
with st.sidebar:
    st.markdown('<h1 style="text-align: center;">Eduardo<span style="color: #60A5FA;">.dev</span></h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center;">Analista de Dados</p>', unsafe_allow_html=True)
    
    # Placeholder para foto do perfil
    st.image("https://via.placeholder.com/300", caption="Eduardo Machado", use_column_width=True)
    
    selected = option_menu(
        "",
        ["Início", "Sobre Mim", "Habilidades", "Projetos", "Dashboard Demo", "Contato"],
        icons=['house', 'person', 'gear', 'code-slash', 'bar-chart', 'envelope'],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": "#60A5FA", "font-size": "18px"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "padding": "10px", "border-radius": "5px"},
            "nav-link-selected": {"background-color": "#1E40AF", "font-weight": "bold"},
        }
    )
    
    st.markdown("---")
    st.markdown("### Contato Rápido")
    st.markdown("📧 eduardo.machado@email.com")
    st.markdown("📱 (11) 98765-4321")
    st.markdown("📍 São Paulo, SP")
    
    st.markdown("---")
    st.markdown("### Redes Sociais")
    cols = st.columns(4)
    with cols[0]:
        st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com)")
    with cols[1]:
        st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com)")
    with cols[2]:
        st.markdown("[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com)")
    with cols[3]:
        st.markdown("[![Medium](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com)")

# Página Inicial
if selected == "Início":
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<h1 class="fade-in">Olá, eu sou <span style="color: #60A5FA;">Eduardo Machado</span></h1>', unsafe_allow_html=True)
        st.markdown('<h3 class="fade-in">Analista de Dados</h3>', unsafe_allow_html=True)
        
        st.markdown("""
        <div class="fade-in" style="animation-delay: 0.3s;">
            <p style="font-size: 1.2rem; margin-top: 20px; margin-bottom: 30px;">
                Transformando dados em insights valiosos e soluções de negócios.
                Especialista em SQL, Python, Power BI e visualização de dados.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        col_btn1, col_btn2, _ = st.columns([1, 1, 2])
        
        with col_btn1:
            st.button("Ver Projetos", key="ver_projetos")
        
        with col_btn2:
            st.button("Contate-me", key="contate_me")
        
        # Animação de digitação para estatísticas
        st.markdown("### Estatísticas Rápidas")
        
        metrics_col1, metrics_col2, metrics_col3 = st.columns(3)
        
        with metrics_col1:
            st.metric(label="Projetos Concluídos", value="34+")
        
        with metrics_col2:
            st.metric(label="Anos de Experiência", value="8+")
        
        with metrics_col3:
            st.metric(label="Clientes Satisfeitos", value="25+")
    
    with col2:
        # Gráfico animado para demonstrar habilidades
        fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = 85,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "Performance em Análise de Dados", 'font': {'color': "white"}},
            gauge = {
                'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "white"},
                'bar': {'color': "#60A5FA"},
                'bgcolor': "rgba(30, 64, 175, 0.2)",
                'borderwidth': 2,
                'bordercolor': "white",
                'steps': [
                    {'range': [0, 50], 'color': 'rgba(30, 64, 175, 0.2)'},
                    {'range': [50, 85], 'color': 'rgba(30, 64, 175, 0.5)'}],
                'threshold': {
                    'line': {'color': "white", 'width': 4},
                    'thickness': 0.75,
                    'value': 85}}))
        
        fig.update_layout(
            paper_bgcolor = "rgba(0,0,0,0)",
            plot_bgcolor = "rgba(0,0,0,0)",
            font = {'color': "white", 'family': "Arial"},
            height = 300,
            margin = dict(l=20, r=20, t=50, b=20)
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Informações extras
        st.info("📌 Disponível para novos projetos e consultorias em análise de dados.")

# Página Sobre
elif selected == "Sobre Mim":
    st.markdown('<h1 class="fade-in">Sobre Mim</h1>', unsafe_allow_html=True)
    st.markdown(create_divider(), unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Placeholder para foto do perfil
        st.image("https://via.placeholder.com/400", use_column_width=True)
        
        st.markdown("### Informações Pessoais")
        info_data = {
            "Nome": "Eduardo Machado",
            "Idade": "36 anos",
            "Localização": "São Paulo, SP",
            "Ocupação": "Analista de Dados",
            "E-mail": "eduardo.machado@email.com"
        }
        
        for key, value in info_data.items():
            st.markdown(f"**{key}:** {value}")
    
    with col2:
        st.markdown("""
        <div class="highlight-container fade-in">
            <h2>Minha Jornada</h2>
            <p style="font-size: 1.1rem; line-height: 1.6;">
                Sou Eduardo Machado, um Analista de Dados com paixão por transformar dados brutos em insights valiosos que impulsionam decisões estratégicas. Com 36 anos de idade e baseado em São Paulo, tenho concentrado minha carreira na interseção entre tecnologia e análise de dados.
            </p>
            <p style="font-size: 1.1rem; line-height: 1.6; margin-top: 15px;">
                Minha experiência envolve a implementação de soluções de Business Intelligence, análise exploratória de dados, modelagem estatística e desenvolvimento de dashboards interativos. Estou constantemente aprimorando minhas habilidades técnicas e acompanhando as tendências emergentes no campo da análise de dados e ciência de dados.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<h3>Formação Acadêmica</h3>", unsafe_allow_html=True)
        
        col_edu1, col_edu2 = st.columns(2)
        
        with col_edu1:
            st.markdown("""
            <div class="highlight-container">
                <h4>Graduação em Ciência da Computação</h4>
                <p>Universidade de São Paulo (USP)</p>
                <p><small>2010 - 2014</small></p>
            </div>
            """, unsafe_allow_html=True)
        
        with col_edu2:
            st.markdown("""
            <div class="highlight-container">
                <h4>MBA em Business Intelligence</h4>
                <p>Fundação Getúlio Vargas (FGV)</p>
                <p><small>2016 - 2018</small></p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<h3>Experiência Profissional</h3>", unsafe_allow_html=True)
        
        st.markdown("""
        <div class="highlight-container">
            <h4>Analista de Dados Sênior</h4>
            <p>Empresa Tecnológica Inovadora</p>
            <p><small>2020 - Presente</small></p>
            <p>Desenvolvimento de soluções de análise avançada, implementação de dashboards interativos e coordenação de iniciativas de data science.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="highlight-container">
            <h4>Analista de Business Intelligence</h4>
            <p>Empresa Multinacional</p>
            <p><small>2017 - 2020</small></p>
            <p>Criação de relatórios automatizados, modelagem de dados e suporte à tomada de decisões baseadas em dados.</p>
        </div>
        """, unsafe_allow_html=True)

# Página Habilidades
elif selected == "Habilidades":
    st.markdown('<h1 class="fade-in">Minhas Habilidades</h1>', unsafe_allow_html=True)
    st.markdown(create_divider(), unsafe_allow_html=True)
    
    # Habilidades técnicas
    st.markdown("### Habilidades Técnicas")
    
    col1, col2 = st.columns(2)
    
    with col1:
        show_skill_bar("SQL", 95)
        show_skill_bar("Python", 90)
        show_skill_bar("Power BI", 92)
    
    with col2:
        show_skill_bar("Excel", 97)
        show_skill_bar("Visualização de Dados", 88)
        show_skill_bar("ETL & Data Pipeline", 85)
    
    # Categorias de habilidades
    st.markdown("### Áreas de Especialização")
    
    categories_col1, categories_col2, categories_col3 = st.columns(3)
    
    with categories_col1:
        st.markdown("""
        <div class="highlight-container">
            <h4>Bancos de Dados</h4>
            """ + 
            create_badge("SQL Server") + 
            create_badge("MySQL") + 
            create_badge("PostgreSQL") + 
            create_badge("MongoDB") + 
            """
            <p style="margin-top: 15px;">Experiência em consultas complexas, modelagem de dados e otimização de performance.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with categories_col2:
        st.markdown("""
        <div class="highlight-container">
            <h4>Análise de Dados</h4>
            """ + 
            create_badge("Pandas") + 
            create_badge("NumPy") + 
            create_badge("Scikit-learn") + 
            create_badge("Matplotlib") + 
            """
            <p style="margin-top: 15px;">Domínio em bibliotecas de manipulação e visualização de dados em Python.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with categories_col3:
        st.markdown("""
        <div class="highlight-container">
            <h4>Business Intelligence</h4>
            """ + 
            create_badge("Power BI") + 
            create_badge("Tableau") + 
            create_badge("DAX") + 
            create_badge("Looker") + 
            """
            <p style="margin-top: 15px;">Criação de dashboards interativos e relatórios analíticos.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Segunda linha
    categories_col4, categories_col5, categories_col6 = st.columns(3)
    
    with categories_col4:
        st.markdown("""
        <div class="highlight-container">
            <h4>ETL e Data Pipeline</h4>
            """ + 
            create_badge("SSIS") + 
            create_badge("Airflow") + 
            create_badge("Pentaho") + 
            create_badge("Luigi") + 
            """
            <p style="margin-top: 15px;">Implementação de processos de extração, transformação e carregamento de dados.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with categories_col5:
        st.markdown("""
        <div class="highlight-container">
            <h4>Cloud Computing</h4>
            """ + 
            create_badge("AWS") + 
            create_badge("Azure") + 
            create_badge("GCP") + 
            create_badge("Databricks") + 
            """
            <p style="margin-top: 15px;">Experiência em plataformas cloud para análise e armazenamento de dados.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with categories_col6:
        st.markdown("""
        <div class="highlight-container">
            <h4>Análise Estatística</h4>
            """ + 
            create_badge("R") + 
            create_badge("SPSS") + 
            create_badge("Minitab") + 
            create_badge("SAS") + 
            """
            <p style="margin-top: 15px;">Aplicação de métodos estatísticos para análise de dados e tomada de decisão.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Certificações
    st.markdown("### Certificações")
    
    cert_col1, cert_col2, cert_col3 = st.columns(3)
    
    with cert_col1:
        st.markdown("""
        <div class="highlight-container">
            <h4>Microsoft Certified: Data Analyst Associate</h4>
            <p><small>Microsoft, 2023</small></p>
        </div>
        """, unsafe_allow_html=True)
    
    with cert_col2:
        st.markdown("""
        <div class="highlight-container">
            <h4>Python Data Science Certificate</h4>
            <p><small>DataCamp, 2022</small></p>
        </div>
        """, unsafe_allow_html=True)
    
    with cert_col3:
        st.markdown("""
        <div class="highlight-container">
            <h4>AWS Certified Data Analytics</h4>
            <p><small>Amazon Web Services, 2023</small></p>
        </div>
        """, unsafe_allow_html=True)

# Página de Projetos
elif selected == "Projetos":
    st.markdown('<h1 class="fade-in">Projetos</h1>', unsafe_allow_html=True)
    st.markdown(create_divider(), unsafe_allow_html=True)
    
    # Filtros
    st.markdown("### Filtrar Projetos")
    
    col_filter1, col_filter2, col_filter3 = st.columns(3)
    
    with col_filter1:
        categoria = st.selectbox("Categoria", ["Todos", "Business Intelligence", "Machine Learning", "ETL", "Visualização"])
    
    with col_filter2:
        tecnologia = st.selectbox("Tecnologia", ["Todas", "Python", "SQL", "Power BI", "Excel", "Tableau"])
    
    with col_filter3:
        ano = st.selectbox("Ano", ["Todos", "2025", "2024", "2023", "2022", "2021"])
    
    # Projetos
    st.markdown("### Projetos Destacados")
    
    # Projeto 1
    with st.expander("Dashboard Financeiro", expanded=True):
        proj1_col1, proj1_col2 = st.columns([1, 2])
        
        with proj1_col1:
            st.image("https://via.placeholder.com/400x300", use_column_width=True)
        
        with proj1_col2:
            st.markdown("""
            <h4>Dashboard Financeiro</h4>
            <p style="margin-bottom: 10px;">
                """ + 
                create_badge("Power BI") + 
                create_badge("SQL") + 
                create_badge("DAX") + 
                """
            </p>
            <p>Desenvolvimento de dashboard interativo para análise financeira com Power BI, conectando múltiplas fontes de dados.</p>
            <h5>Principais recursos:</h5>
            <ul>
                <li>Indicadores financeiros em tempo real</li>
                <li>Análise comparativa entre períodos</li>
                <li>Previsão de receita e despesas</li>
                <li>Detalhamento por departamento e centro de custo</li>
            </ul>
            """, unsafe_allow_html=True)
            
            st.button("Ver detalhes do projeto", key="proj1_details")
    
    # Projeto 2
    with st.expander("Modelo Preditivo de Vendas"):
        proj2_col1, proj2_col2 = st.columns([1, 2])
        
        with proj2_col1:
            st.image("https://via.placeholder.com/400x300", use_column_width=True)
        
        with proj2_col2:
            st.markdown("""
            <h4>Modelo Preditivo de Vendas</h4>
            <p style="margin-bottom: 10px;">
                """ + 
                create_badge("Python") + 
                create_badge("Scikit-learn") + 
                create_badge("Pandas") + 
                """
            </p>
            <p>Implementação de modelo de machine learning para previsão de vendas usando séries temporais e análise de fatores externos.</p>
            <h5>Principais recursos:</h5>
            <ul>
                <li>Previsão de vendas com precisão de 87%</li>
                <li>Análise de sazonalidade e tendências</li>
                <li>Identificação de fatores que influenciam vendas</li>
                <li>Relatórios automatizados de previsão</li>
            </ul>
            """, unsafe_allow_html=True)
            
            st.button("Ver detalhes do projeto", key="proj2_details")
    
    # Projeto 3
    with st.expander("ETL Automatizado"):
        proj3_col1, proj3_col2 = st.columns([1, 2])
        
        with proj3_col1:
            st.image("https://via.placeholder.com/400x300", use_column_width=True)
        
        with proj3_col2:
            st.markdown("""
            <h4>ETL Automatizado</h4>
            <p style="margin-bottom: 10px;">
                """ + 
                create_badge("Python") + 
                create_badge("Airflow") + 
                create_badge("PostgreSQL") + 
                """
            </p>
            <p>Desenvolvimento de pipeline de dados para automatizar a extração, transformação e carregamento de informações de vendas.</p>
            <h5>Principais recursos:</h5>
            <ul>
                <li>Pipeline automatizado com execução diária</li>
                <li>Monitoramento e notificação de erros</li>
                <li>Interface de controle e gestão</li>
                <li>Integração com múltiplas fontes de dados</li>
            </ul>
            """, unsafe_allow_html=True)
            
            st.button("Ver detalhes do projeto", key="proj3_details")
    
    # Projeto 4
    with st.expander("Análise de Sentimento de Clientes"):
        proj4_col1, proj4_col2 = st.columns([1, 2])
        
        with proj4_col1:
            st.image("https://via.placeholder.com/400x300", use_column_width=True)
        
        with proj4_col2:
            st.markdown("""
            <h4>Análise de Sentimento de Clientes</h4>
            <p style="margin-bottom: 10px;">
                """ + 
                create_badge("Python") + 
                create_badge("NLTK") + 
                create_badge("Tableau") + 
                """
            </p>
            <p>Implementação de análise de sentimento para avaliar feedback de clientes em redes sociais e plataformas de avaliação.</p>
            <h5>Principais recursos:</h5>
            <ul>
                <li>Classificação automática de sentimento</li>
                <li>Identificação de temas recorrentes</li>
                <li>Dashboard de monitoramento em tempo real</li>
                <li>Alertas para avaliações negativas</li>
            </ul>
            """, unsafe_allow_html=True)
            
            st.button("Ver detalhes do projeto", key="proj4_details")

# Página de Dashboard Demo
elif selected == "Dashboard Demo":
    st.markdown('<h1 class="fade-in">Dashboard Demo</h1>', unsafe_allow_html=True)
    st.markdown(create_divider(), unsafe_allow_html=True)
    
    st.info("Esta é uma demonstração interativa das minhas habilidades em visualização de dados usando Streamlit.")
    
    # Carregando dados de exemplo
    df = load_example_data()
    
    # Filtros interativos
    filter_container = st.container()
    with filter_container:
        st.markdown("### Filtros")
        filter_col1, filter_col2 = st.columns(2)
        
        with filter_col1:
            start_month = st.select_slider("Mês Inicial", options=df['Mês'], value='Jan')
        
        with filter_col2:
            end_month = st.select_slider("Mês Final", options=df['Mês'], value='Dez')
    
    # Filtrando dados conforme seleção
    start_idx = df[df['Mês'] == start_month].index[0]
    end_idx = df[df['Mês'] == end_month].index[0]
    
    if start_idx <= end_idx:
        filtered_df = df.iloc[start_idx:end_idx+1]
    else:
        st.error("O mês selecionado não existe")