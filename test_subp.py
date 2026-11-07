import subprocess

#reponse_attendue = "Hello World"

def execute_code (nomF,entrer):
    try:
        p1=subprocess.run( ['python' , f'{nomF}'] , input=entrer ,capture_output= True, text = True  ,timeout=5)
        if p1.returncode != 0:
            return "plantage" , p1.stderr
        else:
           return "ok" , p1.stdout
           
    except subprocess.TimeoutExpired as e :
        return "timeout" , e.timeout

def corrige_code(nomF, test):      
    correct = 0 
    detail_test=[]
    for i in test : 
        statut , output =  execute_code(nomF, i["entree"])
        if(statut == "ok"):
            if output.strip() == i["sortie_attendue"]:
                correct = correct + 1
                detail_test.append(f"test : entrer: {i["entree"]} , output : {output.strip()} | resultat attendue : {i["sortie_attendue"]} | correct ")
            else:
                detail_test.append(f"test : entrer: {i["entree"]} , output : {output.strip()} | resultat attendue : {i["sortie_attendue"]} | incorrect ")
        else:
            detail_test.append(f"test : entrer: {i["entree"]} , output : {statut} | resultat attendue : {i["sortie_attendue"]} | incorrect ") 
    return (correct+len(test)) , detail_test