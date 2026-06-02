from fastapi import FastAPI, Request
import uvicorn
import time

app = FastAPI()

@app.post("/v1/chat/completions")
async def mock_chat(request: Request):
    body = await request.json()
    user_message = body["messages"][-1]["content"]

    print(f" Received from Spring AI: '{user_message}'")

    # Simulate a small processing delay like a real AI
    time.sleep(0.5)

    # Generate a predictable mock response to test your Java logic
    mock_reply = f"[MOCK AI RESPONSE] I received your prompt: '{user_message}'. Your Spring AI configuration is working perfectly !"

    # Return the exact JSON structure Spring AI expects from OpenAI/Ollama
    return {
        "id": "chatcmpl-mock123",
        "object": "chat.completion",
        "created": int(time.time()),
        "model": "mock-model",
        "choices": [{
            "index": 0,
            "message": {
                "role": "assistant",
                "content": mock_reply
            },
            "finish_reason": "stop"
        }]
    }

@app.post("/api/chat")
async def mock_ollama_chat(request: Request):
    body = await request.json()
    user_message = body["messages"][-1]["content"]
    print(f" Received from Spring AI (Ollama Format): '{user_message}'")

    # Return the exact JSON structure the Spring AI Ollama starter expects
    return {
        "model": "mock-model",
        "created_at": "2026-06-02T14:35:00Z",
        "message": {
            "role": "assistant",
            "content": f"[MOCK OLLAMA RESPONSE] I received your prompt: '{user_message}'. Your Spring AI Ollama config is working!"
        },
        "done": True
    }

if __name__ == "__main__":
    print(" Mock AI Server started on http://127.0.0.1:8000")
    print("Point your Spring AI application here to practice.")
    uvicorn.run(app, host="127.0.0.1", port=8000)
