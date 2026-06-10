from fastapi import APIRouter

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.get("/")
def get_tasks():
    return {
        "message": "Tasks API working",
        "data": [],
    }


@router.post("/")
def create_task():
    return {
        "message": "Task created successfully",
    }