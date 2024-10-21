
#debugging
def add_numbers_in_list(data):
    print('im into the function...')
    print(data)
    total=0
    for i in range(len(data)):
        print(data[i],i)
        total=total+data[i]
        print("++++")
        print(total)
    return total
my_data=[5,4,3,2,1]
print(add_numbers_in_list(my_data)) #15