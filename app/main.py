from fastapi import FastAPI

app = FastAPI()


#start endpoint
@app.get("/")
def read_root():
    print("running...")
    return {"status": "ok"}
