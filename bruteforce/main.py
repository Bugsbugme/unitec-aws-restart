from fastapi import FastAPI, HTTPException

# app = FastAPI(docs_url="/")
app = FastAPI(docs_url="/")


@app.get("/login/{password}")
def login(password):
    if password == "superman":
        return "Login Successful."
    else:
        raise HTTPException(status_code=403, detail="Incorrect Password.")


@app.post("/test")
def testingpost(username):
    return f"Your username is: {username}"
