import fastapi

app = fastapi.FastAPI()


@app.get("/")
def hello():
    return "hello"
