number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

i = 0

while i < len(number_list):
    if number_list[i] > 50:
        number_list.pop(i)
    else:
        i += 1

print (number_list)
