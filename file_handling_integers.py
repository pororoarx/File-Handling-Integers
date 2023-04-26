# import pyfiglet
import pyfiglet

# Set and print the title of the activity in color and different font
title_of_assign = "Module 2-Prob 1"
font = "slant"
print("\033[38;5;206m", pyfiglet.figlet_format(title_of_assign, font=font))


# a Python program that reads a text file named numbers.txt that contains 20 integers. The program will create two other text file; the first text file will be named even.txt that will contains all even numbers extracted from the numbers.txt. The second text file will be named odd.txt that will contains all odd numbers extracted from the numbers.txt.


# Start

# Create a function called process
def process():
    # open numbers.txt (read), even.txt (write), odd.txt (write)
    with open("number.txt") as file_1, open("even.txt", "w") as even_file, open("odd.txt", "w") as odd_file:
        # Loop through each line in numbers.txt
        for line in file_1:
            # Convert the line into integer 
            number = int(line.strip())
            # Print number to the console to check if the code is working
            print(number)
            # Check if the number is even or odd
            if number % 2 == 0:
                # If even, write it to even.txt
                even_file.write(str(number) + "\n")
            else:
                # If odd, write it to odd.txt
                odd_file.write(str(number) + "\n")

# Execute the function
process()