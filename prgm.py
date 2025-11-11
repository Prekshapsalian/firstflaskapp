'''name = "yathika"  # no need to declare a type in Python
print(type(name))  # display datatype

name = input("enter your name: ")  # take input from user
print("hello", name)

try:
    age = int(input("enter your age: "))  # convert input to int
except ValueError:
    print("Please enter a valid integer for age.")
    raise SystemExit(1)

print(age)

if age >= 18:
    print("you are eligible to vote")
elif 0 <= age < 18:
    print("you are not eligible to vote")
else:
    print("enter valid age")

#loops

for i in range(10):
    print("hello world",i)
count=1
while count<10:
    print("hi",count)
    count+=1
'''
#to create list
fruits = ["apple", "banana", "cherry"]
print(fruits)
'''#to print one after another
for i in fruits:
    print(i)
#to access single element
print(fruits[1])  # prints 'banana'
print(fruits[-1])#to access last element
#to add new elememts to end of list
fruits.append("orange")
print(fruits)
print(len(fruits))#to find length of list
#to add element in particular position not at end
fruits.insert(2,"mango")
print(fruits)
#to delete element
fruits.remove("banana")
print(fruits)
#to remove last ele
fruits.pop()
#to delete element using index
del fruits[0] # fruits.pop(0)'''
#to clear entire list
fruits.clear()
print(fruits)
print(len(fruits))