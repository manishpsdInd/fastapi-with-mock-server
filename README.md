# fastapi-with-mock-server

### FastAPI with mock server for GenAI practice in a restricted (office) or non-admin environment

Summary of the working architecture to bypass the enterprise restrictions.


#### The Working Architecture
>> Java Code (Spring AI) ➔ HTTP Request (Ollama Format) ➔ Local Python Script (FastAPI) ➔ Mock JSON Payload Response


Instead of using non-accessed and blocked urls or files, this example routes network data locally using standard data exchange structures:

#### server path [mock_server.py](src/main/java/ai/support/server/mock_server.py) [plain text response]

#### server path [mock_server.py][mock_server_json.py](src/main/java/ai/support/server/mock_server_json.py) [json response]


### Steps:
#### 1. Need python and Java both
#### 2. install FastAPI library in python (better to create a .venv then install library into it)
#### 3. run the server using [mock server](src/main/java/ai/support/server/mock_server_json.py) and check response in [localhost](http://localhost:8000) it should be
~~~json
{
  "detail":"Not Found"
}
~~~
#### Start java application access swagger in [8080](http://localhost:8080/swagger-ui/index.html)
#### Sample Mocker Json Reponse:
~~~json
{
    "category": "Network & Access",
    "priority": "HIGH",
    "summary": "User session is blocked by an enterprise Mimecast proxy rule."
}
~~~
#### 5.2. [Swagger response in json]((src/main/resources/output/Output-Screenshot-json.png))
