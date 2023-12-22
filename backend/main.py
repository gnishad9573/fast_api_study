from fastapi import FastAPI
from core.config import setting

app = FastAPI(title=setting.PROJECT_TITLE, version=setting.PROJECT_VERSIION)

@app.get("/")
def hello():
    return {"msg": "hello this is ganesh "}