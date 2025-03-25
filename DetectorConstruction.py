from geant4_pybind import *


class DetectorConstruction(G4VUserDetectorConstruction):

    def __init__(self):
        super().__init__()
        self.size = 1.*mm

    def Construct(self):
        nist = G4NistManager.Instance()
        checkOverlaps = True

        worldMat = nist.FindOrBuildMaterial('G4_Galactic')

        solid = G4Box("world", self.size/2, self.size/2, self.size/2)
        logic = G4LogicalVolume(solid, worldMat, "World")
        physic = G4PVPlacement(None, G4ThreeVector(), logic, "World", None, False, 0, checkOverlaps)
        # logic.SetUserLimits(G4UserLimits(10.*nm))
        icemat = nist.BuildMaterialWithNewDensity('Ice', 'G4_WATER', 0.900 * g / cm3, 10.*kelvin)
        solidIce = G4Box('solidIce', 50*um, 50*um, 50*um);
        logicIce = G4LogicalVolume(solidIce, icemat, 'logicIce');
        # logicIce.SetUserLimits(G4UserLimits(10.*nm))
        physicIce = G4PVPlacement(None, G4ThreeVector(0,0,0), logicIce, 'physicIce', logic, False, 0, checkOverlaps);
        
        return physic
    

