# exercise, remove duplicate numbers from list
numbers = [2, 2, 4, 6, 3, 4, 6, 1]

# MY SOLUTION
numbers2 = numbers.copy()           # make a copy to work with
for num in numbers2:                # for each number in list
    while numbers2.count(num) > 1:  # while there is more than one
        numbers2.remove(num)        # remove the number
print(numbers)
print(numbers2)

# Mosh's SOLUTION
uniques = []                    # new list to store one of each number
for number in numbers:          # for each number in list
    if number not in uniques:   # check if it is not in uniques yet
        uniques.append(number)  # if not, append it
print(numbers)
print(uniques)

