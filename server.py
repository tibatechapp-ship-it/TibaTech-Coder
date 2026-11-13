import os
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI()

# سيقرأ المفتاح من متغيرات البيئة (سنضعه في Codespaces لاحقاً)
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY", "YOUR_KEY_HERE"),
    base_url="https://api.deepseek.com/v1"
)

class ChatRequest(BaseModel):
    prompt: str

@app.post("/generate")
async def generate(request: ChatRequest):
    try:
        response = client.chat.completions.create(
            model="deepseek-coder", # يستخدم أحدث إصدار تلقائياً
            messages=[{"role": "user", "content": request.prompt}],
            temperature=0.2
        )
        return {"response": response.choices[0].message.content}
    except Exception as e:
        return {"error": str(e)}