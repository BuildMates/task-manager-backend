from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Task Manager Backend is running"}


@app.get("/tasks")
def get_tasks():
    return [
        {"id": 1, "title": "Learn FastAPI", "completed": False},
        {"id": 2, "title": "Build task manager backend", "completed": False},
    ]


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)