# embedder.py

import boto3
import json

client = boto3.client("bedrock-runtime", region_name="us-east-1")

def embed_text_titan(texts, model_id="amazon.titan-embed-g1-text-02"):
    if isinstance(texts, str):
        texts = [texts]

    embeddings = []

    for text in texts:
        body = {
            "inputText": text
        }

        response = client.invoke_model(
            modelId=model_id,
            contentType="application/json",
            accept="application/json",
            body=json.dumps(body)
        )

        response_body = json.loads(response["body"].read())
        embeddings.append(response_body["embedding"])

    return embeddings
