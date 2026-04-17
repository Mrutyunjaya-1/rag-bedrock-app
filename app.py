import streamlit as st
from rag_backend import get_answer

st.set_page_config(page_title="RAG System", layout="wide")

st.title("📚 Enterprise Knowledge Base Q&A")

query = st.text_input("Ask a question from your documents:")

if st.button("Get Answer"):

    if not query.strip():
        st.warning("Please enter a question")
    else:
        with st.spinner("Thinking..."):
            answer, sources = get_answer(query)

        st.subheader("🧠 Answer")
        st.write(answer)

        st.subheader("📄 Sources")
        for i, src in enumerate(sources):
            st.write(f"{i+1}. {src}")