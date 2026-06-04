# HR Manual Chatbot - Malaysia Labor Law

An intelligent chatbot application to answer HR manual and Malaysia labor law queries using document embeddings and AI.

## Features

- 📄 Document upload and processing (PDF, TXT, DOCX)
- 🤖 AI-powered responses based on Malaysia labor law documents
- 🔍 Semantic search with vector embeddings
- 💬 Web interface for easy interaction
- ⚡ Fast response times with caching
- 🔐 Secure document handling

## Architecture

- **Backend**: Python (Flask) + LangChain
- **Frontend**: Node.js/React web application
- **Database**: Vector database (Pinecone) + SQLite/PostgreSQL
- **LLM**: OpenAI GPT or local LLM

## Quick Start

### Prerequisites
- Python 3.9+
- Node.js 16+
- OpenAI API key (or local LLM)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/m365-test01-ql/hr-manual-chatbot.git
cd hr-manual-chatbot
```

2. **Backend Setup**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. **Frontend Setup**
```bash
cd frontend
npm install
```

4. **Environment Configuration**
Create `.env` files in both backend and frontend directories

5. **Run the Application**

Backend:
```bash
cd backend
python app.py
```

Frontend:
```bash
cd frontend
npm start
```

## Project Structure

```
hr-manual-chatbot/
├── backend/              # Python Flask backend
├── frontend/             # React web application
├── docker-compose.yml
├── .gitignore
└── README.md
```

## License

MIT License
