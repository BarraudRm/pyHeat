#Question 3.1

import numpy as np

# Initialisation
N = 5000  # nombre d'itérations
params = np.zeros((N, 3))
energies = np.zeros(N)
accepts = np.zeros(N)
profils = []


sigma_obs = 1


# Tirage initial selon le prior
moinslog10K = np.random.uniform(*range_moinslog10K)
lambda_s = np.random.uniform(*range_lambda_s)
n = np.random.uniform(*range_n)
K = 10**(-moinslog10K)

tempe_modele, profil = modele_direct(K, lambda_s, n)
E = energie_systeme(tempe_modele, temp_obs, sigma_obs)

params[0] = [moinslog10K, lambda_s, n]
energies[0] = E
profils.append(profil)
accepts[0] = 1

for i in range(1, N):
    # Propositions
    K_prop = perturbation(K, sigma_moinslog10K, range_moinslog10K,True)
    lambda_s_prop = perturbation(lambda_s, sigma_lambda_s, range_lambda_s)
    n_prop = perturbation(n, sigma_n, range_n)
    
    
    tempe_modele_prop, profil_prop = modele_direct(K_prop, lambda_s_prop, n_prop)
    E_prop = energie_systeme(tempe_modele_prop, temp_obs, sigma_obs)
    
    # Calcul du ratio d'acceptation
    alpha = np.exp(E - E_prop) #probabilité d'acceptation, déterminée par la loi gaussienne propositionnelle 
    if np.random.rand() < alpha:
        # Acceptation
        K, lambda_s, n = K_prop, lambda_s_prop, n_prop
        E = E_prop
        profil = profil_prop
        accepts[i] = 1
    else:
        accepts[i] = 0
    
    params[i] = [K, lambda_s, n]
    energies[i] = E
    profils.append(profil)
