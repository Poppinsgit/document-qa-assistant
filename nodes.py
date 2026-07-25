from state import AgentState

from retriever import get_relevant_chunks
from llm import ask_llm



def retrieve_node(state: AgentState):

    documents, sources = get_relevant_chunks(
        state["question"]
    )

    return {
        "question": state["question"],
        "context": documents,
        "sources": sources,
        "answer": ""
    }



def generate_node(state: AgentState):

    context = state["context"]   

    answer = ask_llm(
        state["question"],
        context
    )

    return {
        "question": state["question"],
        "context": context,
        "sources": state["sources"],
        "answer": answer
    }
