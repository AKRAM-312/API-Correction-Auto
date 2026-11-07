from fastapi import FastAPI
import uvicorn
import test_subp as test
import json
app = FastAPI()

@app.get("/")

def root():
    return {"Hello": "World"}


@app.post("/correction")

def lancer_correction(nomF , id):
    with open(f"{id}.json" ,encoding="utf-8") as f :
        exercice = json.load(f)
    note,code_statut=test.corrige_code(nomF,exercice["tests"])
    
    return{
        "statut": code_statut,
        "note" : f"{note}/10" 
    }



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)