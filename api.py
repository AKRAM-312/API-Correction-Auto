from fastapi import FastAPI,HTTPException
import uvicorn
import test_subp as test
import json
from pydantic import BaseModel,Extra
import tempfile,os
app = FastAPI()

@app.get("/")

def root():
    return {"Hello": "World"}

class fichier(BaseModel):
    exercice_id : str
    code_source : str
    class Config:
        extra = Extra.forbid

@app.post("/correction")




def lancer_correction(s : fichier):
    if not s.exercice_id.isalnum():
        raise HTTPException(400, "exercice_id invalide")
    try:    
        with open(f"{s.exercice_id}.json" ,encoding="utf-8") as f :
            exercice = json.load(f)
    except FileNotFoundError:
         raise HTTPException(404, "exercice introuvable")
    with tempfile.NamedTemporaryFile(mode='w',encoding="utf-8",suffix=".py",delete=False) as tmp :
        tmp.write(s.code_source)
    try:
        note,code_statut=test.corrige_code(tmp.name,exercice["tests"])
        
    finally:
        os.remove(tmp.name)
    return{
        "statut": code_statut,
        "note" : f"{note}/10" 
    }



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)