from fastapi import FastAPI
from pydantic import BaseModel
# ... كود الخادم ...
app = FastAPI()
@app.post('/generate')
async def generate(request: dict):
    return {'response': '...'}
