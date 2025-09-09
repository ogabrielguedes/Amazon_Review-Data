# 📊 Análise de Sentimento em Avaliações de Produtos Online (Streamlit Dashboard)

Este projeto demonstra uma abordagem completa para analisar avaliações de produtos, transformando dados brutos de feedback de clientes em insights acionáveis para a tomada de decisão de negócios. Utilizando Python com SQL, Pandas, NLTK e Streamlit, construí uma dashboard interativa capaz de revelar o verdadeiro sentimento dos consumidores, além da simples nota do produto.

## 🌟 O Problema
No universo do e-commerce, a nota média de um produto (e.g., 4.5 estrelas) muitas vezes não revela a história completa. Empresas precisam ir além e entender **o que** impulsiona a satisfação ou insatisfação dos clientes nos comentários, para otimizar produtos, marketing e operações.

## 🚀 A Solução
Desenvolvi uma solução que:
1.  **Extrai dados** de avaliações de produtos diretamente de um banco de dados **SQLite**.
2.  **Limpa e processa** um grande volume de dados (mais de 500.000 avaliações).
3.  Aplica **Processamento de Linguagem Natural (NLP)** com a biblioteca NLTK (VADER) para classificar o sentimento de cada comentário como 'Positivo', 'Negativo' ou 'Neutro'.
4.  Apresenta os insights de forma interativa através de uma **dashboard construída com Streamlit**.

## ✨ Insights Chave
* **Além da Nota Média:** O projeto revela que um produto pode ter uma nota geral alta, mas ainda apresentar um volume significativo de sentimentos negativos em aspectos específicos, não visíveis na média.
* **Pontos Fortes e Fracos:** A análise de sentimento permite identificar padrões nas reclamações (e.g., "bateria fraca", "entrega atrasada") e nos elogios (e.g., "design elegante", "fácil de usar"), oferecendo um diagnóstico preciso.
* **Tomada de Decisão Acionável:** Com esses insights, empresas podem direcionar esforços para melhorias no produto, refinar estratégias de marketing focando nos pontos fortes, ou otimizar processos operacionais (logística, suporte ao cliente).

## 🛠️ Tecnologias Utilizadas
* **Python:** Linguagem principal de desenvolvimento.
* **SQL (SQLite):** Armazenamento e extração de dados.
* **Pandas:** Manipulação e análise de dados.
* **NLTK (VADER):** Análise de Sentimento (NLP).
* **Seaborn/Matplotlib:** Visualização de dados.
* **Streamlit:** Construção da dashboard interativa.

## 👨‍💻 Como Rodar o Projeto
1.  **Baixe o arquivo de dados:** O arquivo `database.sqlite` é muito grande para ser hospedado no GitHub. Faça o download dele através deste link:
    [Download database.sqlite](https://drive.google.com/file/d/1boXr3JUSp_iqAgsKt8GpJJko-OBTQoNh/view?usp=drive_link)

2.  **Clone o repositório:**
   
3.  **Mova o arquivo de dados:** Coloque o arquivo `database.sqlite` na mesma pasta onde o código está.

4.  **Instale as dependências:**
    ```bash
    pip install pandas sqlalchemy seaborn matplotlib nltk streamlit
    ```
5.  **Baixe o lexicon do NLTK** (apenas na primeira vez):
    ```python
    import nltk
    nltk.download('vader_lexicon')
    ```
6.  **Execute a dashboard:**
    ```bash
    streamlit run data_base.py
    ```

---
**<img width="546" height="755" alt="image" src="https://github.com/user-attachments/assets/28eb9c9d-f04d-4d77-8b13-8b4b15005b74" />
**
