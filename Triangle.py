class Triangle:
    def _init_(self, base, height):
        self.base = base
        self.height = height
    def calculate_area(self):
        area = (1/2)*self.base*self.height
        print(area)

t1 = Triangle(10,20)
t1.calculate_area

t2=Triangle(20,30)
t2.calculate_area()
