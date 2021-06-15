#Assigning Sting to variable:
Hours = "thirty"
print(Hours)

#Indexing using Strings:
Days = "Thirty one days"
print(Days[10])

#How to print the particular character from certain text?
Challenge = "Guido Van Rossum"
print(Challenge[7:10])

#Print the length of Character:
Challenge = "Guido Van Rossum"
print(len(Challenge))

#String Concatenation – Joining two strings
a = "30 Days"
b = "30 hours"
c = a + b
print(c)

#Adding space during concatenation
a = "30 Days"
b = "30 hours"
c = a + " " + b
print(c)

#casefold() - Usage
text = "Thirty one days and Thirty one hours"
x = text.casefold()
print(x)

text = "east west north south"
y = text.capitalize()
print(y)

text = "DON’T TROUBLE TROUBLE UNTIL TROUBLE TROUBLES YOU"
z = text.find('u')
print(z)

text = "DON’T TROUBLE TROUBLE UNTIL TROUBLE TROUBLES YOU"
a = text.isalpha()
print(a)

text = "DON’T TROUBLE TROUBLE UNTIL TROUBLE TROUBLES YOU"
b= text.isalnum()
print(b)
