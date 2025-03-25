from geant4_pybind import *

class StackingAction(G4UserStackingAction):

    def __init__(self, evt_data):
        super().__init__()
        self.evt_data = evt_data
        #self.run_manager = G4RunManager.GetRunManager()

    def ClassifyNewTrack(self, track):
        # вызывается по началу транспорта каждой частицы
        #evt_id = self.run_manager.GetCurrentEvent().GetEventID()
        return G4ClassificationOfNewTrack.fUrgent

