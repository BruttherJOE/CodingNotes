# C++ Cheat sheet

-------------------------------------------------------------------------------------------------------------------      compiled by bruttherjoe





[TOC]

# Basic Syntax

## Semicolons & Blocks in C++

Statements must end with `;`.  `;` terminates statements. 

Blocks must be encapsulated by `{}`.





------

------





## Code Organisation and flow

### Line Comprehension

You can make one liners to flex on your friends! bad for reading and documentation though.

C++ does not recognise the end of a line as a terminator. For example,

```c++
x = y;
y = y+1;
add(x, y);
```

is the same as

```c++
x = y; y = y+1; add(x, y);
```

### New line character 

This is `\n` in python.

C++ uses `endl`.

For example,

```c++
#include <iostream>
using namespace std;
int main()
{
 cout << "My name is : " << Joe << endl;
 cout << "My age is : " << 22 << endl;
 return 0;
}
```

## Comments

```c++
/* This is a comment */
/* C++ comments can also
* span multiple lines
*/
--------------------------------------
#include <iostream>
using namespace std;
main()
{
 cout << "Hello World"; // prints Hello World
 return 0;
}
```





------

------





## Variables

### Variable Declaration

use `extern` to declare variables.

```c++
#include <iostream>
using namespace std;
// Variable declaration:
extern int a, b;
extern int c;
extern float f;

int main ()
{
 // Variable definition:
 int a, b;
 int c;
 float f;
 // actual initialization
 a = 10;
 b = 20;
 c = a + b;
 cout << c << endl ;
 f = 70.0/3.0;
 cout << f << endl ;
C++
30
 return 0;
}

--------------- results: ----------------------------

30
23.3333
```

### Variable declaration and assignment of value

```c++
int g = 20;
```

### Local Variables

Variables declared inside a function or block are local variables, and are not known to functions outside their own.

### Global Variables

Global variables are defined outside of all functions, usually at the top of the program, and are known everywhere in the function.

### Initialising Variables

Local variables are initialised manually by yourself.

Global variables are initialised automatically by the system as such:

| Data type | Initialiser |
| --------- | ----------- |
| int       | 0           |
| char      | `\0`        |
| float     | 0           |
| double    | 0           |
| pointer   | NULL        |





------

------





## Constants

2 ways to define them

- `#define` preprocessor
- `const` keyword



### #define Preprocessor

2 Parameters:
`#define identifier value`

```c++
#define LENGTH 10
#define WIDTH 5
```



### const Keyword

`const type variable = value;`

```c++
 const int LENGTH = 10;
 const int WIDTH = 5;
```





It is good programming practice to define constants in **CAPITALS**.





------

------





## Function calling 

(kinda like OOP in python)

You can declare function anywhere, define it anywhere, and call it anywhere. Stick to this format because there may be other nuances and u are not a cs boi.

```c++
// function declaration
int func();


int main()
{
 // function call
 int i = func();
}


// function definition
int func()
{
 return 0;
}

```





------

------



## Undone stuff which I may never do

storage classes, register, static storage class, extern storage class,mutable storage class

arithmetic operators (copy python stuff, its the same)

