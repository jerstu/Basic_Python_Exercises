numbers = [5, 2, 1, 5, 7, 4]
# numbers.append(20) # append 20 to and of list
# numbers.insert(0,10) # insert 10 at index 0
# numbers.remove(5) # remove first instance of 5 from list
# numbers.pop() # remove last item from list

print(numbers.index(5))  # return index of first instance of 5
print(50 in numbers)  # return boolean, in operator checks for existence of item in object
print(numbers.count(5))  # return number of occurrences
numbers.sort()  # sorts in ascending order
numbers.reverse()  # reverses list
numbers2 = numbers.copy()
print(numbers)
