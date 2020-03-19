# Python Cheatsheet

This is a cheat sheet prepared and used by myself in Digital world.

## Contents
  1) Strings
  1.5) Useful Imports
  2) Lists (in construction)
  3) Dictionaries (in construction)
  4) OOP (in construction)


## Chapter 1 : Strings
### 1.1 String Methods/Functions
stringname.method(parameters) to do whatever the description mentions

Commands:
```
Method      Parameters Description

upper       none       Returns string in all uppercase
lower       none       Returns string in all lowercase
capitalise  none       Returns string with first letter capitalised only
strip       none       Returns string with all spaces " " removed
split       itemname   Returns string, split by itemname with a comma
count       itemname   Returns the number of occurrences of item
replace     old, new   Replaces all occurrences of old substring with new
find        itemname   Returns the leftmost index where the substring item is found, or -1 if not found
```
other useful functions that I do not have the time to google, worry about, or include:

Commands:
```
Print
Len
Range
List
Sorted
Map
Lambda
Str
Repr
In
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


## 1.5 Useful Imports

import time

```
Method    Parameters      Description

time      None            Gets time since epoch (the start of universe)
localtime None
asctime   None            gives you current clock time on ur bottom right screen

```


time.time() usage

```
usage: set a start time and also an end time. this allows u to time a certain amt of actions in ur code.

import time
def stopwatch_fn:
  start_time = time.time()
      - YOUR CODE HERE -
  end_time = time.time()
  total_time_taken = start_time - end_time
  return total_time_taken
```


## Dictionaries cr @methyldragon
### 3.10 Dictionaries

[go to top](#top)

Dictionaries are made up of values with a **UNIQUE** key for each value! It's basically a keyed list.

> You can't join them like you can with lists though!

```python
# Define a dictionary using {}
species_dictionary = {"Bob" : "Human",
                     "methylDragon" : "Dragon",
                     "haojun" : "Snake"}
# The things to the left of the colon are the keys, and the ones on the right are the values

# To call an entry by key
species_dictionary["methylDragon"] # Returns Dragon

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
### OOP
