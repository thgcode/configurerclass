from __future__ import absolute_import, division, print_function, unicode_literals

from configurer import Configurer
class Player(Configurer):
    def __init__(self):
        self.objects = []
        processed = self.load("example.ini")
        for k, v in processed.items():
            if k.startswith("obj"):
                self.objects.append(v)
                delattr(self, k) # Need to think in a way to handle this

    def print_stats(self):
        print("%s is level %d, his died flag is %d and his objects are:" % (self.name, self.level, self.died))
        for o in self.objects:
            print(o)

    def save_data(self):
        return self.save("another.ini", ["name", "level", "died"])

p = Player()
p.print_stats()
p.save_data()
