from fastapi import FastAPI
from app.routes import auth

app = FastAPI()


#auth routes
app.include_router(auth.router)


#start endpoint
@app.on_event("startup")
def startup_event():
    print("Starting up...")
@app.get("/")
def read_root():
    return {"status": "ok"}
