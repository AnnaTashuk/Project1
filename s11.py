import re

def findSumReg(fileName):
    """
    Returns amount of all numbers in the input file. Ignores letters, non-characters 
    like punctuation and spaces.

    fileName: name of input file
    returns: sum of all numbers
    """
    return sum([int(num) for num in re.findall('[0-9]+',open(fileName).read())])


'''
test1
findSumReg(r'C:\Users\User\Desktop\Programing\2semestr\done\s1\regex_sum_42.txt')
'''
