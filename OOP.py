class Soda:
    def __init__(self, ingredient=None):
        if isinstance(ingredient,str):
            self.ingredient = ingredient
        else:
            self.ingredient = None
    def show_my_drink(self):
        if self.ingredient:
            print(f"Soda and {self.ingredient}")
        else:
            print("Just Soda")

drink1 = Soda()
drink2 = Soda('pineapple')
drink3 = Soda(5)
drink1.show_my_drink()
drink2.show_my_drink()
drink3.show_my_drink()

