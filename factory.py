class Burger:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def print(self):
        print(f"Ingredients:", *self.ingredients, sep="\n ")

class BurgerFactory:
    def createCheeseBurguer(self):
        ingredients = [
            "bun",
            "cheese",
            "beef-patty",
            ]
        
        return Burger(ingredients)
    
    def createDeluxeCheeseBurguer(self):
        ingredients = [
            "bun",
            "tomatoe",
            "lettuce",
            "cheese",
            "beef-patty",
            ]
        
        return Burger(ingredients)
    
    def createVeganBurguer(self):
        ingredients = [
            "bun",
            "special-sauce",
            "vegie-patty",
            ]
        
        return Burger(ingredients)
    
if __name__ == "__main__":
    burguer_factory = BurgerFactory()
    cheeseburguer = burguer_factory.createCheeseBurguer()
    deluxe_cheeseburguer = burguer_factory.createDeluxeCheeseBurguer()
    vegan_burguer = burguer_factory.createVeganBurguer()

    cheeseburguer.print()
    deluxe_cheeseburguer.print()
    vegan_burguer.print()