name = input('What is your name?') # input takes a prompt, which needs to be a string
print(f'Hello {name}!') #output, prints the color given to the console

if name == "Justin":
    print("Hey! That's my name too!")


print('*******************************************************************')    

count = 10
while count > 0:
    name = input('What is your name?')
    print(f'Hello {name}!')
    count -= 1
print("It was nice to meet you all.")


print('*******************************************************************')


count = 10
unique_names = []
while count > 0:
    found = False
    name = input('What is your name?')
    for unique_name in unique_names:
        if name == unique_name:
            found = True
            break 
    if found:
        print("Name already in use")
        continue
    print(f'Hello {name}!')
    if name == "Justin":
        print("Hey! That's my name too!")
    unique_names.append(name)
    count -=1
print("It was nice to meet you all.")
