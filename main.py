"""

    @author: Nicolas Flipo
    @date: 11.02.2021

    main file of pyHeat1D
    Everything is based on the Column class in geometry.py
        1.  initialisation from a JSON file
        2.  setting up the properties of the porous medium with JSON files
        3.  setting up the boundary conditions (hydraulique and thermal) with
            JSON files
        4.  solving the problem and printing and plotting the results
        5.  setting up other parameter values and solving again

"""
from codepyheat.geometry import Column
from codepyheat import JSONPATH, LAMBDAW
import matplotlib.pyplot as plt
import numpy as np

# step 1
rivBed = Column.fromJsonFile(JSONPATH + "configColumn.json")
rivBed.printProps()

# step 2
rivBed.setHomogeneousPorMed(JSONPATH + "paramColumn.json")
rivBed.physProp.printProps()

# step 3
rivBed.setBcHyd(JSONPATH + "configBcHydro.json")
rivBed.setBcT(JSONPATH + "configBcTemp.json")
rivBed.printBcHydSteady()
rivBed.printBcTempSteady()

# step 4 solving the problem and printing and plotting the results
upperK = rivBed.physProp.propH.upperK
porosity = rivBed.physProp.propH.n
lambd = rivBed.physProp.propM.getLambdaEq(LAMBDAW,porosity)
rivBed.runForwardModelSteadyState(upperK, lambd, porosity)

# step 5 running forward model with other parameter values
z = rivBed.generateZAxis()
for l in (2,4,6,8) :
    plt.plot(rivBed.runForwardModelSteadyState(1e-5, l, 0.1,False,False,False),z,label=f"lambdas={l}")
    
plt.legend()
plt.ylabel("hauteur colonne (m)")
plt.xlabel("Température de l'eau (K)")
plt.title("Profil de température en fonction de la conductivité thermique")
plt.show()
#rivBed.runForwardModelSteadyState(1e-5, 2, 0.1)

#rivBed.runForwardModelSteadyState(1e-7, 2, 0.1)
# rivBed.iterativePlotT(caracItSteadyTemplate.format(rivBed.physProp.upperK,rivBed.physProp.lambd,rivBed.physProp.n))

print('End of simulation pyHeat steady')
