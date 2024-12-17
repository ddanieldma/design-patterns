class Burger:
    def __init__(self):
        self.buns = None
        self.patty = None
        self.cheese = None

    def setBuns(self, bunStyle):
        self.buns = bunStyle
        
    def setPatty(self, pattyStyle):
        self.patty = pattyStyle
        
    def setCheese(self, cheeseStyle):
        self.cheese = cheeseStyle
    
    def print(self):
        print(f"Ingredients: {self.buns}, {self.patty}, {self.cheese}")

class BurgerBuilder:
    def __init__(self):
        # Cria objeto de burger vazio
        self.burger = Burger()

    # E vai adicionando seus ingredientes
    # Cada método precisa retornar a própria classe para que seja possível 
    # chamar os métodos um em cima do outro
    def addBuns(self, bunStyle):
        self.burger.setBuns(bunStyle)
        return self
        
    def addPatty(self, pattyStyle):
        self.burger.setPatty(pattyStyle)
        return self
        
    def addCheese(self, cheeseStyle):
        self.burger.setCheese(cheeseStyle)
        return self
    
    # E por fim temos o método que retorna o hamburguer feito
    def build(self):
        return self.burger
    
myBurger = BurgerBuilder() \
            .addBuns("sesame") \
            .addPatty("chicken-patty") \
            .addCheese("cheddar") \
            .build()

myBurger.print()