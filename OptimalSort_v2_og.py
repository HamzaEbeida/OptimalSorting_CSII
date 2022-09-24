import sys
import random

def alphaSort(words, letterIndex, letters, first, last):
    for i in words[first:last]:
        if letterIndex < len(i):
             count = alphaNumber.get(i[letterIndex])
             if count is None:
                 count = 0
                 for i in letters:
                     letters[count] += 1
             else:
                  for i in letters[count:26]:
                      letters[count] += 1
        else:
            count = 0
            for i in letters:
                letters[count] += 1

    wordsCopy = words.copy()
    lettersIterate = letters.copy()

    count = 0
    for i in wordsCopy[first:last]:
        if letterIndex < len(i):
             if alphaNumber.get(i[letterIndex]) is None:
                  words[first + lettersIterate[0] - 1] = i
                  lettersIterate[0] -= 1
             else:
                  words[first + lettersIterate[alphaNumber.get(i[letterIndex])] - 1] = i
                  lettersIterate[alphaNumber.get(i[letterIndex])] -= 1
        else:
            words[first + lettersIterate[0] - 1] = i
            lettersIterate[0] -= 1

def recursiveCall(words, first, last, letterIndex):
     letters = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

     alphaSort(words, letterIndex, letters, first, last)
     count = 1

     for i in letters[2:26]:
          if letters[count] < i:
               recursiveCall(words, letters[count], i, letterIndex + 1)
          count += 1


alphaNumber = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
    "K": 11,
    "L": 12,
    "M": 13,
    "N": 14,
    "O": 15,
    "P": 16,
    "Q": 17,
    "R": 18,
    "S": 19,
    "T": 20,
    "U": 21,
    "V": 22,
    "W": 23,
    "X": 24,
    "Y": 25,
    "Z": 26
}

words = ["a", "b", "c", "C", "cess", "chess", "celerey", "ce-lery", "d", "D", "Don't", "t", "u", "v", "w", "x", "y", "z"]

random.shuffle(words)
recursiveCall(words, 0, len(words), 0)
print("done: ", words)

#alphaSort(words, 0, letters, 0, len(words))
#letters = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]