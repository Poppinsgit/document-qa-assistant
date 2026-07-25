import streamlit as st

from graph import graph


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

        with st.spinner("🤖 Thinking..."):

            result = graph.invoke(
                {
                    "question": question,
                    "context": "",
                    "answer": "",
                    "sources": []
                }
            )


        st.subheader("Answer")

        st.write(
            result["answer"]
        )


        st.subheader("📚 Sources")

        for source in result["sources"]:
            st.write(
                f"📄 {source}"
            )