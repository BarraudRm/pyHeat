# QUESTION 1.2
import numpy as np 

def temp(depth):
    n,h=int(dico["ncells"]),int(dico["depth"]["val"])
    return ref[ int(n*depth/h) ]

echant=[0.2,0.4,0.6,0.8]

def get_temp_echant(echant, brouillee = True):
    tempe=[]
    for val in echant : 
        tempe.append( float(temp(val)))
    tempe_brouille=[]
    for val in echant : 
        tempe_brouille.append( float(temp(val)) + np.random.normal(0,1) )
    if brouillee:
        return tempe_brouille
    else:
        return tempe   

print(get_temp_echant(echant))
print(get_temp_echant(echant, brouillee=False))

# QUESTION 2.4

Dict_Param = {
    "K": K_ref,
    "lambda_s": lambda_s_ref,
    "n": n_ref
}

def model_direct (Dict_Param, brouillee = True):
    ref = rivBed.runForwardModelSteadyState(Dict_Param["K"], Dict_Param["lambda_s"], Dict_Param["n"])
    t_echant = get_temp_echant(echant, brouillee=brouillee)
    return ref, t_echant

ref, t_echant_brouille = model_direct(Dict_Param)

#print(max(t_echant_brouille))
#print(ref)

#FIN QUESTION 2.4