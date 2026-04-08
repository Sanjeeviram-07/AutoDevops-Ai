from langgraph.graph import StateGraph
from agents.supervisor import supervisor
from agents.log_agent import log_agent
from agents.fix_agent import fix_agent
from agents.infra_agent import infra_agent

def build_graph():

    graph = StateGraph(dict)

    graph.add_node("log_agent", log_agent)
    graph.add_node("fix_agent", fix_agent)
    graph.add_node("infra_agent", infra_agent)

    graph.set_entry_point("log_agent")

    graph.add_edge("log_agent", "fix_agent")

    graph.add_conditional_edges(
        "fix_agent",
        lambda state: "infra_agent" if "deploy" in state["input"].lower() else "__end__"
    )

    return graph.compile()