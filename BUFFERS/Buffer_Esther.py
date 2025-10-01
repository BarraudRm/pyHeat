#Q.2.3

import numpy as np
def perturbation(param, sigma, range, K=False): 
    if K:
        param = -np.log10(param)
    result = param + np.random.normal(0, sigma)
    if result < range[0] or result > range[1]:
        reste = result%abs(range[1]-range[0])
        result = range[0] + reste
    if K:
        result = 10**(-result)
    return result

""""""


"""""""
#Q.2.4 cellule 2

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

E = energie_systeme(model_direct, temp_obs, sigma_obs)

def energie(model_direct, temp_obs, sigma_obs):
    energie = (1/2*sigma_obs**2)*sum((temp_obs[i]-model_direct(Dict_Param)[2][i])**2 for i in [20,40,60,80])
    return energie

#ce que j'observe c'est l'échantillonage? et mes données observées sont celles calculées avec modèle direct?
#-log vraissemblance (erreur quadratique connue, normalisée par sigma_obs)
#on compare là où on a des données!

#Q.2.5 cellule 1

def initialisation_param():
    K = 10**(-np.random.uniform(range_moinslog10K[0], range_moinslog10K[1]))
    lambda_s = np.random.uniform(range_lambda_s[0], range_lambda_s[1])
    n = np.random.uniform(range_n[0], range_n[1])
    dico = {
        "K" : K,
        "lambda_s" : lambda_s,
        "n" : n }
    return dico

#voir ce que Rémi renvoie... 
Val_model(initialisation_param)
Energie_model = energie(Val_model)


#Q.2.5 cellule 2

nb_iterations = 100
val_param = np.ndarray((nb_iterations, 3))
energie_etats = np.ndarray(nb_iterations)
moy_taux_acceptation = np.ndarray(nb_iterations)
profils_temp = np.ndarray((nb_iterations, len(ref)))
val_param[0] = [initialisation_param()[key] for key in ["K", "lambda_s", "n"]]
energie_etats[0] = Energie_model    
moy_taux_acceptation[0] = #trouver la formule...
profils_temp[0] = #fonction rémi 
#conserver tout cela pour chacun des états générés 
#formule taux d'acceptation? calcul de la probabilité d'acceptation
