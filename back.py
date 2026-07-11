from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Hello from my backend!"
    }

@app.get("/about")
def about():
    return {
        "name": "Kim",
        "course": "Backend AI Engineering"
    }
