from fastapi import FastAPI

from app.api.routes.health import router as health_router
from app.api.routes.tasks import router as tasks_router

app = FastAPI(
    title="Task Manager Backend",
    version="1.0.0",
)

app.include_router(health_router, prefix="/api")
app.include_router(tasks_router, prefix="/api")


@app.get("/")
def root():
    return {"message": "Task Manager Backend is running"}