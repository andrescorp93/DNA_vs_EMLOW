from geant4_pybind import *

class RunAction(G4UserRunAction):

    def __init__(self, evt_data):
        super().__init__()
        self.evt_data = evt_data

    def BeginOfRunAction(self, aRun):
        # Вызывается в начале каждого рана
        print("RUN START ")
        self.evt_data.Reset()

    def EndOfRunAction(self, aRun):
        # Вызывается в конце каждого рана
        self.evt_data.DumpRunData() # Вызываем метод, записывающий данные на диск
        print(f" Number of events: {aRun.GetNumberOfEvent()}")
        print("RUN END ")

