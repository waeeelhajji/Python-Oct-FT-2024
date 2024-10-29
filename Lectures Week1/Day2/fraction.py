class Fraction:
    #class attributes
    list_of_fraction=[]
    #constructor
    def __init__(self,numerator,denominator):
        self.numerator=numerator
        self.denominator=denominator
        Fraction.list_of_fraction.append(self)
    
    def print_info(self):
        print(f"{self.numerator}/{self.denominator}")
        return self
    
    def multiply_by_half_same_fraction(self):
        self.numerator=self.numerator
        self.denominator=self.denominator*2
        return self


    def multiply_by_half(self):
        new_numerator=self.numerator*1
        new_denominator=self.denominator*2
        new_fraction=Fraction(new_numerator,new_denominator)
        return new_fraction
    
    #association between two classes
    def multiply_by_fraction(self,another_fraction):
        new_numerator=self.numerator*another_fraction.numerator
        new_denominator=self.denominator*another_fraction.denominator
        new_fraction=Fraction(new_numerator,new_denominator)
        return new_fraction
        
    @classmethod
    def list_all_the_fractions(cls):
        for i in range(len(cls.list_of_fraction)):
            cls.list_of_fraction[i].print_info()
    
    @staticmethod
    def add_two_numbers(num1,num2):
        return num1+num2
    
    
fraction_one=Fraction(1,3)
fraction_two=Fraction(4,9)
fraction_three=fraction_two.multiply_by_half()

# fraction_one.multiply_by_half_same_fraction()
# fraction_one.print_info()
# fraction_three.print_info()
# fraction_four=fraction_one.multiply_by_fraction(fraction_two)
# #fraction_four.print_info()
# Fraction.list_all_the_fractions()
#print(Fraction.add_two_numbers())
fraction_two.print_info()
fraction_two.multiply_by_half_same_fraction()
fraction_two.print_info()
#Chaining methods
fraction_two.print_info().multiply_by_half_same_fraction().print_info()


