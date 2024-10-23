from classes_pkg.shape import Shape

class Rectangle(Shape):
    def __init__(self,name,color,length,width):
        super().__init__(name,color)
        self.length=length
        self.width=width
    #defining a new function
    def print_info_rectangle(self):
        super().print_info()
        print(f"the length is {self.length} and the width is {self.width}")
        
    #overriding the parent's function
    def print_info(self):
        super().print_info()
        print(f"the length is {self.length} and the width is {self.width}")
    
    #polymorphism
    def calculate_surface(self):
        return self.width*self.length