import sqlite3
import json


def connexion():
        return sqlite3.connect("database.db")



def init_db():
    try:
        with connexion() as conn:
            cursor = conn.cursor()
            sql= '''
                    CREATE TABLE IF NOT EXISTS review (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    code_source TEXT,
                    exercice_id TEXT,
                    statut TEXT,
                    note TEXT
                    );'''
            cursor.execute(sql)
            conn.commit()
            conn.close()
    except Exception as e :
        print(f"An error occurred while creating the table : {e}")  


def record_review(exercice_id , note , code_source , statut):
    try:
        with connexion() as conn :
            cursor = conn.cursor()
            sql= "INSERT INTO review (code_source , exercice_id , statut , note) VALUES (?,?,?,?) ;"
            cursor.execute(sql , (code_source , exercice_id , json.dumps(statut) , note))
            conn.commit()
            conn.close()
    except Exception as e :
        print(f"An error occured while insering the review : {e}")
                
