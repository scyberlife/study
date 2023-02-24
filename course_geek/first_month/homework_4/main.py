data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
letters, numbers = [], [] # created two empty lists
for i in range (0, len(data_tuple)): # distributed the elements of the tuple into the lists using a loop
    if str(data_tuple[i]).isalpha() and data_tuple[i] != "True":
        letters.append(data_tuple[i])
    else:
        numbers.append(data_tuple[i])
numbers.pop(0) # removed 6.13 from the list
letters.append(letters[4]) # added an element to the end of the list to remove it later
letters.pop(4)
numbers.insert(1, 2) # inserted the number 2 between 1 and 3
numbers = sorted(numbers) # sorted the list
letters.reverse() # reversed the list
letters[1], letters[7] = 'G', 'c' # replaced two letters
numbers = [int(numbers[i]) ** 2 for i in range(len(numbers))] # squared each number in the list
print(f'Tuple letters - {tuple(letters)} \nTuple numbers - {tuple(numbers)}') # printed the tuples after converting them