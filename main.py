from fastapi import FastAPI, WebSocket, Query
from fastapi.responses import JSONResponse, FileResponse
from trie import trie

app = FastAPI()

@app.get("/suggest")
async def suggest(input: str = Query(..., min_length=1)):
    suggestions = trie.search_prefix(input)
    return JSONResponse(suggestions)

@app.get("/")
async def read_index():
    return FileResponse('index.html')

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        suggestions = trie.search_prefix(data)
        await websocket.send_json(suggestions)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
