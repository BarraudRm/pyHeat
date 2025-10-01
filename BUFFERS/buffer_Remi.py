# QUESTION 2.4

Dict_Param = {
    "K": K_ref,
    "lambda_s": lambda_s_ref,
    "n": n_ref
}

def modele_directe (Dict_Param, brouillee = True):
    ref = rivBed.runForwardModelSteadyState(Dict_Param["K"], Dict_Param["lambda_s"], Dict_Param["n"])
    t_echant = get_temp_echant(echant, brouillee=brouillee)
    return ref, t_echant

ref, t_echant_brouille = modele_directe(Dict_Param)

#print(max(t_echant_brouille))
#print(ref)

#FIN QUESTION 2.4