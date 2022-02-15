import re
from collections import Counter

'''def wordcheck(guess):
    if(guess == "hello"):
        return ["yes"]
    return ["no"]
'''
def loadwords():
    wordlist = []
    with open("words.txt", mode = "r") as wordfile:
        for line in wordfile:
            wordlist.append(line)
    return wordlist

def startcheck(guess, positions):
    guessList = list(zip(list(guess),list(positions)))
    #wordlist = ["hello", "fears", "works", "nopes", "tests"]
    wordlist = loadwords()
    wlist = parser(guessList, wordlist)
    return wlist

def check(guess, positions, wordlist):
    guessList = list(zip(list(guess),list(positions)))
    wlist = parser(guessList, wordlist)
    return wlist


def parser(guess, wordlist):
    pattern = ["","","","",""]
    remove = []
    contains = []
    dupes = set()
    cap = {}
    for pos, (letter, value) in enumerate(guess):
        if letter not in cap:
            cap[letter] = 5
        if value == "X":
            if letter in contains:
                cap[letter] = contains.count(letter)
            elif letter not in dupes:
                remove.append(letter)
            pattern[pos] += "^{}".format(letter)
        elif value == "!":
            contains.append(letter)
            if letter in remove:
                cap[letter] = contains.count(letter)
                remove.remove(letter)
                for i in range(len(pattern)):
                    pattern[i] += "^{}".format(letter)
            #self.found[pos] = letter
            pattern[pos] = letter
        else:
            contains.append(letter)
            if letter in remove:
                cap[letter] = contains.count(letter)
                remove.remove(letter)
            pattern[pos] += "^{}".format(letter)
        dupes.add(letter)

    patternstring = "[" + "][".join(pattern) + "]"
    return removeInvalid(remove, contains, re.compile(patternstring), cap, wordlist)

def removeInvalid(remove, contains, pattern, cap, wordlist):
    return list(filter(lambda x : checkRemove(x,remove) and checkRegex(x,pattern) and checkContains(x,contains,cap), wordlist))

def checkRemove(string, remove):
    return not any([i in string for i in remove])
    
def checkRegex(string, pattern):
    return pattern.match(string)
    
def checkContains(string, contains, cap):
    count = Counter(contains)
    return all([cap[i] >= string.count(i) >= count[i] for i in count])