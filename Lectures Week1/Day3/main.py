# from classes_pkg.shape import my_shape,print_info

# print(my_shape)
# print_info()

from classes_pkg.shape import Shape
from classes_pkg.rectangle import Rectangle
from classes_pkg.circle import Circle

my_shape=Shape("My shape","White")
circle_one=Circle("Circle one ","yellow",5)
# my_shape.print_info()

rectangle_one=Rectangle("Rectangle One","Blue",10, 4)

# rectangle_one.print_info()
# print("*"*10)
# rectangle_one.print_info_rectangle()
# print(rectangle_one.calculate_surface())

# print(circle_one.calculate_surface())
#circle_one.print_info()
# your_message=input("please insert your comment")

# print(f"your message was {your_message}")


#inputs outputs
list_of_rectangles=[]
print("*********MENU OF OPTIONS**********")
print("1)Add a rectangle to the list")
print("2)list all the rectangles")
print("5)Terminate the program")
option=input("Please select an option:")
while option !="5":
    if option=="1":
        rectangle_name=input("please enter the name of the rectangle")
        rectangle_color=input(f"please enter the color of {rectangle_name}")
        rectangle_length=input(f"please enter the length of {rectangle_name}")
        reclangle_width=input(f"please enter the width of{rectangle_name}")
        new_rectangle=Rectangle(rectangle_name,rectangle_color,int(rectangle_length),int(reclangle_width))
        new_rectangle.print_info()
        list_of_rectangles.append(new_rectangle)
    if option=="2":
        for rectangle in list_of_rectangles:
            rectangle.print_info()
            print("*"*10)
    print("*********MENU OF OPTIONS**********")
    print("1)Add a rectangle to the list")
    print("2)list all the rectangles")
    print("5)Terminate the program")
    option=input("Please select an option:")