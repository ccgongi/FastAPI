from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Dare is thgggge GOAT! jkjk"}
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
