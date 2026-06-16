from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.controllers.health import router as health_router
from app.controllers.user_auth import router as user_auth_router

app = FastAPI(
    title="Task Manager Backend",
    version="1.0.0",
)

origins = [
    "http://localhost:5173",
    "http://localhost:3000",
    "http://13.205.158.142",
    "https://your-frontend-domain.com",
    "http://buildmates-frontend-dev.s3-website.ap-south-1.amazonaws.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,        # use ["*"] for quick testing only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router, prefix="/api")
app.include_router(user_auth_router, prefix="/api")


@app.get("/")
def root():
    return {"message": "Task Manager Backend is running"}