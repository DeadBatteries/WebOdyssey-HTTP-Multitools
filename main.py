from Core.Requests.request import get_r
from Interface.interface import appInterface, appBanner
from Utils.selectOptions import select_number
from Models.History.addToHistory import addToHistory
from Models.History.history import history
from Interface.showHistory import showHistory
from Models.History.historyOptions import historyOptions

def initApp():

    while True:

        try:

            appInterface()

            choice = select_number()

            match choice:

                case 1:
                    r = get_r()
                    
                    if r:
                        addToHistory(r)
                        
                case 2:
                    
                    showHistory(history)
                    historyOptions()

                case 0:
                    print("Returning to the base...Farewell!")
                    break

        except TypeError as error:

            print(error)

appBanner()
initApp()


