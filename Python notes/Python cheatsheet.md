# Python Cheatsheet

This is a cheat sheet prepared and used by myself in Digital world.  
Author : BruttherJOE

## Contents
  0) Useful Imports  
    0.1) import time  
    0.2) import libdw  
    0.3) import math  
    0.4) import numpy
  1) Strings  
  2) Lists (in construction)  
    2.1) List Commands  
    2.2) Enumerate  
  3) Dictionaries (in construction)  
  4) OOP (in construction)  
    4.25) #__init__
  5) Misc  
    5.1) exception handling : try, except, finally  
    5.2) debugging  
    5.3) confusing arithmetic operators

## Chapter 0 : Useful Imports  
  ### Introduction to imports
  will update when there is time.
  
  ___________________
  ### import time
  > time is useful for timing things in your program.  

time.*method* (parameters) to do **Description**


Method  |  Parameters  |    Description
----------|------------|-----------------
time      |None        |    Gets time since epoch (the start of universe)
localtime |None        |    returns current year, month, day in month, hour, min, sec, wday, yday... as a list
asctime   |None        |    gives you current clock time on ur bottom right screen. returns as a str. splittable by spaces.

  
time.time() usage  

usage: set a start time and also an end time. this allows u to time a certain amt of actions in ur code.
```python
import time
def stopwatch_fn:
  start_time = time.time()
      - YOUR CODE HERE -
  end_time = time.time()
  total_time_taken = start_time - end_time
  return total_time_taken
```
___________________________
### import libdw

#### Introduction
this package was written by Oka Kurniawan, a professor from SUTD.  
For windows, in anaconda prompt, or terminal on linux/IOS, to install, do  
`pip install libdw`  
this will install the package.  

##### Documentations
the full list is too long and there is already good documentations on it.  
Here is the link : https://people.sutd.edu.sg/~oka_kurniawan/10_009/doc/html/libdw.html

I will still be compiling the most useful stuff from this package in a table on this notes though, so stay tuned!  

______________________________
### import math  
advanced arithmetic operations and variables  
  
`math.e` euler number  
`math.pi` pi  
_________________________________________  

### import numpy
library that involves handling of numbers
#### np array
  `np.array`  
  this creates an array. usually done by a list of lists. these lists need to be same length.
  
  ```python
  m = np.array([1,2,3],[4,5,6],[7,8,9])
  print(m)
  ```
  ```
  [[1 2 3]
   [4 5 6]
   [7 8 9]]
   ```
_____________________________________
#### np array shape
   `[arrayname].shape`  
   this command will tell you the x and y lengths of the array respectively. You can store this in a variable.
   ```python
   n = m.shape
   print n
   ```
   `(3,3)`
 
  
________________________
## Chapter 1 : Strings  
  
