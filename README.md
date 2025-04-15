```markdown
# 📄 AI Investment Memo Analyzer with Amazon Bedrock (Claude + Titan)

An interactive Streamlit app that uses **Claude 3 (Haiku)** and **Titan Embeddings** via Amazon Bedrock to analyze PDF investment memos, generate AI summaries, and answer questions with retrieval-augmented generation (RAG).

---

## 🔍 Features

- 📥 Upload a PDF investment memo or report  
- 📄 Summarizes document in chunks using **Claude 3 Haiku**  
- 🔗 Embeds summaries with **Titan Embeddings**  
- 💬 Ask any question about the document — gets accurate answers  
- 🔍 Preview source chunk Claude used  
- 💾 Auto-caches results to save costs  
- 📁 Saves summary in `output/` folder as plain text  

---

## 🧠 Powered By

- 🤖 [Amazon Bedrock](https://aws.amazon.com/bedrock/)  
  - `Claude 3 Haiku` (by Anthropic) for summarization + Q&A  
  - `Titan Embeddings G1` for semantic search  
- 🖥️ Streamlit for the UI  

---

## 📂 Project Structure

```
investment-analyzer/
├── input_docs/         # Optional sample inputs
├── output/             # Saved summary files
├── cache/              # Cached embeddings/summaries
├── streamlit_app.py    # Main Streamlit app
├── summarize.py        # Claude summarization logic
├── embedder.py         # Titan embedding logic
├── ingest.py           # PDF text extraction
├── qa.py               # Q&A via Claude + embeddings
├── utils.py            # Chunking helpers
├── cache_utils.py      # Caching logic
├── requirements.txt    # Python dependencies
└── README.md           # You're reading it 🙂
```

---

## 🚀 How to Run Locally

```bash
git clone https://github.com/ritik294/investment-analyzer.git
cd investment-analyzer
python -m venv venv
source venv/bin/activate        # Or venv\Scripts\activate on Windows
pip install -r requirements.txt
streamlit run streamlit_app.py
```

---

### ⚙️ AWS Setup (.env)

Create a `.env` file in the root directory:

```
AWS_ACCESS_KEY_ID=your-key
AWS_SECRET_ACCESS_KEY=your-secret
AWS_REGION=us-east-1
```

Or use:

```bash
aws configure
```

to set credentials globally.

---

## 🧪 Example Use Cases

- Investment memo or due diligence summarization  
- Q&A on long financial or legal documents  
- Research paper summarization and answering  
- AI-powered brief generation from any PDF  

---

## 🧠 Model Info

- **Claude 3 Haiku (Anthropic)** — Text summarization + Q&A  
- **Titan Embeddings (Amazon)** — Embedding vectors for similarity search  

---

## 📦 Deployment (Optional)

You can deploy this app to [Hugging Face Spaces](https://huggingface.co/spaces) using Streamlit.

Example `app.py` for Spaces:

```python
import os
os.system("streamlit run streamlit_app.py")
```

---

## 🛡️ License

This project is open-source for academic, demo, and research use.  
Please check [AWS Bedrock Terms](https://aws.amazon.com/service-terms/) for commercial deployment.
```


