import streamlit as st

from retriever import get_relevant_chunks
from llm import ask_llm


st.set_page_config(
    page_title="Document Q&A Assistant",
    page_icon="📄"
)


st.title("📄 Document Q&A Assistant")
st.write(
    "Upload a PDF and ask questions from the document."
)


uploaded_file = st.file_uploader(
    "Upload your PDF",
    type="pdf"
)


if uploaded_file:

    st.success("PDF uploaded!")

    question = st.text_input(
        "Ask your question:"
    )


    if question:

        print("🔎 Retrieving chunks...")

        context, sources = get_relevant_chunks(
            question
        )

        print("✅ Retrieval done")


        with st.spinner(
            "🤖 Thinking..."
        ):

            answer = ask_llm(
                question,
                context
            )


        st.subheader(
            "Answer"
        )

        st.write(answer)


        st.subheader(
            "📚 Sources"
        )


        for source in sources:
            st.write(
                f"📄 {source}"
            )