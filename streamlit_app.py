import streamlit as st
import os
from ingest import extract_text_from_pdf
from summarize import summarize_text_claude
from utils import split_text_into_chunks
from embedder import embed_text_titan
from qa import answer_question
import tempfile
from cache_utils import hash_file, save_summary, load_summary, save_embeddings, load_embeddings

st.set_page_config(page_title="AI Investment Memo Analyzer", layout="wide")
st.title("📄 AI-Powered Investment Memo Analyzer")

uploaded_file = st.file_uploader("Upload a PDF document", type=["pdf"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    hash_id = hash_file(tmp_path)

    # Try loading summary from cache
    cached_summary = load_summary(hash_id)
    cached_embed = load_embeddings(hash_id)

    if cached_summary and cached_embed:
        st.success("✅ Loaded from cache")
        all_summaries = cached_summary
        embeddings = cached_embed

    else:
        st.info("Extracting and summarizing content with Claude 3 Haiku...")
        content = extract_text_from_pdf(tmp_path)
        chunks = split_text_into_chunks(content)

        all_summaries = []
        progress = st.progress(0)
        for i, chunk in enumerate(chunks, 1):
            summary = summarize_text_claude(f"Summarize this: \n{chunk}")
            all_summaries.append(summary)
            progress.progress(i / len(chunks))
        os.makedirs("output", exist_ok=True)
        output_file = f"output/summary_{hash_id}.txt"
        with open(output_file, "w", encoding="utf-8") as f:
            for i, summary in enumerate(all_summaries, 1):
                f.write(f"--- Chunk {i} ---\n{summary}\n\n")
        save_summary(hash_id, all_summaries)

        with st.spinner("Embedding chunks with Titan Embeddings..."):
            embeddings = embed_text_titan(all_summaries)

        save_embeddings(hash_id, embeddings)

    st.success("✅ Embeddings Ready for Q&A")
    st.subheader("💬 Ask a question about this document")
    user_query = st.text_input("Enter your question:")

    if user_query:
        with st.spinner("Thinking with Claude..."):
            answer, matched_chunk, matched_index = answer_question(user_query, all_summaries, embeddings)

        st.markdown(f"### 🤖 Claude's Answer:\n{answer}")
        with st.expander("🔍 Show source chunk used for this answer"):
            st.markdown(f"**Chunk {matched_index + 1}:**")
            st.write(matched_chunk)
