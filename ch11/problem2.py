class Animals:
    def __init__(self,name):
        self.name=name
class Pets(Animals):
    def __init__(self, name,owner):
        super().__init__(name)
        self.owner=owner
class Dogs(Pets):
    def __init__(self, name, owner,breed):
        super().__init__(name, owner)
        self.breed=breed
    def bark(self):
        print(f"name: {self.name} says: Woof! Woof!")
d=Dogs("Buddy","Alice","German Shepard")
print(f"name: {d.name} , Owner name: {d.owner} , Breed: {d.breed}")
d.bark()