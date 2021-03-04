"""
    @author: Nicolas Flipo
    @date: 10.02.2021

    Contains 3 Classes related to heat :
    Heat which contains T, and fluxes
    PropMedia which contains the grain properties
    BoundaryConditionHeat which contains only Triv and Taq

"""

from codepyheat.factory import FactoryClass
from codepyheat.units import calcValMult, calcValAdd
from codepyheat import printDir, printDirCard, caracParamTemplate

RHOS = 2500  # sediment density kg m-3
LAMBDAS = 2  # sediment thermal conductivity W m-1 K-1 = kg m s-3 K-1
HEATCAPAS = 1250  # sediment specific heat capacity m2 s-2 K-1


LAMBDAW = 0.598  # water thermal conductivity W m-1 K-1
HEATCAPAW = 4185  # water specific heat capacity m2 s-2 K-1
CODE_HEAT = -3333


class PropMedia(FactoryClass):
    """
        instantiate with
            - PropMedia(a_dict)
            - PropMedia.fromJsonFile(full path and file name)
            - PropMedia.fromJsonString(valid json string)

    """
    nameM = 'Undefined'
    lambd = LAMBDAS
    heatCapa = HEATCAPAS
    rho = RHOS

    def __init__(self, propM=None):
        if propM is not None:
            self.lambd = calcValMult(propM['sediment']['lambda'], "lambda")
            self.setHeatCapa(calcValMult(propM['sediment']
                                         ['specificHeatCapacity'],
                                         "specificHeatCapacity"
                                         )
                             )
            self.rho = calcValMult(propM['sediment']['rho'], "rho")

    def setLambda(self, lambd):
        self.lambd = lambd

    def getLambda(self):
        return self.lambd

    def setHeatCapa(self, heatCapa):
        self.heatCapa = heatCapa

    def getHeatCapa(self):
        return self.heatCapa

    def setRho(self, rho):
        self.rho = rho

    def getRho(self):
        return self.rho

    def setName(self, name):
        self.nameM = name

    def getName(self):
        return self.nameM

    def setAll(self, lambd, heatCapa, rho):
        self.lambd = lambd
        self.heatCapa = heatCapa
        self.rho = rho

    def getLambdaEq(self, lw, n):
        lambd = pow(
                (n * pow(lw, 0.5)+(1-n) * pow(self.lambd, 0.5)), 2
            )  # lw lambda water, n porosity
        return lambd

    def setNameM(self, name):
        self.nameM = name

    def getNameM(self):
        return self.nameM

    def printProp(self):
        print("Thermal Properties of the phase (pure solid)", self.nameM)
        print(caracParamTemplate.format(
            '\tthermal conductivity:',
            self.lambd,
            'W m-1 K-1'))
        print(caracParamTemplate.format(
            '\tspecific heat capacity:',
            self.heatCapa,
            'm2 s-2 K-1'))
        print(caracParamTemplate.format('\tdensity:', self.rho, 'kg m-3'))


class Heat:
    upperT = CODE_HEAT
    speciHeatFlux = CODE_HEAT
    heatFlux = CODE_HEAT
    type = 'regular'

    def setT(self, temperature):
        self.upperT = temperature

    def setSpeciHeatFlux(self, upperU):
        self.speciHeatFlux = self.upperT * upperU  # U in m.s-1

    def setHeatFluxFromQ(self, upperQ):
        self.heatFlux = self.upperT * upperQ  # Q in m3.s-1

    def setHeatFluxFromSurf(self, surf):
        self.heatFlux = self.speciHeatFlux * surf

    def setAllFlux(self, upperU, surf):
        self.setSpeciHeatFlux(upperU)
        self.setHeatFluxFromSurf(surf)

    def setAll(self, upperT, upperU, surf):
        self.setT(upperT)
        self.setSpeciHeatFlux(upperU)
        self.setHeatFluxFromSurf(surf)

    def setDirichletCell(self, dir, num):
        self.type = "BcDirichlet, face -> {}{}".format(
            printDir(dir),
            printDirCard(dir, num)
        )

    def setDirichletFace(self, upperT):
        self.type = 'BcDirichlet'
        self.upperT = upperT


class BoundaryConditionHeat(FactoryClass):
    """
        instantiate with
            - BoundaryConditionHeat(a_dict)
            - BoundaryConditionHeat.fromJsonFile(full path and file name)
            - BoundaryConditionHeat.fromJsonString(valid json string)

    """
    def __init__(self, bcs):
        # print('first level keys:',bcs.keys())
        # print('second level keys:',bcs['dH'].keys())
        self.tempRiv = calcValAdd(bcs['Triv'], "Triv")
        self.tempAq = calcValAdd(bcs['Taq'], "Taq")
