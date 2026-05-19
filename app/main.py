from fastapi import FastAPI
from app.routes import auth, gmail, ai

app = FastAPI()


#routes
app.include_router(auth.router)
app.include_router(gmail.router)
app.include_router(ai.router)

#start endpoint
@app.on_event("startup")
def startup_event():
    print("Starting up...")
@app.get("/")
def read_root():
    return {"status": "ok"}
