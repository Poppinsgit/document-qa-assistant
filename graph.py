from langgraph.graph import StateGraph, START, END

from state import AgentState
from nodes import retrieve_node, generate_node


builder = StateGraph(AgentState)

# Add nodes
builder.add_node("retrieve", retrieve_node)
builder.add_node("generate", generate_node)

# Connect nodes
builder.add_edge(START, "retrieve")
builder.add_edge("retrieve", "generate")
builder.add_edge("generate", END)

# Compile graph
graph = builder.compile()