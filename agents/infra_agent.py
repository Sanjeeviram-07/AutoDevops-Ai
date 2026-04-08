from utils.llm import get_llm

def infra_agent(state):
    llm = get_llm()

    prompt = f"""
    Task:
    {state['input']}

    Generate Docker + Terraform
    """

    response = llm.invoke(prompt)

    return {
        "input": state["input"],   # ✅ keep input
        "analysis": state.get("analysis", ""),
        "fix": state.get("fix", ""),
        "infra": response.content
    }