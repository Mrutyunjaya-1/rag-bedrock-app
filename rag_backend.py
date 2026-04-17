import boto3
import json

# ---------------- CONFIG ----------------
REGION = "us-east-1"
KNOWLEDGE_BASE_ID = "BRUJBHZIUK"  # replace if needed

# ---------------- CLIENTS ----------------
bedrock_runtime = boto3.client(
    "bedrock-runtime",
    region_name=REGION
)

bedrock_agent = boto3.client(
    "bedrock-agent-runtime",
    region_name=REGION
)

# ---------------- RETRIEVE ----------------
def retrieve_docs(query):
    try:
        response = bedrock_agent.retrieve(
            knowledgeBaseId=KNOWLEDGE_BASE_ID,
            retrievalQuery={"text": query},
            retrievalConfiguration={
                "vectorSearchConfiguration": {
                    "numberOfResults": 5
                }
            }
        )

        docs = []
        sources = []

        for r in response.get("retrievalResults", []):
            docs.append(r["content"]["text"])

            src = r.get("location", {}).get("s3Location", {}).get("uri", "Unknown")
            sources.append(src)

        return docs, sources

    except Exception as e:
        print("❌ Retrieval Error:", e)
        return [], []

# ---------------- GENERATE ----------------
def generate_answer(query, docs):
    if not docs:
        return "I don't know based on the provided documents."

    # Limit context to avoid high cost & latency
    context = "\n\n".join(docs[:3])

    prompt = f"""
You are a professional enterprise knowledge assistant.

Your task is to answer the user's question using ONLY the provided context.

### Instructions:
- Provide a clear, structured, and professional answer
- Use headings and bullet points where appropriate
- Be concise but informative
- Do NOT make up information
- If the answer is not present in the context, respond with: "I don't know based on the provided documents"

### Context:
{context}

### Question:
{query}

### Answer:
"""

    try:
        response = bedrock_runtime.converse(
            modelId="amazon.nova-lite-v1:0",
            messages=[
                {
                    "role": "user",
                    "content": [{"text": prompt}]
                }
            ]
        )

        return response["output"]["message"]["content"][0]["text"]

    except Exception as e:
        print("❌ Generation Error:", e)
        return "Error generating response. Please try again."

# ---------------- MAIN ----------------
def get_answer(query):
    docs, sources = retrieve_docs(query)

    if not docs:
        return "I don't know based on the provided documents.", []

    # Clean source names
    sources = list(set([s.split("/")[-1] for s in sources]))

    answer = generate_answer(query, docs)

    return answer, sources
