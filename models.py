from pydantic import BaseModel

class AffiliateLinkRequest(BaseModel):
    url: str
