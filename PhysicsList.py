from geant4_pybind import *

class PhysicsList(G4VModularPhysicsList):

    def __init__(self):
        super().__init__()
        self.defaultCutValue = 10.*nm
        self.SetVerboseLevel(1)
        self.RegisterPhysics(G4DecayPhysics())
        self.RegisterPhysics(G4EmDNAPhysics())
        self.RegisterPhysics(G4RadioactiveDecayPhysics())
        self.RegisterPhysics(G4OpticalPhysics())

    def SetCutsWithDefault(self):
        self.SetDefaultCutValue(self.defaultCutValue)
        self.SetCuts()


