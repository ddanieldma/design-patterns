class ApplicationState:
    instance = None

    def __init__(self):
        self.isLoggedIn = False

    # Retorna estado global do aplicativo
    @staticmethod
    def getAppState():
        # Se não tiver uma instância
        if not ApplicationState.instance:
            # Define uma, que deve ser única. de forma que tenhamos um 
            # singleton
            ApplicationState.instance = ApplicationState()
        return ApplicationState.instance
    
appState1 = ApplicationState.getAppState()
print(appState1.isLoggedIn) # False

appState2 = ApplicationState.getAppState() # False tambem
appState1.isLoggedIn = True

print(appState1.isLoggedIn) # True
print(appState2.isLoggedIn) # True