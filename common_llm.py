import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("GROQ_API_KEY not found in environment variables.")

client = Groq(api_key=groq_api_key)

def llm_call(prompt: str, model: str = "llama3-70b-8192", temperature: float = 0.7, system_prompt: str = "") -> str:
    """
    Sends a prompt to the GROQ model and returns the response.
    """
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})

    try:
        response = client.chat.completions.create(
            messages=messages,
            model=model,
            temperature=temperature,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Error in LLM response: {str(e)}"
