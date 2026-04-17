import boto3
import json

# ---------------- CONFIG ----------------
REGION = "us-east-1"
KNOWLEDGE_BASE_ID = "BRUJBHZIUK"

# ---------------- CLIENTS ----------------
bedrock_runtime = boto3.client(
    "bedrock-runtime",
    region_name=REGION
)

bedrock_agent = boto3.client(
    "bedrock-agent-runtime",
    region_name=REGION
)


def retrieve_docs(query):
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

    for r in response["retrievalResults"]:
        docs.append(r["content"]["text"])

        src = r.get("location", {}).get("s3Location", {}).get("uri", "Unknown")
        sources.append(src)

    return docs, sources

def generate_answer(query, docs):
    context = "\n\n".join(docs)

    prompt = f"""
You are a professional enterprise assistant.

Give structured answers with:
- Headings
- Bullet points
- Clear formatting

Use ONLY the context.
If not found, say "I don't know".

Context:
{context}

Question:
{query}
"""

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

# ---------------- MAIN ----------------
def get_answer(query):
    docs, sources = retrieve_docs(query)

    if not docs:
        return "No relevant data found.", []

    sources = list(set([s.split("/")[-1] for s in sources]))

    answer = generate_answer(query, docs)

    return answer, sources
