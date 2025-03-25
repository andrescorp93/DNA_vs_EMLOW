from geant4_pybind import *
import numpy as np

class SteppingAction(G4UserSteppingAction):

    def __init__(self, evt_data):
        super().__init__()
        self.evt_data = evt_data
        self.run_manager = G4RunManager.GetRunManager()

    def UserSteppingAction(self, step):
        # вызывается на каждом шаге
        dtypes = np.dtype([ ('g4id',int), ('pdgid', int), ('parent_id', int), ('part_name', np.str_, 16),
                            ('proc_name', np.str_, 16), ('x_um', float), ('y_um', float), ('z_um', float), 
                            ('t_ps', float), ('Etot_keV', float), ('Ekin_keV', float), ('Edep_keV', float) ])
        step_info = np.empty(1, dtype=dtypes)
        track = step.GetTrack()

        step_info['g4id'] = track.GetTrackID()
        step_info['pdgid'] = track.GetDefinition().GetPDGEncoding()
        step_info['parent_id'] = track.GetParentID()
        step_point = step.GetPostStepPoint()
        step_info['proc_name'] = step_point.GetProcessDefinedStep().GetProcessName()
        step_info['part_name'] = track.GetParticleDefinition().GetParticleName()
        pos = step_point.GetPosition()
        step_info['x_um'] = pos.x/um
        step_info['y_um'] = pos.y/um
        step_info['z_um'] = pos.z/um
        step_info['t_ps'] = step_point.GetGlobalTime()/ps
        step_info['Etot_keV'] = step_point.GetTotalEnergy()/keV
        step_info['Ekin_keV'] = step_point.GetKineticEnergy()/keV
        step_info['Edep_keV'] = step.GetTotalEnergyDeposit()/keV
        #evt_id = self.run_manager.GetCurrentEvent().GetEventID()
        self.evt_data.KeepStepData(step_info)
