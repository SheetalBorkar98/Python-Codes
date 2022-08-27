a = "Hello, "
b = ". How may I help you?"
c = "Sheetal"
d = a+c+b
print(d)

# OUTPUT :
# Enter name : Sheetal
# Hello, Sheetal. How may I help you?

# SLICING
x = d[7:15]             # First index is included and Last is excluded
print(x)

#iNDEXING
print(d[-7])
print(d[7])
print(d[0:])
print(d[0:0])
print(d[-6])
print(d[0:35])
print(len(d))

print(d[-15:-7])

story = "hi hello fella hi"
print(len(story))
print(story.endswith("o fella"))
print(len("hi"))
print(story.count("F"))
print(story.count("f"))             #occurance of character
print(story.count("el"))
print(story.count("fella"))

print(story.capitalize())
print(story)

print(story.find("hi"))              # finds the first occurance of the word, returns first index

print(story.replace("hi","heya"))       #Replaces all the occurance in the string
print(story)

print("i am a \n girl")
print("i am a \t girl")
print("i am a \' girl")
print("i am a \ girl")





