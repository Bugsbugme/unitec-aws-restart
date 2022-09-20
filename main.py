# Run "uvicorn main:app --reload" in the console
import fastapi

app = fastapi.FastAPI()


@app.get("/")
def hello():
    return "hello"


@app.get("/tournaments")
def list_tournaments():
    return [1, 2, 3]


@app.get("/stats")
def stats():
    return {"mvp": "Jordan", "points": 9001}
