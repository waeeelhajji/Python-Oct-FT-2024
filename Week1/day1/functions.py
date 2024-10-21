

# in js function theNameOfTheFunction(parm...){}
def my_function(a,b):
    #pass
    total=a+b
    return total

my_total=my_function(7,8)
print(my_total)

#default parameters
def add_two_numbers(num1=0,num2=0):
    total=num1+num2
    return total
#no arguments are given
print(add_two_numbers())
#first argument is given
print(add_two_numbers(24))
#the second parameter is given
print(add_two_numbers(24,45))



    