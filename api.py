from fastapi import FastAPI,HTTPException
import uvicorn
import test_subp as test
import json
from pydantic import BaseModel,Extra
import tempfile,os
import database as db


app = FastAPI()


db.init_db()


class fichier(BaseModel):
    exercice_id : str
    code_source : str
    class Config:
        extra = Extra.forbid

@app.get("/")

def root():
    return {"Hello": "World"}


@app.post("/correction")

def lancer_correction(s : fichier):
    
    if not s.exercice_id.isalnum():
        raise HTTPException(400, "exercice_id invalide")
    
    #loading the json associated to the id of the exercise 
    try:    
        with open(f"{s.exercice_id}.json" ,encoding="utf-8") as f :
            exercice = json.load(f)
    except FileNotFoundError:
         raise HTTPException(404, "exercice introuvable")

    # loading code source of the user in a temporary file
    with tempfile.NamedTemporaryFile(mode='w',encoding="utf-8",suffix=".py",delete=False) as tmp :
        tmp.write(s.code_source)
    
    try:
        # executing the code with our function (corrige_code) to get the results 
        note,code_statut=test.corrige_code(tmp.name,exercice["tests"])

        # on enregistre tout dans notre base de données
        db.record_review(s.exercice_id , f"{note}/10" ,s.code_source , code_statut)
    finally:
        # removing the tempfile with os.remove so that the file doesnt just sit around in the folder
        os.remove(tmp.name)
    
    return{
        "statut": code_statut,
        "note" : f"{note}/10" 
    }



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)