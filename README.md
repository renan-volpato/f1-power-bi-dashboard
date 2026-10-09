# 🏎️ F1 Power BI Analytics

Projeto de análise de dados da **Fórmula 1**, utilizando Python e Power BI para explorar resultados históricos, identificar padrões e apresentar informações sobre pilotos, construtores, corridas e circuitos.

## 📌 Sobre o projeto

O objetivo deste projeto é transformar dados históricos da Fórmula 1 em informações visuais e análises que facilitem a compreensão do desempenho de pilotos e equipes ao longo das temporadas.

O projeto reúne etapas de inspeção e validação de dados com Python e a construção de um dashboard interativo no Power BI.

## 🛠️ Tecnologias utilizadas

* **Python** — inspeção e validação dos dados.
* **Power BI** — modelagem, criação de indicadores e visualizações interativas.
* **DAX** — criação de medidas e indicadores para o dashboard.
* **CSV** — armazenamento e organização dos dados utilizados.

## 📊 Dashboard

O relatório foi organizado em cinco páginas:

1. **Visão Geral:** indicadores gerais, rankings de pilotos e construtores e evolução dos pontos por temporada.
2. **Análise de Pilotos:** avaliação do desempenho individual, incluindo pontos, vitórias e pódios.
3. **Análise de Construtores:** comparação de equipes com base em pontos, vitórias e pódios.
4. **Corridas e Circuitos:** exploração de temporadas, países e circuitos.
5. **Comparação de Pilotos:** comparação do desempenho de diferentes pilotos ao longo do tempo.

## 🐍 Análise com Python

O projeto utiliza Python e a biblioteca Pandas para inspecionar os arquivos CSV e realizar verificações iniciais da qualidade dos dados históricos da Fórmula 1.

inspect_data.py — Inspeção dos dados

Script responsável por percorrer os arquivos CSV presentes na pasta data/ e apresentar:

Quantidade de registros e colunas de cada arquivo.
Nomes das colunas disponíveis.
Primeiro registro de cada conjunto de dados.

Essa etapa ajuda a compreender a estrutura dos arquivos antes de utilizá-los nas análises e visualizações.

validate_data.py — Validação dos dados

Script que realiza verificações sobre os conjuntos de dados utilizados no projeto, incluindo:

Período histórico: identificação do primeiro e do último ano, quantidade de temporadas e quantidade de corridas.
Verificação de chaves: contagem de registros, IDs únicos e possíveis IDs duplicados nas tabelas de pilotos, construtores, circuitos, corridas, resultados, classificações e status.
Valores ausentes: identificação de colunas que apresentam valores ausentes nos arquivos analisados.

Essas verificações ajudam a identificar características e possíveis problemas nos dados antes de sua utilização no Power BI.

## 📁 Estrutura do repositório

```text
F1-PowerBI-Analytics/
├── data/                  # Dados utilizados no projeto
├── images/                # Capturas de tela do dashboard
├── powerbi/                # Arquivo do Power BI (.pbix)
├── inspect_data.py         # Inspeção dos dados
├── validate_data.py        # Validação dos dados
└── README.md               # Documentação do projeto
```

## 🚀 Como visualizar o projeto

1. Clone este repositório:

   ```bash
   git clone https://github.com/renan-volpato/f1-power-bi-dashboard.git
   ```

2. Entre na pasta do projeto:

   ```bash
   cd F1-PowerBI-Analytics
   ```

3. Para visualizar o relatório, abra o arquivo `.pbix` da pasta `powerbi/` utilizando o Microsoft Power BI Desktop.

4. Para executar os scripts Python, instale uma versão compatível do Python e as dependências necessárias, caso existam, e execute:

   ```bash
   python inspect_data.py
   python validate_data.py
   ```

## 📷 Prévia do dashboard

As capturas de tela do relatório estão disponíveis na pasta `images/`.

<!-- Adicione abaixo as imagens após colocá-las na pasta images. -->

## 📚 Fonte dos dados

Os dados utilizados são referentes a resultados históricos da Fórmula 1.

**Fonte dos dados:** F1 Performance Insights and Analysis(1950 - 2024) [https://www.kaggle.com/code/maroofiums/f1-performance-insights-and-analysis-1950-2024]

Consulte os termos de uso e a licença da fonte antes de redistribuir os arquivos originais.

## 👨‍💻 Autor

Projeto desenvolvido como parte do meu aprendizado em análise de dados, utilizando Python e Power BI.

**GitHub:** [renan-volpato](https://github.com/renan-volpato)
