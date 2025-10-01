#Q.4.1 

%pylab inline

from codepyheat.geometry import Column
from codepyheat import JSONPATH

K_ref = 1e-5
lambda_s_ref = 2
n_ref = 0.1

# step 1
dico = {
    "depth": {
            "val": "1",
            "unit": "m"
        },
    "ncells": 100
}

rivBed = Column(dico)
rivBed.printProps()

# step 2
rivBed.setHomogeneousPorMed(JSONPATH + "paramColumn.json")
rivBed.physProp.printProps()

# step 3
rivBed.setBcHyd(JSONPATH + "configBcHydro_4.1.json")
rivBed.setBcT(JSONPATH + "configBcTemp_4.1.json")

# step 4 running forward model with other parameter values
ref = rivBed.runForwardModelSteadyState(K_ref, lambda_s_ref, n_ref)


#suite Q.4.1 en réflexion... j'essaye de voir comment accéder aux graphiques des différentes simulations... 
#à partir du code de geometry.py... 

simulations = []

for elt in params:
    Dict_Param["moinslog10K"] = elt[0]
    Dict_Param["lambda_s"] = elt[1]
    Dict_Param["n"] = elt[2]
    simulations.append(model_direct(Dict_Param, brouillee = True))
    
#it = caracItSteadyTemplate.format(
#               physP.getUpperK(), physP.getLambda(), physP.getPorosity()
#            )

for simu in simulations:
    simu.iterativePlotT(it) #essayer de le mettre sur un même graphique...



#Q.4.3 

#idée potentielle : cru/innondations, statue au milieu de la Seine - le zouave du point de l'Alma 
