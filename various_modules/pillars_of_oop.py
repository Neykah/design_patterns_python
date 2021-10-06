class Cat:
    ...

class Dog:
    ...


bag = [Cat(), Dog()]

for animal in bag:
    animal.make_sound()

