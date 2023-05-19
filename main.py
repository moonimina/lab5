class Pizza:
    def __init__(self):
        self.dough = ''
        self.sauce = ''
        self.topping = ''

    def __str__(self):
        return f'тесто: {self.dough}, соус: {self.sauce}, начинка: {self.topping}'


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def getPizza(self):
        return self.pizza

    def buildDough(self):
        pass

    def buildSauce(self):
        pass

    def buildTopping(self):
        pass


class HawaiianPizzaBuilder(PizzaBuilder):

    def buildDough(self):
        self.pizza.dough = 'толстое'

    def buildSauce(self):
        self.pizza.sauce = 'белый'

    def buildTopping(self):
        self.pizza.topping = 'ананас+ветчина'


class SpicyPizzaBuilder(PizzaBuilder):

    def buildDough(self):
        self.pizza.dough = 'тонкое'

    def buildSauce(self):
        self.pizza.sauce = 'острый'

    def buildTopping(self):
        self.pizza.topping = 'пепперони+салями'


class SeafoodPizzaBuilder(PizzaBuilder):

    def buildDough(self):
        self.pizza.dough = 'тонкое'

    def buildSauce(self):
        self.pizza.sauce = 'томатный'

    def buildTopping(self):
        self.pizza.topping = 'креветки+лосось'


class PizzaDirector:

    def __init__(self, pizzaBuilder: PizzaBuilder):
        self.pizzaBuilder = pizzaBuilder

    def makePizza(self):
        self.pizzaBuilder.buildDough()
        self.pizzaBuilder.buildSauce()
        self.pizzaBuilder.buildTopping()

    def getPizza(self):
        return self.pizzaBuilder.getPizza()


director = PizzaDirector(SeafoodPizzaBuilder())
director.makePizza()
pizza = director.getPizza()
print(pizza)
