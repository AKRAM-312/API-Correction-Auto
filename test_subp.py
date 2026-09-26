import subprocess

#reponse_attendue = "Hello World"
try:
    p1=subprocess.run( 'python -u test.py' , capture_output= True, text = True , timeout=5)

    if p1.returncode != 0:
        print(f"votre code est incorrect voici le erreur :\n {p1.stderr}")
    else:
        print("le code compilé sans erreur")
except subprocess.TimeoutExpired as e :
    print(f"Erreur : le code a depassé la limite de temps de {e.timeout} secondes ce qui fait que vous avez une boucle infini reverifier le code!")
    