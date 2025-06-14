# You are going to build an encryption and decryption program using the Caesar cipher.
#
# Demo
# https://appbrewery.github.io/python-day8-demo/
#
# TODO-1:
# Create a function called encrypt() that takes original_text and shift_amount as 2 inputs.
#
# TODO-2:
# Inside the 'encrypt' function, shift each letter of the original_text forwards in the alphabet by the shift_amount and print the encrypted text.
#
# You can use the built-in Python index() function to find out the position of an item in a list. e.g.
#
# fruits = ["Apple", "Pear", "Orange"]
# fruits.index("Pear") #1
# e.g. If we have following values:
#
# plain_text = "hello"
# shift_amount = 1
# The final encrypted output should be:
#
# Here is the encoded result: ifmmp
#
# Where each of the letters of 'hello' is shifted up by 1.
#
#  Hint 1
# TODO-3:
# Call the encrypt() function and pass in the user inputs. You should be able to test the code and encrypt a message.
#
# TODO-4:
# What happens if you try to shift the letter 'z' forwards by 9? Can you fix the code?
#
#  Hint 2