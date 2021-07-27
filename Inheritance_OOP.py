
class Intersteller:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("Hey im {}".format(self.name))

    def survive(self):
        print("Hey im survive")


    def updateStrength(self, value):
        self.value= value


    def testing(self):
        print("am a little baby")


# INHERITENCE

class Inception(Intersteller):

    def Dream(self):
        print("amar ghumate eccha kore na")


Zahed=Intersteller("Full Stack Developer")
Mariam=Intersteller("Full Stack Developer")
Rafath=Inception("Mongo Expert")
Baby=Intersteller("Finally")
Alisha=Intersteller("For testing")


Zahed.introduce()
Mariam.introduce()
Rafath.Dream()
Baby.survive()
Alisha.testing()
