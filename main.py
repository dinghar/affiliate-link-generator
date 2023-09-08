from fastapi import FastAPI
from models import AffiliateLinkRequest
from affiliate_link_generator import generate_affiliate_link

app = FastAPI()

@app.get("/")
def read_root():
    return {"msg": "Hello World"}

@app.post("/generate")
def generate(request: AffiliateLinkRequest):
    x = generate_affiliate_link(request)
    return {"affiliate_link": x}
