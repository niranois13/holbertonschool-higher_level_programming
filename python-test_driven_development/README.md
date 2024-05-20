# Python - Test-driven development

This repository contains the tasks I made in order to grasp the concept and the importance of testing during development.

### Task List:

0. **Integers addition**
   -[0-add_integer.py](../tree/main/0-add_integer.py), [tests/0-add_integer.txt](../tree/main/tests/0-add_integer.txt)  
   -Tasks:  
     1. Write a function that adds 2 integers.
     2. Prototype: def add_integer(a, b=98):
     3. a and b must be integers or floats, otherwise raise a TypeError exception with the message a must be an integer or b must be an integer
     4. a and b must be first casted to integers if they are float
     5. Returns an integer: the addition of a and b
     6. You are not allowed to import any module

**1. Divide a matrix**
   -Files  
   -Tasks:  
     1. Write a function that divides all elements of a matrix.
     2. Prototype: def matrix_divided(matrix, div):
     3. 'matrix' must be a list of lists of integers or floats, otherwise raise a 'TypeError' exception with the message 'matrix must be a matrix (list of lists) of integers/floats'
     4. Each row of the matrix must be of the same size, otherwise raise a 'TypeError' exception with the message 'Each row of the matrix must have the same size'.
     5. 'div' must be a number (integer or float), otherwise raise a 'TypeError' exception with the message 'div must be a number'.
     6. 'div' can’t be equal to 0, otherwise raise a 'ZeroDivisionError' exception with the message 'division by zero'
     7. All elements of the 'matrix' should be divided by 'div', rounded to 2 decimal places
     8. Returns a new matrix
     9. You are not allowed to import any module

**2. Say my name**
  -Files  
  -Tasks:  
     1. Write a function that prints My name is '<first name> <last name>'
     2. Prototype: 'def say_my_name(first_name, last_name=""):'
     3. 'first_name' and 'last_name' must be strings otherwise, raise a 'TypeError' exception with the message 'first_name must be a string or last_name must be a string'
     4. You are not allowed to import any module

**3. Print square**
  -Files  
  -Tasks:  
     1. Write a function that prints a square with the character #.
     2. Prototype: 'def print_square(size):'
     3. 'size' is the size length of the square
     4. 'size' must be an integer, otherwise raise a 'TypeError' exception with the message 'size must be an integer'
     5. if 'size' is less than 0, raise a 'ValueError' exception with the message 'size must be >= 0'
     6. if 'size' is a float and is less than 0, raise a 'TypeError' exception with the message 'size must be an integer'
     7. You are not allowed to import any module

**4. Text indentation**
  -Files  
  -Tasks:  
     1. Write a function that prints a text with 2 new lines after each of these characters: ., ? and :
     2. Prototype: def text_indentation(text):
     3. text must be a string, otherwise raise a TypeError exception with the message text must be a string
     4. There should be no space at the beginning or at the end of each printed line
     5. You are not allowed to import any module

**5. Max integer - Unittest**
  -Files  
  -Tasks:  
     1. Since the beginning you have been creating “Interactive tests”. For this exercise, you will add 'Unittests'.
     2. In this task, you will write 'unittests' for the function 'def max_integer(list=[]):'.
     3. Your test file should be inside a folder tests
     4. You have to use the 'unittest' module
     5. Your test file should be python files (extension: .py)
     6. Your test file should be executed by using this command: 'python3 -m unittest tests.6-max_integer_test'
     7. All tests you make must be passable by the function below
     8. We strongly encourage you to work together on test cases, so that you don’t miss any edge case
