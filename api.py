from fastapi import FastAPI
import uvicorn
import test_subp as test
app = FastAPI()

@app.get("/")

def root():
    return {"Hello": "World"}


@app.post("/correction")

def lancer_correction():
    code_statut,note=test.corrige_code("test.py",4)
    
    return{
        "statut": code_statut,
        "note" : note
    }



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)