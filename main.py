from fastapi import FastAPI
app=FastAPI()

@app.get("/")
def example():
    return{'GFG Example':'FastAPI'}