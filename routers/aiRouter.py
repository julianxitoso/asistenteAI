from fastapi import APIRouter
from interfaces.chatinterfaces import InputMessage
import os
from openai import OpenAI

router = APIRouter()

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("OPENROUTER_API_KEY"),
)

@router.post("/ai-chat")
def aiChat(data: InputMessage):
    data = data.model_dump()
    user_message = data["message"]

    prompt = "Por favor responde de manera concreta, clara y siempre en castellano."

    try:
        completion = client.chat.completions.create(
            model="meta-llama/llama-3.3-8b-instruct:free",
            messages=[
                {
                    "role": "system",
                    "content": "Eres un asistente inteligente que responde en español (Colombia), de forma clara, "
                    "concisa y siempre manteniendo un tono respetuoso y amigable. Responde de manera precisa a las "
                    "preguntas del usuario, usando un lenguaje sencillo, directo y adaptado al contexto colombiano."
                },
                {
                    "role": "user",
                    "content": f"{prompt} Responde a esta pregunta: {user_message}"
                }
            ]
        )

        respuesta = completion.choices[0].message.content
        print("Respuesta del modelo:", respuesta)
        print("response "+completion.choices[0].message.content)
        return {"reply": respuesta}

    except Exception as e:
        print(f"Error: {e}")
        return {"reply": f"Error al generar respuesta: {str(e)}"}


# endpoint2

@router.post("/ai-chat-v2")
def aiChatV2(data: InputMessage):
    data = data.model_dump()
    user_message = data["message"]

    prompt = "Por favor responde de manera concreta y clara, con un tono amigable y directo."

    try:
        completion = client.chat.completions.create(
            model="google/gemma-3-4b-it:free", 
            messages=[
                {
                    "role": "system",
                    "content": "Eres un asistente que responde de forma concisa, clara y con un tono amigable y profesional."
                },
                {
                    "role": "user",
                    "content": f"{prompt} Responde a esta pregunta: {user_message}"
                }
            ]
        )

        respuesta = completion.choices[0].message.content
        print("Respuesta del modelo v2:", respuesta)
        return {"reply": respuesta}

    except Exception as e:
        print(f"Error: {e}")
        return {"reply": f"Error al generar respuesta: {str(e)}"}