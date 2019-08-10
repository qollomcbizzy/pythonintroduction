class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(self.name, "he is talking")


person1 = Person('John')
person1.talk();
