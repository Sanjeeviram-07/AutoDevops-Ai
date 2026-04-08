import streamlit as st
from graph.workflow import build_graph

st.set_page_config(page_title="AutoDevOps AI", layout="wide")

st.title("🚀 AutoDevOps AI")
st.write("AI DevOps Assistant using LangGraph + Agents")

user_input = st.text_area("Enter error / task:")

if st.button("Run AI System"):

    if user_input:
        graph = build_graph()

        result = graph.invoke({
            "input": user_input
        })

        st.subheader("🧠 Analysis")
        st.write(result.get("analysis", "No analysis"))

        st.subheader("🔧 Fix Suggestions")
        st.write(result.get("fix", "No fix"))

        st.subheader("☁️ Infra Code")
        st.write(result.get("infra", "No infra generated"))
        
        st.subheader("🧠 Memory Used")
st.write("System recalls similar past issues automatically!")