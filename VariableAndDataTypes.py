# Variable is a name given to a memory location.
# It is a container to store a value.
# Keywords are reserved words in python.

# Variable rules:
# ----> VALID :
#         a
#         A
#         _HI
#         _hi
#         h_25
# ----> INVALID
#         1fd
#         @hum
#         kite-sky

# PYTHON IS CASE-SENSITIVE
# UPPER CASE & LOWER CASE are considered as different variables.

a = 'Sheetal'               #string ' or " any
print(a+' How are you?')    # Here '+' acts as a concatenation operator
print(type(a),'\n')         #to check the type of variable

a = 345                     #integer number
print(a+5)                  # here + adds the value to a cz it is a int value.
print(type(a),'\n')
print("================")

# To use '+' operator make sure both the values on each side are of same data type.


# Triple quotes can be used in assigning a variable when want to use both ' and " quotes in a sentence.
sent = '''Hello, what's the "occasion" '''
print(sent)

sent = '''Hello, what's the "occasion" today? '''
print(sent)


#printing multiline
hi = '''hi
wassup?'''
print(hi)
print(type(hi),'\n')

# Boolean opeartor
c = True
print(c, 'Printed')
print(type(c),'\n')

# Comma can concatenate any type of data together. Any number of ',' can be added.
# '+' concatenates only similar type of data.
print(100 , "Hundred",'\n')

# None DATATYPE
n = None
print(n)
print(type(n))

