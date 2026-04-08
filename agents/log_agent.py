from utils.llm import get_llm
from memory.memory_manager import retrieve_memory

def log_agent(state):
    llm = get_llm()

    past_context = retrieve_memory(state["input"])

    prompt = f"""
    Past issues:
    {past_context}

    Analyze:
    {state['input']}
    """

    response = llm.invoke(prompt)

    return {
        "input": state["input"],   # ✅ keep input
        "analysis": response.content
    }