# Function Parameters


def greet_user(first_name, last_name=''):       # functions take 'parameters'
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')


print("Start")
greet_user("Jeremy", "Stewart")     # function calls send 'arguments' to function 'parameters'
greet_user("Mary")
print("Finish")