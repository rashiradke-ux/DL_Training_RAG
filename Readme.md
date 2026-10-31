# 🎓 College Knowledge Assistant

A robust, extractive Retrieval-Augmented Generation (RAG) assistant designed to answer college inquiries using official institutional documents. Built purely with Python, Streamlit, and scikit-learn—**no external or paid LLM API required**, preventing hallucinations by design.

---

## 🌟 Key Features

- **Multi-Format Ingestion**: Supports `.txt` and `.pdf` documents with automated text normalization and chunking.
- **Hybrid Retrieval**: Combines word-level TF-IDF (1-2 n-grams), sub-word character n-grams (3-5 chars), and query expansion for precise lexical matching.
- **Source Grounding & Citations**: Every answer provides precise source file name, chunk IDs, and page numbers.
- **Strict Hallucination Prevention**: Rejects unanswerable queries when semantic relevance falls below confidence thresholds.
- **Contradiction Detection**: Detects conflicting information across different policy documents (e.g., competing library hours notices).
- **Interactive Web Interface**: Streamlit UI allows uploading new documents, dynamic index rebuilding, and real-time query answering.

---

## 🚀 Quickstart

### 1. Prerequisites
- Python 3.10+ (tested on Python 3.11, 3.12, and 3.15)
- Git

### 2. Installation
Clone or download the repository:
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

Install the required dependencies:
```bash
python -m pip install -r requirements.txt
```

### 3. Run the Application
Launch the Streamlit web dashboard:
```bash
python -m streamlit run app.py
```
Open your web browser at `http://localhost:8501`.

---

## 🧪 Testing & Verification

Automated test cases covering all mandatory evaluation scenarios are included in `tests/test_rag.py`:

```bash
python -m pytest tests/test_rag.py -v
```

### Mandatory Evaluation Scenarios Covered:
1. **Direct Answer**: Fact clearly stated in one document (*Database-I.txt*).
2. **Multi-Document Synthesis**: Answer requiring information from two distinct documents (*Database-IV.txt* and *Database-V.txt*).
3. **Unanswerable / Out-of-Domain**: Out-of-scope question properly rejected without hallucinating (*FIFA World Cup query*).
4. **Paraphrased Query**: Different wording mapped to exact document facts via query expansion.
5. **Conflicting Documents**: Automatic contradiction detection between differing notices (*Database-II.txt* vs *Database-VI.txt*).
6. **Citation Metadata**: Accurate source, chunk, and page metadata preservation.

### Benchmark Evaluation Script
Run the automated evaluation across all 12 test questions from `test_questions.json`:
```bash
python evaluate.py
```

---

## 🏗️ Architecture

```
User Query
    │
    ▼
[Query Expansion] ── (Adds synonyms/related academic terms)
    │
    ▼
[Hybrid Retrieval Engine]
    ├── Word TF-IDF Matrix (unigram + bigram)
    ├── Char TF-IDF Matrix (3-5 char n-grams)
    └── Token Overlap Scoring
    │
    ▼
[Conflict Detection Heuristics] ── (Flags time/date contradictions)
    │
    ├──> Contradiction Detected? ──> Surface conflicting sources and warn user
    │
    ▼
[Relevance Threshold Filter]
    │
    ├──> Below threshold / no lexical overlap? ──> Abstain safely
    │
    ▼
[Extractive Passage Synthesis & Citations]
    │
    ▼
Streamlit User Interface
```

---

## 🚢 Deployment

The project is pre-configured for multiple deployment methods:

- **Streamlit Community Cloud**: Connect your GitHub repository to [share.streamlit.io](https://share.streamlit.io/) and deploy in one click.
- **Docker**:
  ```bash
  docker build -t college-rag-assistant .
  docker run -p 8501:8501 college-rag-assistant
  ```
- **Docker Compose**:
  ```bash
  docker compose up -d
  ```
- **Render / Railway**: Pre-configured via `render.yaml` and `Procfile`.

For full deployment documentation, see [`DEPLOYMENT.md`](DEPLOYMENT.md).

---

## 📁 Repository Structure

```
├── app.py                     # Main Streamlit web application
├── rag_pipeline.py            # Core RAG retrieval and indexing engine
├── evaluate.py                # Automated evaluation suite
├── requirements.txt           # Production dependencies
├── Dockerfile                 # Container deployment specification
├── docker-compose.yml         # Multi-container orchestration
├── render.yaml                # Render cloud deployment config
├── Procfile                   # Cloud process declaration
├── DEPLOYMENT.md              # Detailed deployment guide
├── .streamlit/
│   └── config.toml            # Streamlit server & theme configuration
├── documents/                 # Default knowledge base documents
│   ├── Database-I.txt
│   ├── Database-II.txt
│   ├── Database-III.txt
│   ├── Database-IV.txt
│   ├── Database-V.txt
│   └── Database-VI.txt
├── test_documents/            # Isolated test document collection
├── tests/
│   └── test_rag.py            # Pytest automated test suite
└── test_questions.json        # Evaluation test question dataset
```

---

## 📄 License
MIT License.
