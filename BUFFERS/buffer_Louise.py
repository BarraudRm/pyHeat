
#Question 2.4 Energy 

def energie_systeme(tempe_modele, tempe_obs, sigma_obs):
    """
    Calcule l'énergie du système pour le MCMC.
    tempe_modele : liste des températures simulées aux points de mesure
    tempe_obs : liste des températures observées (bruitées)
    sigma_obs : écart-type de l'erreur de mesure
    """
    tempe_modele = np.array(tempe_modele)
    tempe_obs = np.array(tempe_obs)
    return np.sum((tempe_modele - tempe_obs)**2) / (2 * sigma_obs**2)

temp_obs=tempe_brouille
sigma_obs=1

#Question 3.1

import numpy as np

# Initialisation
N = 1000  # nombre d'itérations
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

Dict_Param["K"] = K
Dict_Param["lambda_s"] = lambda_s
Dict_Param["n"] = n

tempe_obs=get_temp_echant(echant)
profil, tempe_modele = modele_directe(Dict_Param)
E = energie_systeme(tempe_modele, tempe_obs, sigma_obs)

params[0] = [moinslog10K, lambda_s, n]
energies[0] = E
profils.append(profil)
accepts[0] = 1

for i in range(1, N):
    # Propositions
     
    K_prop = perturbation(K, sigma_moinslog10K, range_moinslog10K,True)
    lambda_s_prop = perturbation(lambda_s, sigma_lambda_s, range_lambda_s)
    n_prop = perturbation(n, sigma_n, range_n)

    Dict_Param["K"] = K_prop
    Dict_Param["lambda_s"] = lambda_s_prop
    Dict_Param["n"] = n_prop
    profil_prop,tempe_modele_prop = modele_directe(Dict_Param)
    E_prop = energie_systeme(tempe_modele_prop, tempe_obs, sigma_obs)

    # Calcul du ratio d'acceptation
    #Par symétrie de la fonction q, la proba d'acceptation ne dépend que de pi
    alpha = np.exp(E - E_prop) #probabilité d'acceptation, déterminée uniquement par la loi gaussienne propositionnelle 
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



import numpy as np
import matplotlib.pyplot as plt

proba_accept = np.cumsum(accepts) / np.arange(1, N + 1) # probabilité d'acceptation cumulée grace à np.cumsum

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(energies)
plt.xlabel('Itérations')
plt.ylabel('Énergie')
plt.title('Énergie du système au cours des itérations MCMC')
plt.grid()

plt.subplot(1, 2, 2)
plt.plot(proba_accept)
plt.xlabel('Itérations')
plt.ylabel('Proba. acceptation')
plt.title('Probabilité d\'acceptation cumulée')
plt.grid()

plt.tight_layout()
plt.show()


#Histogrammes des paramètres

import matplotlib.pyplot as plt

plt.figure(figsize=(15, 4))

plt.subplot(1, 3, 1)
plt.hist(params[:,0], bins=40, color='skyblue', edgecolor='black')
plt.xlabel('-log10(K)')
plt.title('Histogramme a posteriori de -log10(K)')

plt.subplot(1, 3, 2)
plt.hist(params[:,1], bins=40, color='salmon', edgecolor='black')
plt.xlabel('lambda_s')
plt.title('Histogramme a posteriori de lambda_s')

plt.subplot(1, 3, 3)
plt.hist(params[:,2], bins=40, color='lightgreen', edgecolor='black')
plt.xlabel('n')
plt.title('Histogramme a posteriori de n')

plt.tight_layout()
plt.show()

#Histogramme 2D suite

plt.figure(figsize=(15, 4))

plt.subplot(1, 3, 1)
plt.hist2d(params[:,0], params[:,1], bins=40, cmap='Blues')
plt.xlabel('-log10(K)')
plt.ylabel('lambda_s')
plt.title('K vs lambda_s')
plt.colorbar(label='Nombre d\'échantillons')

plt.subplot(1, 3, 2)
plt.hist2d(params[:,0], params[:,2], bins=40, cmap='Greens')
plt.xlabel('-log10(K)')
plt.ylabel('n')
plt.title('K vs n')
plt.colorbar(label='Nombre d\'échantillons')

plt.subplot(1, 3, 3)
plt.hist2d(params[:,1], params[:,2], bins=40, cmap='Oranges')
plt.xlabel('lambda_s')
plt.ylabel('n')
plt.title('lambda_s vs n')
plt.colorbar(label='Nombre d\'échantillons')

plt.tight_layout()
plt.show()

#Médianes et quartile

import numpy as np
import matplotlib.pyplot as plt

profils_array = np.array(profils)  # (N, ncells)
median = np.median(profils_array, axis=0)
q025 = np.quantile(profils_array, 0.025, axis=0)
q975 = np.quantile(profils_array, 0.975, axis=0)

plt.figure(figsize=(10,6))
plt.plot(ref, label='Profil de référence', color='black', linewidth=2)
plt.plot(median, label='Médiane a posteriori', color='blue')
plt.fill_between(np.arange(len(median)), q025, q975, color='blue', alpha=0.2, label='Quantiles 2.5% - 97.5%')

# Affichage des données bruitées aux points d'échantillonnage
plt.scatter([int(100*x) for x in echant], tempe_brouille, color='red', label='Données bruitées', zorder=10)

plt.xlabel('Cellule')
plt.ylabel('Température')
plt.title('Profil de température : médiane et quantiles')
plt.legend()
plt.grid()
plt.show()