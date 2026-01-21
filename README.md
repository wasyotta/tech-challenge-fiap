# 📚 Books Public API – Tech Challenge FIAP

API pública desenvolvida em **Python + FastAPI** como parte do **Tech Challenge da FIAP**.  
A aplicação expõe endpoints para consulta de livros, categorias e estatísticas, utilizando um dataset extraído do site **books.toscrape.com**.

---

### 🧱 Pipeline e Arquitetura

- API REST construída com **FastAPI**
- Arquitetura organizada em **camadas (routes, services, repositories)**
- Dataset local em CSV
- Deploy automatizado na plataforma **Render**
- Documentação automática via **Swagger**

---

### 🛠️ Tecnologias

- Python
- FastAPI
- Uvicorn
- Pandas
- BeautifulSoup
- Requests
- Render

---

### 📂 Estrutura do Projeto

api/
├── main.py
├── routes/
│ ├── books.py
│ ├── categories.py
│ ├── health.py
│ └── stats.py
├── services/
│ ├── books_service.py
│ └── stats_service.py
├── repositories/
│ └── init.py
data/
└── books.csv
scripts/
└── scrape_books.py
requirements.txt
start.sh
README.md


---

### 🚀 Execução Local

### 1️⃣ Criar ambiente virtual (opcional, mas recomendado)

```bash
python -m venv .venv
source .venv/bin/activate  # Linux / Mac
.venv\Scripts\activate     # Windows
```
### 2️⃣ Instalar dependências
```bash
pip install -r requirements.txt
```
### 3️⃣ Executar a aplicação
```bash
uvicorn api.main:app --reload
```
---

### 🌐 Acesso à API

URL local:
http://127.0.0.1:8000

Swagger (documentação interativa):
http://127.0.0.1:8000/docs

---
### 📌 Endpoints Principais
🔹 Health Check
GET /api/v1/health

🔹 Listar livros
GET /api/v1/books

🔹 Listar categorias
GET /api/v1/categories

🔹 Estatísticas
GET /api/v1/stats

---
### ☁️ Deploy
A aplicação está publicada na plataforma Render.

---
### 🔗 URL pública:
https://tech-challenge-fiap-896p.onrender.com

---
### 📘 Swagger em produção:
https://tech-challenge-fiap-896p.onrender.com/docs

---
### 👨‍💻 Autor

Projeto desenvolvido para o Tech Challenge – FIAP
por Wilson Alves Silva
---
### ✅ Status do Projeto

✔️ Funcional
✔️ Documentado
✔️ Deploy realizado
✔️ Pronto para avaliação
---