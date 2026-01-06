class Animal:

    def __init__(self, name):
        self.name = name

    def feature1(self):
        print(f"{self.name} have 4 legs")

    def feature2(self):
        print(f"{self.name} have 2 eyes")

    def feature3(self):
        print(f"{self.name} have a mouth")

class Dog(Animal):

    
    def dog_feature1(self):
        super().feature1()
        super().feature2()
        super().feature3()
        print(f"{self.name} can Bark!!")

    def dog_feature2(self):
        print(f"{self.name} is a pet animal")

d = Dog("Dogg")
# d.feature1()
# d.feature2()
# d.feature3()
d.dog_feature1()
d.dog_feature2()