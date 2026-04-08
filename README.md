# 🚀 AutoDevOps AI

### Multi-Agent DevOps Assistant using LangGraph + Streamlit (100% Free Stack)

---

## 📌 Overview

**AutoDevOps AI** is a GenAI-powered DevOps assistant that simulates a real-world **SRE/DevOps team** using **multi-agent workflows**.

It can:

* Analyze error logs
* Suggest fixes
* Generate infrastructure code (Docker, Terraform)
* Learn from past issues using FAISS memory

Built entirely using **free tools**, this project demonstrates **real-world AI system design, debugging intelligence, and cloud engineering workflows**.

---

## 🧠 Features

### 🔍 Log Analysis Agent

* Identifies root cause
* Classifies severity
* Detects issue category

### 🔧 Fix Generation Agent

* Suggests step-by-step fixes
* Provides commands and debugging tips

### ☁️ Infrastructure Agent

* Generates:

  * Dockerfile
  * Terraform scripts

### 🧠 FAISS Memory (Long-Term Learning)

* Stores previous issues and fixes
* Retrieves similar problems
* Improves response quality over time

### 🔄 LangGraph Workflow

* Multi-agent pipeline
* Stateful data flow between agents

### 🖥️ Streamlit UI

* Simple interface for testing
* Displays analysis, fixes, and infra code

---

## 🏗️ Architecture

```bash
User Input (Streamlit)
        ↓
LangGraph Workflow
        ↓
 ┌───────────────┐
 │ Log Agent     │
 └──────┬────────┘
        ↓
 ┌───────────────┐
 │ Fix Agent     │
 └──────┬────────┘
        ↓
 ┌───────────────┐
 │ Infra Agent   │
 └───────────────┘
        ↓
 FAISS Memory (store & retrieve)
```

---

## ⚙️ Tech Stack (100% Free)

| Component  | Tool Used               |
| ---------- | ----------------------- |
| Frontend   | Streamlit               |
| LLM        | Groq (LLaMA 3.1 models) |
| Agents     | LangGraph + LangChain   |
| Memory     | FAISS                   |
| Embeddings | Sentence Transformers   |
| Language   | Python                  |

---

## 📁 Project Structure

```bash
autodevops-ai/
│
├── app.py
├── requirements.txt
├── .env
│
├── agents/
├── graph/
├── memory/
├── vectorstore/
├── utils/
```

---

## 🚀 Getting Started

### 1️⃣ Clone the repository

```bash
git clone <your-repo-link>
cd autodevops-ai
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Add environment variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

👉 Get free API key from: https://console.groq.com

---

### 4️⃣ Run the app

```bash
streamlit run app.py
```

---

## 🧪 Example Inputs

### 🔹 Debugging

```
Error: Address already in use
```

### 🔹 Deployment

```
Deploy a Node.js app using Docker and Terraform
```

---

## 📸 Output

* Root cause analysis
* Fix suggestions
* Command-line solutions
* Dockerfile & Terraform code

---

## 🏆 Key Highlights

* ✅ Multi-agent AI system (LangGraph)
* ✅ Stateful workflows with memory
* ✅ Real-world DevOps use case
* ✅ Fully free tech stack
* ✅ Production-inspired architecture

---

## 🔮 Future Enhancements

* RAG with DevOps documentation
* GitHub auto-fix PR generation
* Real-time log monitoring
* Cloud deployment integration (AWS/GCP)
* Agent visualization dashboard

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork this repo and submit a PR.

---

## 📜 License

MIT License

---

## 👨‍💻 Author

Built by **Sanjeeviram**
Aspiring Cloud & DevOps Engineer 🚀
