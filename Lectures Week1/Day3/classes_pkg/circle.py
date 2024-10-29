from classes_pkg.shape import Shape

class Circle(Shape):
    def __init__(self,name,color,rayon):
        super().__init__(name,color)
        
        self.rayon=rayon
    
    def calculate_surface(self):
        return self.rayon*self.rayon*3.14
    def print_info(self):
        super().print_info()
        print(f"The rayon is {self.rayon}")