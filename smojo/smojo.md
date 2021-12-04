# SMOJO

#### ⬛ Basic housekeeping

1) smojo is left to right
2) everything is either a literal (number, text, objects ; a variable) or words (actions ; a command)

3. Literals and words need spaces



#### ⬛ Why chatbot

- conversational application


- makes books webs, char, come allive

- allow people to consume info in an easy and interactive way




#### ⬛ Applications

- e commerce

- education

- retail /fnb

- advisory services (where to go)



#### ⬛ What makes chatbot useful

- Good chatbots has to guide the user

- active role in information discovery
- serves to reduce information overload
- can complement website or app
- serves to reduce friction in user actions by providing more info to users



#### ⬛ Examples

- chatbot.university





Chatbot challenge 

SG APIS to build chatbot

mapping data - 2d map



build chatbots for citzen services (where to eat, how to get there)

4:35









#### Judging criteria

usefullness : recognise user's intent and respond accurately

engaging : keep user engaged and want to interact further

design :uiux

informative : ability to educate users







#### ⬛ 2 kinds of chatbots

- Stateless

  > cannot remember the past

- Stateful

  > can remember the past











### ⬛ Types and Things



types are like the groups (lists, dictionaries)

things are the things inside the umbrella term 'types'

```smojo
@: animal food 					//@ symbol creates types

animal : chicken, dog, cat
food : cheese apple banana
```



### ⬛ Templates : 

basically comparing strings

```
@: likes
likes: apple oil metal

Q: like $likes
// $ sign takes the types 
A: Yes, I do.
```

templates can consist of multiple Q and A and all of them must have a double dash.

since "apple" and "apples" are different, how do we 





### ⬛ OR operator `|`

strings can be added. so %likes + s means like `apples`, `oils`, `metals`

```
@: likes
likes : apple oil metal

Q: like $likes | %likes + s
A: Yes, I do
```





dont aim for perfect grammer. aim for a factually correct response.





#### ⬛ Alternative Response `;` 

semicolon operator can be used to give alternative response.

```
@: likes love
likes : apple oil metal
love : like crazy_about

Q: like anot
A: Yeah! ; Yes, I $love $likes

--

bot response 1 : Yes, i crazy about oil
bot response 2 : Yeah!
```



## References and guards





### ⬛ Ordinary Reference

```
Q: $x            // matches any word. any word after this will be stored in a var
A: Yes, I like $x // recall the match in Q
```

so `$x` is an input field, where the user inputs the data. if its love instead of like, then the bot will output `?` as the function has not been coded. alternatively add love and like into a "words_to_represent_likes" list



- you can have many ordinary references in 1 user defined input variable

```
Q: like $x and $y
A: love $y and $x
```







### ⬛ Type Reference

```
@: likes
likes: apple oil metal

Q: like $likes  // matches the type (grp, list) denoted "likes"
A: Yes, I like $likes // recalls the match in likes
```







### ⬛ Conjunctions operator  `.`

limit reference match

```
@: animal food
animal: bird turkey pig horse
food: pretzel cheese turkey

Q: like $x.@animal.@food  // matches a thing that is both animal and food. as you can see here, turkey is in both lists so bot will only respond to turkey and the rest will output <?> case.
A: Yes, I like $x   // reference back what user has said
--
```

The `$x` is there for you to reference back specifically what the guy asked in the bot.

however, i noticed that you get back that reference when you write the $group in the `A` section as well.





Templates that are more specific must be above the templates that are more general.

Otherwise, general templates will activate and prevent the specific ones from activating.

```
@: drink
drink : coffee tea bubble tea

Q: like $x.@drink
A: Yes, I like $x
--

Q: like $x
A: i'm not sure
--


// in this example, general templates are below. code runs from top to bottom.
```



#### ⬛ Wildcard `$_`

you use this operator to signify a user input that you wanna take note 

```
@: drink
drink : coffee tea

Q: like $x.@drink or $_
Q: like $_ or $x.@drink // (two combinations of speech)
A: I prefer $x
--

//assuming x is tea and $_ is water
output : I prefer tea
```



#### ⬛ Guards

guards are ways to create conditional outputs. 

```
@: drink
drink : coffee tea bubble_tea|bubbel_tea

Q: like $x.@drink
A: $x :bubble_tea same? % I luv Bubble Tea
A: Yes, I like $x
--
```







#### ⬛ Synonyms in @ list

```
@: famous people
famous_people : Lee_Kuan_Yew|LKY Mike_Tyson
```

OR operator `| `in the list defines a synonym, and this can be mapped to your guards automatically.





#### ⬛ Super type (nested list)

