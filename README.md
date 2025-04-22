
# 🏢🔍 Localizador de Sites de Empresas com Python 🐍

Este projeto tem como objetivo automatizar a busca de sites oficiais de empresas a partir de um arquivo CSV 📄 contendo seus nomes. Utilizando a biblioteca do Google para pesquisa 🔎 e o poder do pandas 🐼 para manipulação de dados, o programa adiciona ao CSV original uma nova coluna com os respectivos sites encontrados 🌐.

---

## 🚀 Tecnologias Utilizadas

- **Python** 🐍  
- **Pandas** para manipulação de dados  
- **Google Search API** ou biblioteca de scraping (como `googlesearch-python`) 🔎  
- **Poetry** para gerenciamento de dependências 📦  
- **Pytest** para testes unitários ✅

---

## 📁 Estrutura do Projeto

```
📦 empresas_site/
 ┣ 📂 dados/
 ┃ ┣ 📄 empresas_site.csv
 ┃ ┗ 📄 teste.csv
 ┣ 📂 tests/
 ┃ ┣ 📄 test_data_frame_empresas_site.py 🐍
 ┃ ┗ 📄 test_google_search.py 🐍
 ┣ 📄 data_frame_empresas_site.py 🐍
 ┣ 📄 empresas_sites.py 🐍
 ┣ 📄 google_search.py 🐍
 ┣ 📄 poetry.lock
 ┣ 📄 pyproject.toml
 ┗ 📄 README.md
```

---

## ⚙️ Como Usar

1. **Clone o repositório**  
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
   ```

2. **Instale as dependências com Poetry**  
   ```bash
   poetry install
   ```

3. **Execute o programa**  
   ```bash
   poetry run python empresas_sites.py 🐍
   ```

   O script irá:
   - Ler o arquivo `empresas_site.csv` 📄
   - Criar um DataFrame com os nomes das empresas
   - Buscar os sites correspondentes
   - Atualiza o DataFrame com uma nova coluna `site` 🌐

---

## 🧪 Testes

Para rodar os testes e garantir a qualidade do código:

```bash
poetry run pytest
```

---

## 📌 Observações

- É necessário acesso à internet para que as buscas funcionem corretamente 🌐.
- Verifique se o uso da API ou scraping está em conformidade com os termos de uso do Google.

---

## 🧠 Contribuição

Sinta-se à vontade para abrir *issues*, enviar *pull requests* ou sugerir melhorias! 💡

---

## 📄 Licença

Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

---

Se quiser personalizar com o nome real do seu repositório, usuário ou estrutura exata, posso ajustar!