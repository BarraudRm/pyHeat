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
