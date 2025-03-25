from geant4_pybind import *

class PrimaryGeneratorAction(G4VUserPrimaryGeneratorAction):

    def __init__(self, data, particle_type = 'proton', energy=10*MeV, pos=[0,0,-0.4*mm]):
        super().__init__()
        self.data = data
        self.particle_gun = G4ParticleGun(1)

        # Параметры первичной частицы
        particleTable = G4ParticleTable.GetParticleTable()
        particle = particleTable.FindParticle(particle_type)
        self.particle_gun.SetParticleDefinition(particle)
        self.particle_gun.SetParticlePosition(G4ThreeVector(*pos))
        self.particle_gun.SetParticleMomentumDirection(G4ThreeVector(0, 0, 1))
        self.particle_gun.SetParticleEnergy(energy)


    def GeneratePrimaries(self, anEvent):
        # Вызывается в начале каждого события;
        # здесь можно менять параметры первичной частицы, если это необходимо
        self.particle_gun.GeneratePrimaryVertex(anEvent)
