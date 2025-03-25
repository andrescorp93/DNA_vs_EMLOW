from geant4_pybind import *
from DetectorConstruction import DetectorConstruction
from PrimaryGeneratorAction import PrimaryGeneratorAction
from RunAction import RunAction
from EventAction import EventAction
from StackingAction import StackingAction
from SteppingAction import SteppingAction
from EventData import EventData
from PhysicsList import *

import sys

class ActionInitialization(G4VUserActionInitialization):
    # Инициализация объектов управляющих разными этапами моделирования
    # с реализацией многопоточности

    def __init__(self, evt_data):
        super().__init__()
        self.evt_data = evt_data               # управление записью данных на диск

    def BuildForMaster(self):
        pass
        #self.SetUserAction(RunAction(None))   # запуск Рана -- самый глобальный этап

    def Build(self):
        evt_data = self.evt_data
        self.SetUserAction(PrimaryGeneratorAction(self.evt_data))   # создание первичной частицы
        self.SetUserAction(RunAction(self.evt_data))                # самый глобальный этап
        self.SetUserAction(EventAction(self.evt_data))              # на каждое событие
        self.SetUserAction(StackingAction(self.evt_data))           # на каждую новую частицу
        self.SetUserAction(SteppingAction(self.evt_data))           # на каждый шаг любой частицы


#########################
## Инициализация всего ##
#########################

# Запись данных
evt_data = EventData()

# Создание менеджера раном
runManager = G4RunManagerFactory.CreateRunManager(G4RunManagerType.Serial)
# runManager = G4RunManagerFactory.CreateRunManager(G4RunManagerType.MT, 4)

# Инициализации геометрии
runManager.SetUserInitialization(DetectorConstruction())

# Инициализация физики
# physicsList = FTFP_BERT()
physicsList = PhysicsList()
# cutLength = 1*nm
# physicsList.SetCutValue(cutLength, "gamma");
# physicsList.SetCutValue(cutLength, "e-");
# physicsList.SetCutValue(cutLength, "e+");
# physicsList.SetCutValue(cutLength, "proton");
# physicsList.SetVerboseLevel(1)
runManager.SetUserInitialization(physicsList)

# Инициализация объектов для управления этапами моделирования
runManager.SetUserInitialization(ActionInitialization(evt_data))

# Инициализация визуализации
visManager = G4VisExecutive("Quiet")
visManager.Initialize()

# Инициализация пользовательского интерфейса и запуск сессии
UImanager = G4UImanager.GetUIpointer()

#   Интерактивный режим, если аргументов не было
if len(sys.argv) == 1:
    ui = G4UIExecutive(len(sys.argv), sys.argv)
    UImanager.ApplyCommand("/control/execute init_vis.mac")
    ui.SessionStart()

#   Фоновый режим, если был передан macro-файл в качестве аргумента
else:
    fileName = sys.argv[1]
    UImanager.ApplyCommand("/control/execute "+fileName)

