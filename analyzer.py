import os
import json

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

from models import SocialMediaAnalysis

load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.1-8b-instant"
)

template = """
Analyze the following social media post.

Return ONLY valid JSON in this format:

{{
    "tone": "",
    "intent": "",
    "communication_style": "",
    "summary": ""
}}

Post:
{post}
"""

prompt = PromptTemplate(
    input_variables=["post"],
    template=template
)

def analyze_post(post):

    chain = prompt | llm

    response = chain.invoke({
        "post": post
    })

    result = response.content

    result = (
        result.replace("```json", "")
              .replace("```", "")
              .strip()
    )

    output = json.loads(result)

    validated = SocialMediaAnalysis(**output)

    return validated.model_dump()