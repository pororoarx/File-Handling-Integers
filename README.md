# File-Handling-Integers


A Python program that reads a text file named numbers.txt that contains 20 integers. The program will create two other text file; the first text file will be named even.txt that will contains all even numbers extracted from the numbers.txt. The second text file will be named odd.txt that will contains all odd numbers extracted from the numbers.txt.

Table of Contents:
- Installation
- Usage
- Contributing
- Conclusion
=============================================================================================================
- Installation
1. Clone the repository to your local machine: ‘git clone git@github.com:pororoarx/File-Handling-Integers.git’
2.	Install the required ‘pyfiglet’ module: ‘pip install pyfiglet’
3.	Save the ‘numbers.txt’ file in the project directory

- Usage
1. Open Git Bash and go to the project directory.
2.	Run the program: ‘file_handling_integers.py’
3.	Two new files called ‘even.txt’ and ‘odd.txt’ will be created in the same directory

- Formulation:
The program reads the numbers.txt file using the with open() statement and opens two other files even.txt and odd.txt in write mode. It then loops through each line in numbers.txt, converts the line into an integer, and checks if the number is even or odd using the modulus operator. If the number is even, it writes it to even.txt. Otherwise, it writes it to odd.txt.

- Conclusion: 
This program executes find handling, specifically, how to read from and write to a file in Python. It also demonstrates the usage of conditional statements and modulus operator. This REAME.md file provides clear instructions for installing and running the program, so feel free to contribute to its development.

===========================================================================================================