```
@: drink altnamesfor_like food superlist_love
drink: coffee tea bubble_tea cocoa
altnamesfor_like: like prefer love 
food: chicken_rice chendol hor_fun
superlist_love: :food :drink

Q: $altnamesfor_like $x.@superlist_love
A: These foods or drinks are my favourite
--
```

`superlist_love` is the nested list here



## Logging and Debugging

logs can help you analyse responses that users put in. Most often, you would like to analyse logs that output `idk` function.



place `idk` templates last, as they are the most general template for your microtopic.



Logging`L:`

```
Q: like $x
A: I'm not sure if I do.
L: Unknown drink $x
--

// logging is only done when the template matches. 
```



### ⬛ Associations `assoc`

```
@: animal
animal: duck rabbit chicken horse|pony alligator

assoc: feet

{{
	:duck 2
	:rabbit 4
	:chicken 2
	:horse 4
}} +feet

// we often use the assoc in an answer

Q: $animal
A: $animal feet idk? % No info about $animal 
// this will check if its an idk scenario first, then move on to the next answer case if its NOT an idk case
A: $animal has ${ $animal feet } feet
--

// this is a 'smart context'

input : horse
output : horse has 4 feet

input : alligator
output : No info about alligator
```



#### ⬛ Search `search:`

- Search is something that matches keywords in a text



Say that you want to identify the keyword 'fun' in a sentence

```
Inputs:

I want some fun
Rei is beautiful
life is fun
confucius is handsome
```

```
@: keyword
keyword: fun life confucius

// the search function block starts here
search: wise-sayings

{{

"man who drops watch in toilet bowl, gets shitty time"
"man who runs in front of car, gets tired"
"man who runs behind car, gets exhausted"

}}   +wise-sayings
// a list of wise sayings that will be output

Q: $keyword
A: Confucius says: ${  $keyword wise-sayings   }
--

// so if keyword matches the on top part i.e. confucius, then it will output confucius says : <one from the "wise-sayings" list>

```

For this to work, every keyword should appear at least once in your search list











#### ⬛ Memory `mem:`

Memory lets your chatbot remember the past.

memory makes your chatbot `stateful`



```
mem: counts
Q: $_
A: Hello ${ counts }
K: +counts %
--
```

k rule is a rule that can increment the variable 'counts'

at the end of this implementation, the counts variable will be incremented by 1.

```
output as the user spams more and more shit

hello 1
hello 2
hello 3
...

```



#### ⬛ Combining memory and associations

```
mem: counts
assoc: greeting

{{
	1 "Hello"
	2 "Yes?"
	3 "Sorry"

}}
```





⬛ Combine search with assoc and memory





## ⬛ Rooms and keys



in a house you need keys to enter rooms

house is a chatbot, and each room is a collection of templates



#### ⬛ Room

you need some rules to define your room, and if room is not activated (entered) the bot will not perform actions within the room.



```
@: food
food : pretzel bun bread cheese

room: food

Q: like $x.@food
A: Love $x
--

end-room
```



rooms must be encased or wrapped with `room: <name>` and `end-room`



#### ⬛ Adding to a keychain

if template matches, then add key to keychain.



```
Q: food
A: Great! guess my favourite food
K: food   // this activates the `food` key
--
```



for including stuff, include the catch all or most general stuff at the bottom, as the code runs from top to bottom.



in your includes, the bot will match from the top to the bottom.

example : 

```
include ./topics/food.m
include ./topics/drinks.m
```

it will match things from `food.m` before things from `drinks.m`

 

#### ⬛ Remove keys

back command moves back to previous key state

```
Q: food
A: Great! guess my favourite food
K: $back food // this goes back to the previous set of keychains 
```



use of `-` is better : you use this to discard keys

```
Q: food
A: Great! guess my favourite food
K: -food 
```



#### ⬛ Keys with Guards

you can also use K: with guards. use sparingly as it can lead to bugs

```
mem: repeats

Q: drink|drinks
A: repeats 4 < % Bet you cant guess a drink I like
K: repeats 4 < % $back drinks
A: repeats 4 >= % lets try food
K: repeats 4 >= % $back food
K: repeats+ %
--
```

after repeating itself for 4 times, the bot will give a different answer, or set of answers. if you use keys with guards



#### ⬛ Using `K:` with ; alternatives `;`

```
Q: $_
A: Guess something I like
K: $back food ; $back drinks
--
```

- At random, it will assign keys for either the left one or the right one. 

use for discovery bots, or give bots more character.





#### ⬛ New words

```
:  // creates a new word
;  // completes the new word
```

example

```
: hello "Hello" . cr;
```

`cr` creates new line. `.` takes whatever is in the previous block and outputs it.

`hello` is the name, while `"Hello" . cr` is an executable





#### ⬛ XT : Executable





#### ⬛ Potential stuff to build

- element table for the periodic table - information on the elements







