#Python - if/else, loops, functions Project

# Task 0
This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print whether the number stored in the variable number is positive or negative.

# Task 1
This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable number.

# Task 2
A program that prints the ASCII alphabet, in lowercase, not followed by a new line.

# Task 3
A program that prints the ASCII alphabet, in lowercase, not followed by a new line.

# Task 4
A program that prints all numbers from 0 to 98 in decimal and in hexadecimal (as in the following example)

# Task 5
A  program that prints numbers from 0 to 99.

* Numbers must be separated by ,, followed by a space
* Numbers should be printed in ascending order, with two digits
* The last number should be followed by a new line
* You can only use no more than 2 print functions with string format
* You can only use one loop in your code
* You are not allowed to store numbers or strings in a variable
* You are not allowed to import any module

# Task 6
A program that prints all possible different combinations of two digits.

# Task 7
A function that checks for lowercase character.

* Prototype: def islower(c):
* Returns True if c is lowercase
* Returns False otherwise
* You are not allowed to import any module
* You are not allowed to use str.upper() and str.isupper()
* Tips: ord()

# Task 8
A function that prints a string in uppercase followed by a new line.

* Prototype: def uppercase(str):
* You can only use no more than 2 print functions with string format
* You can only use one loop in your code
* You are not allowed to import any module
* You are not allowed to use str.upper() and str.isupper()
* Tips: ord()

# Task 9
A function that prints the last digit of a number.

# Task 10
A function that adds two integers and returns the result.

* Prototype: def add(a, b):
* Returns the value of a + b
* You are not allowed to import any module

# Task 11
A function that computes a to the power of b and return the value.

* Prototype: def pow(a, b):
* Returns the value of a ^ b
* You are not allowed to import any module

# Task 12
A function that prints the numbers from 1 to 100 separated by a space.

* For multiples of three print Fizz instead of the number and for multiples of five print Buzz.
* For numbers which are multiples of both three and five print FizzBuzz.
* Prototype: def fizzbuzz():
* Each element should be followed by a space
* You are not allowed to import any module

# Task 13
A function in C that inserts a number into a sorted singly linked list.

* Prototype: listint_t *insert_node(listint_t **head, int number);
* Return: the address of the new node, or NULL if it failed

# Task 14
A program that prints the ASCII alphabet, in reverse order, alternating lowercase and uppercase (z in lowercase and Y in uppercase) , not followed by a new line.

# Task 15
A function that creates a copy of the string, removing the character at the position n (not the Python way, the “C array index”).

# Task 16
Python function def magic_calculation(a, b, c): that does exactly the same as the following Python bytecode:

3             0 LOAD_FAST                0 (a)
              3 LOAD_FAST                1 (b)
              6 COMPARE_OP               0 (<)
              9 POP_JUMP_IF_FALSE       16

  4          12 LOAD_FAST                2 (c)
             15 RETURN_VALUE

  5     >>   16 LOAD_FAST                2 (c)
             19 LOAD_FAST                1 (b)
             22 COMPARE_OP               4 (>)
             25 POP_JUMP_IF_FALSE       36

  6          28 LOAD_FAST                0 (a)
             31 LOAD_FAST                1 (b)
             34 BINARY_ADD
             35 RETURN_VALUE

  7     >>   36 LOAD_FAST                0 (a)
             39 LOAD_FAST                1 (b)
             42 BINARY_MULTIPLY
             43 LOAD_FAST                2 (c)
             46 BINARY_SUBTRACT
             47 RETURN_VALUE

