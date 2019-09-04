class Snake:
    def __init__(self, name):
        self.name = name

    def change_name(self, name):
        self.name = name


class Rocket:
    def __init__(self, name, distance):
        self.name = name
        self.distance = distance

    def launch(self):
        return "{rocket} a recorrido {km}km".format(rocket=self.name, km=self.distance)


class MarsRover(Rocket):
    def __init__(self, name, distance, maker):
        Rocket.__init__(self, name, distance)
        self.maker = maker

    def get_maker(self):
        return "{rocket} fue lanzado por {maker}".format(rocket=self.name, maker=self.maker)


class MarsRoverComp(Rocket):
    def __init__(self, name, distance, maker):
        self.rocket = Rocket(name, distance)
        self.maker = maker

    def get_maker(self):
        return "{rocket} fue lanzado por {maker}".format(rocket=self.rocket.name, maker=self.maker)


# Ejemplo basico
snake = Snake("python")
print(snake.name)
snake.change_name("anaconda")
print(snake.name)

# Ejemplo con herencia simple y herencia compuesta
x = Rocket("simple rocket", 20)
y = MarsRover("mars over", 30, "ISRO")
z = MarsRoverComp("mars over 2", 35, "XXXX")
print(x.launch())
print(y.launch())
print(y.get_maker())
print(z.rocket.launch())
print(z.get_maker())
