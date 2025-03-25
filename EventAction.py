from geant4_pybind import *

class EventAction(G4UserEventAction):

    def __init__(self, evt_data):
        super().__init__()
        self.evt_data = evt_data

    def BeginOfEventAction(self, anEvent):
        # Вызывается в начале каждого события
        pass

    def EndOfEventAction(self, anEvent):
        # Вызывается в конце каждого события
        evt_id = anEvent.GetEventID()
        print(f" event #{evt_id} complete ")
