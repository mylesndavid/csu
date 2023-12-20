# file to find the addition and subtraction of two numbers 

#function to add two numbers
def add(num1,num2):
    return f'the value of {num1} + {num2} is {num1+num2}'

#function to subtract two numbers
def sub(num1,num2):
    return f'the value of {num1} - {num2} is {num1-num2}'

#function to multiply two numbers
def mul(num1,num2):
    return f'the value of {num1} * {num2} is {num1*num2}'

#function to divide two numbers
def div(num1,num2):
    return f'the value of {num1} / {num2} is {num1/num2}'

print('Part 1\n---------------------\n')
#take both numbers as inputs
print('Two numbers to add then subtract')
num1 = int(input('first number: '))
num2 = int(input('second number: '))

#print the result of the computation
print(add(num1,num2))
print(sub(num1,num2))

print('\nPart 2\n---------------------\n')
#take both numbers as inputs
print('Two numbers to multiply and then divide')
num1 = int(input('first number: '))
num2 = int(input('second number: '))

#print the result of the computation
print(mul(num1,num2))
print(div(num1,num2))