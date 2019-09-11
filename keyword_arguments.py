# Function Parameters with keyword arguments


def greet_user(first_name, last_name=''):       # functions take 'parameters'
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')


print("Start")
greet_user("Jeremy", "Stewart")     # function calls send 'arguments' to function 'parameters'
greet_user("John", last_name="Smith")  # keyword arguments should always come after positional arguments
greet_user("Mary")
print("Finish")