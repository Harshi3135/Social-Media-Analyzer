from pydantic import BaseModel

class SocialMediaAnalysis(BaseModel):
    tone: str
    intent: str
    communication_style: str
    summary: str