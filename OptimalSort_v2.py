import sys
import random

with open("random.txt") as file:
     words = []
     count = 0
     while count < 10000:
          try:
              words.append(next(iter(file)).strip())
          except StopIteration:
              break
          count += 1


#This is what sorts the letters by the letterIndex given (for example letterIndex = 3 sorts them by the thrid let\
ter, first and last is the range that itll send letters from, it takes two passes; the first pass saves the amoun\
t of each letter, and the second uses that to put letters in their correct spots. This function updates the words\
 array passed through and the letters array passed through
def alphaSort(words, letterIndex, letters, first, last):
    for i in words[first:last]:
        if letterIndex < len(i):
             count = alphaNumber.get(i[letterIndex])
             if count is None:
                  letters[0] += 1
             else:
                  letters[count] += 1
        else:
             letters[0] += 1

    j = 0
    for i in letters:
         if j == 0:
              j += 1
         else:
              letters[j] += letters[j - 1]
              j += 1

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

#This is the recursive call function, its what calls the sorting function and decides what ranges to pass through\
, ensures that it's sorting an amount of words larger than two and then calls the function, then uses the updated\
 letters array to define first and last and call itself untill the words array is completely sorted. Updates the \
words array passed through
def recursiveCall(words, first, last, letterIndex):
     letters = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

     alphaSort(words, letterIndex, letters, first, last)
     count = 1

     for i in letters[2:26]:
          if letters[count] < i - 1:
               recursiveCall(words, letters[count], i - 1, letterIndex + 1)
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

random.shuffle(words)
recursiveCall(words, 0, len(words), 0)
print("done")

#alphaSort(words, 0, letters, 0, len(words))
#letters = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]