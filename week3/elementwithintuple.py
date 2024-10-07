
my_tuple = (10, 20, 30, 40, 50, 'apple', 'banana')

def element_exists(element, tup):
    return element in tup

element_to_check = 30
if element_exists(element_to_check, my_tuple):
    print(f"{element_to_check} exists in the tuple.")
else:
    print(f"{element_to_check} does not exist in the tuple.")

element_to_check = 'orange'
if element_exists(element_to_check, my_tuple):
    print(f"{element_to_check} exists in the tuple.")
else:
    print(f"{element_to_check} does not exist in the tuple.")
