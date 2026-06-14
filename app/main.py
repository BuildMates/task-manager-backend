from fastapi import FastAPI

from app.controllers.health import router as health_router
from app.controllers.user_auth import router as user_auth_router


app = FastAPI(
    title="Task Manager Backend",
    version="1.0.0",
)


app.include_router(health_router, prefix="/api")
app.include_router(user_auth_router, prefix="/api")


@app.get("/")
def root():
    return {"message": "Task Manager Backend is running"}