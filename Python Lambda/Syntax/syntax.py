#lambda arguments : expression
#The expression is executed and the result is returned:

#Add 10 to argument a, and return the result:

x = lambda a : a + 10
print(x(5))

#Lambda functions can take any number of arguments:


#Multiply argument a with argument b and return the result:

x = lambda a, b : a * b
print(x(5, 6))

#Summarize argument a, b, and c and return the result:

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))