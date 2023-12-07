from openai import OpenAI

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
import os
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

load_dotenv()
app = FastAPI()

# Set up OpenAI API credentials

# Define our Pydantic model for the request.
class TranslationRequest(BaseModel):
    language: str
    text: str
    context: str = None

# Define our translation route.
@app.post('/translate')
def translate(request: TranslationRequest):
    # Build our prompt, step by step. If the request includes a context,
    # 
    prompt = f'Translate the text below into {request.language}.\n'
    if request.context:
        prompt = f'Given a context, translate the text below into {request.language}.\n\nContext: {request.context}.\n\n'
    prompt += f'Text: "{request.text}"'

    response = client.chat.completions.create(model='gpt-3.5-turbo',
    messages=[
        {
            'role': 'user', 
            'content': prompt,
        }
    ])

    return {'translation': response.choices[0].message.content}
