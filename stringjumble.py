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
list = string.split() #divides all elements of a string into separate elements in a list


line1 = string
print(line1[::-1]) #using slicing to rearrange "line1". leaving the start and end indexes blank signals to use the entire string, while the -1 is the command to flip it


line2 = list[::-1]
print(' '.join(line2)) #joins all the elements in "line2" with only a space in between


line3 = []
[line3.append(list[i][::-1]) for i in range(0,len(list))] #treats each element of the original list individually, flipping them one by one. However, it still add the elements themselves into the new line in the correct order.
print(' '.join(line3))




