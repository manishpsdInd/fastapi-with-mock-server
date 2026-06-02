from fastapi import FastAPI, Request
import uvicorn, time, json

app = FastAPI()

@app.post("/api/chat")
async def mock_ollama_chat(request: Request):
    body = await request.json()

    print("\n================ 📥 INCOMING SPRING AI PAYLOAD ================")

    # Loop through all messages sent by Spring AI to see the architecture
    for msg in body.get("messages", []):
        role = msg.get("role", "unknown").upper()
        content = msg.get("content", "").replace("\n", " ")
        # Print each role cleanly so you can inspect the metadata
        print(f"🔹 [ROLE: {role:<6}] -> {content[:75]}...")
    print("==============================================================")

    # Get the last user message to check for JSON instructions
    user_message = body["messages"][-1]["content"]

    if "json" in user_message.lower() or "format" in user_message.lower():
        structured_data = {
            "category": "Network & Access",
            "priority": "HIGH",
            "summary": "User session is blocked by an enterprise Mimecast proxy rule."
        }
        content_payload = json.dumps(structured_data)
        print("➡️ System matched JSON format requirements. Sending payload.\n")
    else:
        content_payload = f"[MOCK OLLAMA RESPONSE] Received: '{user_message}'"
        print("➡️ Sending raw text fallback payload.\n")

    return {
        "model": "mock-model",
        "created_at": "2026-06-02T14:35:00Z",
        "message": {
            "role": "assistant",
            "content": content_payload
        },
        "done": True
    }

if __name__ == "__main__":
    print("🚀 Inspecting Mock Server running on http://127.0.0.1:8000")
    uvicorn.run(app, host="127.0.0.1", port=8000)
