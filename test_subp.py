import subprocess

#reponse_attendue = "Hello World"

def corrige_code(nomF , reponse_attendue):      
    try:
        p1=subprocess.run( ['python' , f'{nomF}'] , capture_output= True, text = True  ,timeout=5)

        if p1.returncode != 0:
            return f"votre code est incorrect voici le erreur :\n {p1.stderr}" , "0/10"
        else:
            print("le code executé sans erreur")
            if p1.stdout.strip() == str(reponse_attendue).strip() :
                return "Votre code est correct" , "10/10"
            else:
                return "Votre code est incorrect", "5/10"
    except subprocess.TimeoutExpired as e :
        return f"Erreur : le code a depassé la limite de temps de {e.timeout} secondes ce qui fait que votre code peut contenir une boucle infini reverifier le!" , "0/10"

code_statut,note = corrige_code("test.py",4)
print(code_statut , note)