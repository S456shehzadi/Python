
#print statements
print("Hello, world!")

#if statements
x=1
#commenting in python
if x>0:
    print("True")

txt = input("Type Something to test this out: ")
print(txt)

#printing multiple statments in a line
s1 = "statement1"
s2 = "statement2"

print(s1);print(s2)

#indentation

x=1
if x>0:
 print("This Statement has a single space indentation")

x=2
if x>0:
    print("This Statement has a single tab indentation") 

x=5
if x==5:
    print("This Statement has a single space+tab indentation") 


#  data types and type casting 
a = 1110
type(a)
print(type(a))

b = 12.5
print(type(b))

c= -4
print(type(c))

d = 0
print(type(d))

y = complex(1,2)
print(type(y))
print(y)

x = 1+4j
print(type(x))

                #BOOLEAN
x = True
print(type(x))
y= False
print(type(y))

                #strings
str1 = "Hello"
print(str1)
str2 = "Python"
print(str2)
str3 = "day's"
print(str3)

               #Special chatacters in python
print("this is backslash (\\) mark.")
print("this is tab \t key.")  
print("this is newline \n key.")  
print("These are single quotes \'Single Quote\'") 
print("These are double quotes \"Double Quote\"")  

               #String indices and accessing string elements

string1 = "PYTHON TUTORIAL"
print(string1[0])
print(string1[14])
print(string1[-15])
print(string1[-1])
 

               #LISTS in python
list1 = {12,13,14,15}
print(list1)

list2 = {"RED","BLUE","GREEN","WHITE"}
print(list2)

list3 = {"Red",13,14,15}
print(list3)



                  #CONDITIONAL STATEMENTS
a=2
b=5

if a>b:
   print("True")
else:
   print("False")


if a== b:
   print("Equivalent")
if a!=b:
   print("Not Equivalent")   