'''
my_list = [1, 2, 3, 4, 5]
largest_number = max(my_list)
print(largest_number)
'''

##the code above and below finds the largest number in a list.


my_list = [1, 2, 3, 4, 5]

largest_number = my_list[0]

for number in my_list:
    if number >largest_number:
        largest_number = number

print(largest_number)
