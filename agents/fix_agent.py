from utils.llm import get_llm
from memory.memory_manager import save_memory

def fix_agent(state):
    llm = get_llm()

    prompt = f"""
    Analysis:
    {state['analysis']}

    Suggest fixes
    """

    response = llm.invoke(prompt)

    combined = f"Problem: {state['input']}\nFix: {response.content}"
    save_memory(combined)

    return {
        "input": state["input"],   # ✅ keep input
        "analysis": state["analysis"],
        "fix": response.content
    }