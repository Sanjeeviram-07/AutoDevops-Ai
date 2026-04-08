def supervisor(state):
    user_input = state["input"].lower()

    if "deploy" in user_input or "docker" in user_input:
        return "infra_agent"
    else:
        return "log_agent"