# YouTube and TikTok Downloader

Este é um projeto simples de um aplicativo para baixar vídeos do YouTube e TikTok. Apesar de ser um projeto pequeno, utilizei uma estrutura mais elaborada para treinar boas práticas de desenvolvimento, modularização de código e organização em projetos reais.

## **Funcionalidades**

- Baixar vídeos do YouTube em diferentes formatos (MP4, MP3).
- Suporte para escolha de qualidade de download (Melhor Qualidade, Apenas Áudio, Qualidade Baixa).
- Integração para download de vídeos do TikTok sem marca d'água (futuro).

---

## **Tecnologias Utilizadas**

### **Backend**

- **[FastAPI](https://fastapi.tiangolo.com/):** Para criar uma API rápida e eficiente.
- **[yt-dlp](https://github.com/yt-dlp/yt-dlp):** Biblioteca para download de vídeos do YouTube e TikTok.
- **Render:** Plataforma gratuita para hospedar o backend.

### **Frontend**

- **[React](https://reactjs.org/):** Biblioteca JavaScript para criar interfaces de usuário.
- **[Tailwind CSS](https://tailwindcss.com/):** Para estilizações rápidas e modernas.
- **Vercel/Netlify:** Plataformas gratuitas para hospedar o frontend.

---

## **Estrutura do Projeto**

### **Backend**

```plaintext
backend/
├── app/
│   ├── __init__.py          # Torna o diretório um pacote Python.
│   ├── main.py              # Ponto de entrada principal do FastAPI.
│   ├── routes/
│   │   ├── __init__.py      # Torna o diretório "routes" um pacote Python.
│   │   ├── download.py      # Define as rotas para download de vídeos.
│   ├── services/
│   │   ├── __init__.py      # Torna o diretório "services" um pacote Python.
│   │   ├── downloader.py    # Contém a lógica para baixar vídeos.
├── requirements.txt         # Dependências para rodar o backend.
├── README.md                # Documentação do backend.
├── .gitignore               # Arquivos/diretórios ignorados pelo Git.
```

**Arquivos Importantes:**

- **`main.py`**: Configuração principal do FastAPI e inclusão de rotas.
- **`routes/download.py`**: Define os endpoints para processar requisições de download.
- **`services/downloader.py`**: Contém a lógica para baixar vídeos utilizando `yt-dlp`.
- **`requirements.txt`**: Dependências necessárias para rodar o backend.

### **Frontend**

```plaintext
frontend/
├── public/
│   ├── index.html          # HTML principal que carrega o React.
├── src/
│   ├── index.js            # Ponto de entrada do React.
│   ├── App.jsx             # Componente principal do aplicativo.
│   ├── components/
│   │   ├── DownloadForm.jsx # Formulário para entrada de dados do usuário.
│   │   ├── Feedback.jsx     # Mensagens de sucesso ou erro.
│   ├── styles.css          # Estilizações globais usando Tailwind.
├── package.json            # Gerenciador de dependências do frontend.
├── README.md               # Documentação do frontend.
├── .gitignore              # Arquivos/diretórios ignorados pelo Git.
```

**Arquivos Importantes:**

- **`App.jsx`**: Coordena os componentes e lógica principal do frontend.
- **`components/DownloadForm.jsx`**: Renderiza o formulário para entrada do usuário.
- **`styles.css`**: Contém os estilos globais e configurações do Tailwind.
- **`package.json`**: Gerenciador de dependências do frontend.

---

## **Como Rodar o Projeto Localmente**

### **Backend**

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/seu-projeto.git
   cd backend
   ```

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. Rode o servidor localmente:

   ```bash
   uvicorn app.main:app --reload
   ```

4. Acesse a API em: [http://127.0.0.1:8000](http://127.0.0.1:8000).

### **Frontend**

1. Navegue até a pasta do frontend:

   ```bash
   cd frontend
   ```

2. Instale as dependências:

   ```bash
   npm install
   ```

3. Rode o servidor localmente:

   ```bash
   npm start
   ```

4. Acesse o frontend em: [http://localhost:3000](http://localhost:3000).

---

## **Hospedagem**

### **Backend (Render)**

1. Suba o repositório para o GitHub/GitLab.
2. Configure um novo **Web Service** no [Render](https://render.com/).
3. Adicione o comando de inicialização:
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```
4. Render fornecerá uma URL para o backend.

### **Frontend (Vercel ou Netlify)**

1. Suba o repositório do frontend para o GitHub.
2. Configure o projeto no [Vercel](https://vercel.com/) ou [Netlify](https://netlify.com/).
3. No Vercel, o comando de build será detectado automaticamente (`npm run build`).
4. A URL final será algo como `https://seu-projeto.vercel.app`.

---

## **Motivação do Projeto**

Este projeto foi desenvolvido com uma estrutura mais elaborada propositalmente para treinar:

- **Boas práticas de organização** em backend e frontend.
- Modularização e reutilização de código.
- **Integração de tecnologias** como FastAPI e React.
- Publicação de aplicações em plataformas gratuitas como Render e Vercel.

---

## **Próximos Passos**

- Implementar suporte para downloads de vídeos do TikTok sem marca d'água.
- Adicionar testes automatizados para garantir a qualidade do código.
- Melhorar o design do frontend com mais animações e responsividade.

---

**Autor:** Vinitziin
