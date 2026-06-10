# task-manager-backend-python
git clone https://github.com/BuildMates/task-manager-backend.git
cd task-manager-backend

python -m venv .venv
pip install -r requirements.txt
python -m uvicorn main:app --reload