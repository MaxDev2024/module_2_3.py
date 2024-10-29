my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
my_list.remove(0)
initial_value = 0
positive_value = []

while initial_value < len(my_list):
    if my_list[initial_value] < 0:
        break
    positive_value.append(my_list[initial_value])
    print(my_list[initial_value])
    initial_value += 1