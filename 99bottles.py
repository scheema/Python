'''
Author: Srinivas Cheemalapati

Project 1: 99 Bottles
Create a program that prints out every line to the song "99 bottles of beer on the wall."
Do not use a list for all of the numbers, and do not manually type them all in. Use a built in function instead.
Besides the phrase "take one down," you may not type in any numbers/names of numbers directly into your song lyrics.
Remember, when you reach 1 bottle left, the word "bottles" becomes singular.
'''
# Reference: http://www.99-bottles-of-beer.net/lyrics.html

# Use Predefined String Values
str1 = "bottles of beer"
str2 = "bottle of beer"
str3 = "on the wall"
str4 = "Take one down and pass it around"
str5 = "no more"
str6 = "No more"
str7 = "Go to the store and buy some more"

# function to print the song
def repeat(num_bottles):
    if (num_bottles > 2):
        print("%d %s %s, %d %s.\n%s, %d %s %s. \n" %(num_bottles,str1, str3,num_bottles,str1,str4,num_bottles-1,str1,str3))
    elif (num_bottles == 1):
        print("%d %s %s, %d %s.\n%s, %s %s %s. \n" %(num_bottles,str2, str3,num_bottles,str2,str4,str5,str1,str3))        
    elif (num_bottles < 1):
        print("%s %s %s, %s %s.\n%s, %d %s %s. \n" %(str6,str1, str3,str5,str1,str7,99,str1,str3))
# execute the main function
def main():
    for count in reversed(range(100)):
        repeat(count)

# check if the main program is not from an imported module
if __name__ == '__main__':
        main()
