# my_shape="rectangle"
# def print_info():
#     print("Hello There")
class Shape:
    #constructor
    def __init__(self,name,color):
        self.name=name
        self.color=color
        
    def print_info(self):
        print(f"The name is {self.name} and the color is {self.color}")
    
    #abstraction
    def calculate_surface(self):
        raise NotImplementedError