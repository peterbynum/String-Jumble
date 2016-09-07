"""
stringjumble.py
Author: Peter Bynum
Credit:
turning strings into lists: http://stackoverflow.com/questions/8266529/python-convert-string-to-list
turning lists into strings: https://www.decalage.info/en/python/print_list
[::-1] gives reverse order of a string/list: https://docs.python.org/2/whatsnew/2.3.html#extended-slices
Assignment: String Jumble

The purpose of this challenge is to gain proficiency with 
manipulating lists.

Write and submit a Python program that accepts a string from 
the user and prints it back in three different ways:

* With all letters in reverse.
* With words in reverse order, but letters within each word in 
  the correct order.
* With all words in correct order, but letters reversed within 
  the words.

Output of your program should look like this:

Please enter a string of text (the bigger the better): There are a few techniques or tricks that you may find handy
You entered "There are a few techniques or tricks that you may find handy". Now jumble it:
ydnah dnif yam uoy taht skcirt ro seuqinhcet wef a era erehT
handy find may you that tricks or techniques few a are There
erehT era a wef seuqinhcet ro skcirt taht uoy yam dnif ydnah
"""

string = input("Please enter a string of text (the bigger the better): ")
print('You entered "{0}". Now jumble it: '.format(string))
list = string.split()
print()
line1 = string
print(line1[::-1])
print()
line2 = list[::-1]
print(' '.join(line2))
print()
line3 = []
[line3.append(list[i][::-1]) for i in (0,(len(list)-1))]
print(line3)