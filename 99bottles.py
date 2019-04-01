'''
Author: Srinivas Cheemalapati

Project 1: 99 Bottles
Create a program that prints out every line to the song "99 bottles of beer on the wall."
Do not use a list for all of the numbers, and do not manually type them all in. Use a built in function instead.
Besides the phrase "take one down," you may not type in any numbers/names of numbers directly into your song lyrics.
Remember, when you reach 1 bottle left, the word "bottles" becomes singular.

2 (bottles) of beer on the wall, 2 (bottles) of beer.
Take one down and pass it around, 1 (bottle) of beer on the wall.

1 (bottle) of beer on the wall, 1 (bottle) of beer.
Take one down and pass it around, (no more bottles) of beer on the wall.

No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, 99 bottles of beer on the wall.
'''
# Reference: http://www.99-bottles-of-beer.net/lyrics.html


# function to print the song
def repeat(num_bottles):
    # Assign common strings upfront and only make changes to them as needed
    str1 = str2 = str3 = "bottles"
    str4 = "Take one down and pass it around,"
    num1 = num2 = str(num_bottles)
    num3 = str(num_bottles-1)

    if (num_bottles == 2):
        str3 = "bottle"

    elif(num_bottles == 1):
        num3 = "no more"
        str1 = str2 = "bottle"

    elif(num_bottles == 0):
        num1 = "No more"
        num2 = "no more"
        num3 = "99"
        str4 = "Go to the store and buy some more, "

    print(num1 + " " + str1 + " of beer on the wall, " + num2 + " " + str2 + " of beer.")
    print(str4 + " " + num3 + " " + str3 + " of beer on the wall" + "\n")


# execute the main function
def main():
    for count in reversed(range(100)):
        repeat(count)

# check if the main program is not from an imported module
if __name__ == '__main__':
        main()
