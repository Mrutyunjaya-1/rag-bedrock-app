import streamlit as st
from rag_backend import get_answer

st.set_page_config(page_title="Enterprise RAG Assistant", layout="wide")

st.title("🤖 Enterprise Knowledge Assistant")

# ---------------- SESSION STATE ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.header("⚙️ Controls")

    if st.button("🧹 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")
    st.markdown("**Built with AWS Bedrock + RAG** 🚀")

# ---------------- CHAT DISPLAY ----------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------------- USER INPUT ----------------
query = st.chat_input("Ask something about your documents...")

if query:
    # Store user message
    st.session_state.messages.append({"role": "user", "content": query})

    with st.chat_message("user"):
        st.markdown(query)

    # Generate answer
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            answer, sources = get_answer(query)

            st.markdown(answer)

            if sources:
                st.markdown("**📄 Sources:**")
                for s in sources:
                    st.markdown(f"- {s}")

    # Store assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer + "\n\nSources:\n" + "\n".join(sources)
    })
