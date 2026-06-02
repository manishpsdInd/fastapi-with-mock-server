# fastapi-with-mock-server

### FastAPI with mock server for GenAI practice in a restricted (office) or non-admin environment

Summary of the working architecture to bypass the enterprise restrictions.


#### The Working Architecture
>> Java Code (Spring AI) ➔ HTTP Request (Ollama Format) ➔ Local Python Script (FastAPI) ➔ Mock JSON Payload Response


Instead of using non-accessed and blocked urls or files, this example routes network data locally using standard data exchange structures:

#### server path [mock_server.py](src/main/java/ai/server/mock_server.py)

    	


