import openai

import os
openai.api_key = os.getenv("OPENAI_API_KEY")  # ✅ Load from .env


def get_answer(question: str, context: str) -> str:
    prompt = f"Answer the question based on the context below:\n\nContext:\n{context}\n\nQuestion: {question}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=256
    )
    return response.choices[0].message["content"].strip()
