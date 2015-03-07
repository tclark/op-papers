class Person:

    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last
    
    def change_name(self, first, last):
        self.first_name = first
        self.last_name= last

    def increment_age(self):
        try:
            self.age += 1
        except AttributeError:
            self.age = 1
        return self.age

    def kill(self):
        self.dead = True