[go to top](#top)  

### 1.1 String Methods/Functions
stringname.method(parameters) to do whatever the description mentions

Commands:

Method  |    Parameters| Description
--------|--------------|---------------
upper    |   none     |  Returns string in all uppercase
lower    |   none     | Returns string in all lowercase
capitalise | none     | Returns string with first letter capitalised only
strip    |  none     | Returns string with all spaces " " removed
split    |  itemname | Returns string, split by itemname with a comma
count    |  itemname | Returns the number of occurrences of item
replace  |  old, new | Replaces all occurrences of old substring with new
find     |  itemname | Returns the leftmost index where itemname is found, or -1 if not found

other useful functions that I do not have the time to google, worry about, or include:

Commands:  

```
Method                   Description
____________________________________________________________
Print                    Print ur mom
Len                      (len(ls) to get length of list)
Range
List
Sorted
Map
Lambda
Str
Repr
input
enumerate
file
type()
```
### 1.2 String format() Method
```
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))
_________________________________
For only 49.00 dollars!
```



## CHAPTER 2 - LISTS  
  
[go to top](#top)

list commands
listname.*Method*(Parameters) to do Description

```
Method    Parameters     Description
append    itemname       adds itemname to listname
insert    index,itemname adds itemname to listname at index position
index     itemname       returns index of position of itemname
reverse   none           reverses the list


```


For the below, *Method*(listname) to do Description

```
Method       Description
len          returns length of the list in int form
max          returns max of the list
min          returns min of the list
sorted       returns the list, sorted from smallest value to highest.  
             can be used for int/str. str from a-z. opt param (reverse)
```

### 2.2 Enumerate
  
Enumerate allows us to loop over a list and still have a counter.

```python
my_list = ['apple', 'banana', 'grapes', 'pear']
for c, value in enumerate(my_list, 1):
    print(c, value)
```

```
 Output:  
 1 apple  
 2 banana  
 3 grapes  
 4 pear  
```
  
you may also specify at which index you want to start stuffing it from. This is an optional argument.  
  
```python
my_list = ['joe', 'valent', 'iggy', 'dody']
counter_list = list(enumerate(my_list, 100))
print(counter_list)  
---------------------------
# Output: [(100, 'joe'), (101, 'valent'), (102, 'iggy'), (103, 'dody')]
```
#when I have time, I need to redo this part to make it clearer.
[go to top](#top)

## CHAPTER 3 - DICTIONARIES cr @methyldragon
### 3.10 Dictionaries  
  
[go to top](#top)

Dictionaries are made up of values with **UNIQUE** keys for every value.  
It's basically a keyed list.  
Keys are immutable. This means that they cannot be changed.  
This is because the value will get confused and kill itself.  

> You can't join dictionaries like you can with lists  

Dictionaries are defined by {}.  
This is an empty dictionary :  
`dictionary = {}`

```python
dictionary = {"jack" : "good person",
              "apple" : "fruit",
              "haojun" : "Snake"}
```

```
# The things to the left of the colon are the keys, and the ones on the right are the values

# To call an entry by key
Method                                Description
species_dictionary["methylDragon"]    Returns Dragon

# To reassign values (Think lists, but with keys instead of indexes!)
species_dictionary["haojun"] = "Human"

# Empty dictionary
empty_dictionary = {}
```

#### **Dictionary Comprehensions**

```python
# Just some examples for reference
# {key:value for item in list if conditional}

name_list = ["a", "b", "c", "d", "e"]
num_list = [1, 2, 3, 4, 5]

dictionary = {x : y for x, y in zip(name_list, num_list)}
```



### 3.11 Dictionary Methods  
[go to top](#top)

dictionaryname.**method**(**parameters**) to perform **Description**
```
Method   Parameters      Description
get      keyname         returns the itemname in dictionary that is associated with keyname. If no value found, return None
items    none            gets a list of key-value pairs
keys     none            gets a list of keys
values   none            gets a list of values
update   {"Key":"Value"} add a key (merges another dictionary)
```

```python
# List functions work!
del dictionary_name[<key>]
len()
pop(key)
clear() # Empties the entire dictionary

# Add multiple keys (As above, update merges another dictionary)
species_dictionary.update({"Key_1":"Value_1", "Key_2":"Value_2"})

# Add a key (alternative) (Though it isn't an explicit method call...)
species_dictionary["Smaug"] = "Dragon"

# Set a default response to a particular key query if the key is not found
species_dictionary.setdefault("methylDragon", "rad_dragon")
species_dictionary.setdefault("Toothless", "dumb_dragon")

species_dictionary["methylDragon"] # returns "Dragon" (as the key was found)
species_dictionary["Toothless"] # returns "dumb_dragon"
```

Example: Putting it all together!

```python
# Return a list of numbers that appear most frequently in an input list
# Show multiple if tied
# Eg. Input: [1, 1, 2, 2, 3]
# Output: [1, 2]

def most_frequent(lst):
    count_dict = {}
    for i in lst:
        if count_dict.get(i) == None:
            count_dict.update({i : lst.count(i)})
    return [x for x in count_dict.keys() if count_dict[x] == max(count_dict.values())]
```

## Chapter 4  
[go to top](#top)
### OOP (introduction)
an introduction will be placed here when i has dat time


  ### 4.1 Classes  
  ```python
  class dog:
    pass
  ```
  > In python 2, classes require a parameter _(object)_. just follow this if on python 3.
  
  ### 4.15 Instances / Objects
  An instance or object is a copy of the class with the actual values, such as a snake named haojun who has the functions such as slither()  
  
  An email account is a perfect example of an instance.


  ### 4.2 Special Methods
Some class methods have names starting and ending with a double underscore. These methods allow a special syntax in the program and are called special methods. The constructor __init__ is one example.  

List of special methods:
```
  __init__
  __call__
```

  ### 4.25 __init__ Special Method
The ```__init__``` method is used to initialise attributes (characteristics) that a class of things may have. 
For example, people in a "class" have names. all inits have "self" as an argument
(the input variables between the brackets after init). 
Self means its referring to itself. (an object's instance)

```python
class F04:

    # Initializer / Instance Attributes
    def __init__(self, name, age): #inputs
        #set input name, age to be related to an instance
        self.name = name 
        self.age = age

```

> Note : You never have to call the init function, its auto called when you have new inputs / instances

## Chapter 5 - Misc  
[go to top](#top)


diff btw frm math imp * and imp math  



### Chapter 5.1 - Exception Handling  

#### Introduction
When an error occurs, python will stop script and return an error message.  
Sometimes, we still want to run the script even though there is an error.  
Hence, we debug by introducing __Exception Handling__.

This does not always have to be for debugging, but it is usually for debugging.  
This is mostly seen in robotics projects where there may be exceptions in I/O.  
In the case of robotics, sometimes, sensors do not return information.  

#### Execution
`try` Block will let you test a block of code for errors  
`except` Block will let you handle the error  
`finally` will let you execute code regardless of try and except blocks  

#### Explanations
When `try` block raises an error, the `except` block will be executed  
After `try` and `except`, regardless of whether `try` or `except` was executed, `finally` will be executed.

`try`, `except`, `finally`, should all be on the same indentation. should. not too sure myself.

Other keywords that will be documented next time :  
`else`  
`raise`  


### Chapter 5.3 Confusing arithmetic operators  

[go to top](#top)  

This chapter is here because I have forgotten these two before.  
  
`%` the modulus function  
Divides and returns the value of the remainder.
  
`//` the floor function  
Divides and returns the integer value of the quotient. It throws away the decimal digits of the answer.
