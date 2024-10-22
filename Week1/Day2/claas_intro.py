class Table:
    #Constructor
    def __init__(self,owner,shape,color_one,color_two,material,hight,width):
        #Attributes (caracteristics)
        self.shape=shape
        self.color_one=color_one
        self.color_two=color_two
        self.material=material
        self.owner=owner
        self.hight=hight
        self.width=width
        
    
    #Create a method (function inside a class), instance method
    def print_info(self):
        print(f"Hi, I'm {self.owner} my table is {self.shape}, its color is {self.color_one} and {self.color_two}, it's made of {self.material}")
    
    def study(self):
        print("I'm studying on my table")
    
    def calculate_diametre(self):
        diametre = (self.hight+self.width)*2
        return diametre
    
    def calculate_surface(self):
        surface=self.hight*self.width
        return surface
    
    def calculate_surface_of_both(self,second_surface):
        surface=self.calculate_surface()+second_surface
        return surface
    
#instanciation an object of the class Table.Create an instance
alex_table=Table("Alex","rectangular","white","red","wood",1.5,2) 
martha_table=Table("Martha","round","brown","silver","plastic",3,5)
# print(alex_table.shape,alex_table.color,alex_table.material)  

# print(martha_table.shape,martha_table.color,martha_table.material)

alex_table.print_info()
martha_table.print_info()
alex_table.color="Black"
alex_table.shape="triangle"
alex_table.material="iron"
alex_table.print_info()
alex_table.study()
print(alex_table.calculate_diametre())
print(martha_table.calculate_diametre())
print(alex_table.calculate_surface_of_both(martha_table.calculate_surface()))