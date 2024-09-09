Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> Peeps{"Mama" : 52,
	  
SyntaxError: invalid syntax
>>> Peeps{"Mama" : 52, "Phade" : 31, "Kakolz" : 29, "Weezy" : 25, "Yanz" : 20}
	  
SyntaxError: invalid syntax
>>> Peeps = {"Mama" : 52, "Phade" : 31, "Kakolz" : 29, "Weezy" : 25, "Yanz" : 20}
	  
>>> Peeps = {"Mama" : 52, "Phade" : 31, "Kakolz" : 29, "Weezy" : 25, "Yanz" : 20}
	  
>>> 
	  
>>> 
	  
>>> for name, age in Peeps.items() :
	  print("My name is " + name + " , I am " + str(age) + " years old")

	  
My name is Mama , I am 52 years old
My name is Phade , I am 31 years old
My name is Kakolz , I am 29 years old
My name is Weezy , I am 25 years old
My name is Yanz , I am 20 years old
>>> 
	  
>>> 
	  
>>> Lamba = [2,3,4,5,6,7,8]
	  
>>> for index, number in enumerate(Lamba) :
	  print{index + ": " + str(number))
	  
SyntaxError: invalid syntax
>>> 
	  
>>> for index, number in enumerate(Lamba) :
	  print(index + ": " + str(number))

	  
Traceback (most recent call last):
  File "<pyshell#19>", line 2, in <module>
    print(index + ": " + str(number))
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 
	  
>>> 
	  
>>> 
	  
>>> for index, number in enumerate(Lamba) :
	  print("index " + str(index) + ": " + str(number))

	  
index 0: 2
index 1: 3
index 2: 4
index 3: 5
index 4: 6
index 5: 7
index 6: 8
>>> 
	  
>>> 
	  
>>>  for index, number in enumerate(Lamba) :
	  print("index " + str(index + 1) + ": " + str(number))
	  
SyntaxError: unexpected indent
>>> 
	  
>>> for index, number in enumerate(Lamba) :
	  print("index " + str(index + 1) + ": " + str(number))

	  
index 1: 2
index 2: 3
index 3: 4
index 4: 5
index 5: 6
index 6: 7
index 7: 8
>>> 
