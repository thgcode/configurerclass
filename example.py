from configurer import Configurer
class Player(Configurer):
    def __init__(self):
        self.objects = []
        unknown = self.load("example.ini", "player", P_INTS, P_STRINGS, P_BOOLEANS)
        for k, v in unknown.iteritems():
            if k.startswith("obj"):
                self.objects.append(v)

    def print_stats(self):
        print "%s is level %d, his died flag is %d and his objects are:" % (self.name, self.level, self.died)
        for o in self.objects:
            print o

    def save_data(self):
        return self.save("another.ini", "player", P_INTS, P_STRINGS, P_BOOLEANS)

P_INTS = ["level"]
P_STRINGS = ["name"]
P_BOOLEANS = ["died"]
p = Player()
p.print_stats()
p.save_data()
