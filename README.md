# 🚀 Enterprise Knowledge Base Q&A System (RAG with AWS Bedrock)

🌐 **Live Demo:**
https://rag-bedrock-app-dspm6ysxt2jhtpdfuyanh6.streamlit.app/

---

## 📌 Overview

This project implements a **Retrieval-Augmented Generation (RAG)** system that allows users to ask natural language questions on enterprise documents and receive accurate, context-aware answers with source references.

It simulates real-world enterprise AI systems such as:

* Internal knowledge assistants
* HR policy chatbots
* Support automation tools

---

## 🧠 How It Works

1. **User Query**

   * User asks a question via Streamlit UI

2. **Semantic Retrieval**

   * AWS Bedrock Knowledge Base retrieves relevant document chunks

3. **Context Building**

   * Top relevant results are combined into context

4. **Answer Generation**

   * Amazon Nova Lite model generates a structured answer

5. **Response Output**

   * Answer + source documents displayed

---

## ⚙️ Tech Stack

* **AWS Bedrock**

  * Knowledge Bases (retrieval)
  * Nova Lite (LLM generation)
* **Amazon S3** – Document storage
* **Python (Boto3)** – Backend integration
* **Streamlit** – Interactive UI
* **Streamlit Cloud** – Deployment

---

## ✨ Features

* ✅ Context-aware answers (RAG pipeline)
* ✅ No hallucination (strict context usage)
* ✅ Source-backed responses 📄
* ✅ ChatGPT-style interface 💬
* ✅ Multi-document querying
* ✅ Clean structured output (headings + bullets)
* ✅ Cloud deployed (public access)

---

## 📂 Project Structure

```
rag-bedrock-app/
│
├── app.py              # Streamlit chat UI
├── rag_backend.py      # RAG pipeline (retrieval + generation)
├── requirements.txt    # Dependencies
└── README.md
```

---

## 🚀 Getting Started (Local Setup)

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/rag-bedrock-app.git
cd rag-bedrock-app
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Configure AWS credentials

```bash
aws configure
```

OR use environment variables:

```bash
export AWS_ACCESS_KEY_ID=your_key
export AWS_SECRET_ACCESS_KEY=your_secret
export AWS_DEFAULT_REGION=us-east-1
```

---

### 4. Run the application

```bash
streamlit run app.py
```

---

## 🔐 Deployment

This application is deployed on **Streamlit Cloud**.

### Steps:

1. Push code to GitHub
2. Connect repository to Streamlit Cloud
3. Add AWS credentials in **Secrets**
4. Deploy

---

## 🧪 Example Queries

Try these in the app:

* What is company policy?
* What are HR guidelines?
* Summarize all documents
* What support services are available?
* What is CEO salary? (tests hallucination handling)

---

## 🧠 Key Learnings

* Building end-to-end RAG pipelines
* Working with AWS Bedrock APIs
* Prompt engineering for structured responses
* Handling IAM roles & permissions
* Debugging real-world cloud deployment issues
* Optimizing retrieval and response quality

---

## 🔮 Future Improvements

* 🔹 Conversation memory
* 🔹 File upload support
* 🔹 Improved document ranking
* 🔹 Authentication system
* 🔹 Streaming responses
* 🔹 Analytics dashboard

---

## 💼 Resume Highlight

> Built and deployed an enterprise-grade RAG system using AWS Bedrock, enabling context-aware question answering over internal documents with source attribution.

---

## 🤝 Contributing

Contributions are welcome!
Feel free to open issues or submit pull requests.

---

## 📬 Contact

* GitHub: https://github.com/YOUR_USERNAME
* LinkedIn: https://linkedin.com/in/YOUR_PROFILE

---

⭐ If you found this project useful, consider giving it a star!
