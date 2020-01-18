x = input()
y = input()
z = int(x) + int(y)
print(z)
print()
a = int(input('Enter another no: '))
b = int(input('Enter one more no: '))
c = a + b
print(c)
print()
calculator = eval(input("Enter an expression to calculate: "))
print(calculator)
print()




# #for command line arguments
# import sys
# p = int(sys.argv[1]) #bcoz argv[0] contains filename
# q = int(sys.argv[2])
# r = p + q
# print(r)




#using help() and _doc_ to print the docString of a function
#As every function should have a docString associated to it, explaining what it does rather than how it does
def my_function():
  """This function does nothing."""#this how u define docString
  return None

print("with help function: ")
print(help(my_function))
print()
print("with _doc_: ")
print(my_function.__doc__)

