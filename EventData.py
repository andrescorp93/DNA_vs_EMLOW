import numpy as np
from geant4_pybind import *
import sys, os


class EventDataMessenger(G4UImessenger):

    def __init__(self, evt_data):
        super().__init__()
        self.evt_data = evt_data   # привязка к объекту, который создал этот мессенджер
        self.directory = G4UIdirectory("/output/")
        self.directory.SetGuidance("HDF5 output control")
        self.path_cmd = G4UIcmdWithAString("/output/path", self)
        self.path_cmd.SetGuidance("Set path for HDF5 output. Available only before initialization (/run/initialize)")
        self.path_cmd.SetParameterName("path", False)
        self.path_cmd.AvailableForStates(G4State_PreInit, G4State_Idle)

    def SetNewValue(self, command, newValue):
        if command == self.path_cmd:
            self.evt_data.SetOutputPath(newValue)


class EventData():

    def __init__(self):
        self.path = "output.npz"
        self.steps = []            # Каждые элемент списка -- запись со всеми шагами для одного события
        self.messenger = EventDataMessenger(self)

    def Reset(self):               # Сбрасываем содержимое
        self.steps = []

    def SetOutputPath(self, path): # Меняем имя выходного файла
        self.path = path
        if os.path.exists(path):
            print(f"WARNING: overriding existing data file '{self.path}'")
            os.remove(self.path)

    def KeepStepData(self, data):  # Записываем данные с одного шага
        self.steps.append(data)

    def DumpRunData(self):         # Сохраняем на диск
        np.savez(self.path, steps=self.steps)
        # Чтобы открыть: 
        #   data = np.load('output.npz', allow_pickle=True)
        #   data['steps']
        
