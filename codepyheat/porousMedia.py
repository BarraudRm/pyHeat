"""
    @author: Nicolas Flipo
    @date: 10.02.2021

    Class PorousMedia is built upon the classes PropHydro in hydrogeol.py
        and PropMedia in heat.py
    It implements the calculation of effective and equivalent parameters
        for porous media

"""

from codepyheat.factory import FactoryClass
from codepyheat.hydrogeol import PropHydro, RHOW, CODE_HYD
from codepyheat.heat import PropMedia, LAMBDAW, HEATCAPAW
from codepyheat import caracParamTemplate

from codepyheat import JSONPATH


class PropPorousMedia(FactoryClass):
    kappa = CODE_HYD

    def __init__(self, paths):
        self.propH = PropHydro.fromJsonFile(JSONPATH + paths['hydroFile'])
        self.propM = PropMedia.fromJsonFile(JSONPATH + paths['sedFile'])
        self.propM.nameM = paths['name']

    def printProps(self):
        self.propH.printProp()
        self.propM.printProp()
        self.printParamEq()
        self.printParamEffective()

    def setEffectiveParams(self):
        self.kappa = (
            self.propM.getLambdaEq(LAMBDAW, self.propH.n)
            / (RHOW * HEATCAPAW)
        )

    def getKappa(self):
        self.setEffectiveParams()
        return self.kappa

    def setPermeability(self, upperK):
        return self.propH.setPermeability(upperK)

    def getUpperK(self):
        return self.propH.upperK

    def setPorosity(self, porosity):
        self.propH.setPorosity(porosity)

    def getPorosity(self):
        return self.propH.getPorosity()

    def setLambda(self, lambd):
        self.propM.setLambda(lambd)

    def getLambda(self):
        return self.propM.getLambda()

    def getLambdaEq(self, lw, porosity):
        return self.propM.getLambdaEq(lw, porosity)

    def setHeatCapa(self, hc):
        self.propM.setHeatCapa(hc)

    def getHeatCapa(self):
        return self.propM.getHeatCapa()

    def setRho(self, rho):
        self.propM.rho = rho

    def getRho(self):
        return self.propM.rho

    def setNameM(self, name):
        self.propM.setName = name

    def getNameM(self):
        return self.propM.getName()

    def printParamEffective(self):
        print("effective parameters of {}:\n", self.propM.nameM)
        print(caracParamTemplate.format(
            '\teffective thermal conductivity',
            self.getKappa(), 'TO SPECIFY LATER')
        )

    def printParamEq(self):
        print('equivalent parameters of ', self.propM.nameM, ':')
        print(caracParamTemplate.format(
            '\tequivalent thermal conductivity: ',
            self.propM.getLambdaEq(LAMBDAW, self.propH.n),
            'W m-1 K-1'))
