# summarize.py

import boto3
import json

client = boto3.client("bedrock-runtime", region_name="us-east-1")

def summarize_text_claude(prompt, model_id="anthropic.claude-3-haiku-20240307-v1:0"):
    body = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 500,
        "messages": [
            {
                "role": "user",
                "content": [{"type": "text", "text": prompt}]
            }
        ]
    }

    response = client.invoke_model(
        modelId=model_id,
        contentType="application/json",
        accept="application/json",
        body=json.dumps(body)
    )

    output = json.loads(response["body"].read())
    return output["content"][0]["text"]