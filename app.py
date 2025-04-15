import os
from ingest import extract_text_from_pdf
from summarize import summarize_text_claude
from utils import split_text_into_chunks
from embedder import embed_text_titan
from qa import answer_question

if __name__ == "__main__":
    file_path = "input_docs/sample.pdf"
    file_name = os.path.basename(file_path).replace(".pdf", "")
    output_path = f"output/summary_{file_name}.txt"

    print(f"\n📄 Reading PDF: {file_path}")
    content = extract_text_from_pdf(file_path)
    chunks = split_text_into_chunks(content)

    all_summaries = []

    for i, chunk in enumerate(chunks, 1):
        print(f"\n🔹 Summarizing chunk {i}/{len(chunks)}...")
        summary = summarize_text_claude(f"Summarize this:\n\n{chunk}")
        all_summaries.append(summary)

    full_summary = "\n".join([f"\n--- Chunk {i+1} ---\n{summary}" for i, summary in enumerate(all_summaries)])

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(full_summary)

    print(f"\n✅ Saved summary to: {output_path}")

    # ✅ Embedding & Q&A section
    print("\n🔗 Embedding all summary chunks...")
    embeddings = embed_text_titan(all_summaries)

    query = input("\n💬 Ask a question about the document:\n> ")
    answer = answer_question(query, all_summaries, embeddings)

    print("\n🤖 Answer:\n", answer)
