from fastapi import FastAPI
from app.api import auth, gmail, ai, user

app = FastAPI()


#routes
app.include_router(auth.router)
app.include_router(gmail.router)
app.include_router(ai.router)
app.include_router(user.router)

#start endpoint
@app.on_event("startup")
def startup_event():
    print("Starting up...")
@app.get("/")
def read_root():
    return {"status": "ok"}
