import random

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

#Tells if word one comes after word two or not

def comesAfter(word, word2):
    w1 = []
    w2 = []

    for i in word:
        if i.isalpha():
            w1.append(alphaNumber.get(i))                                                                        

    for i in word2:                                                                                              

        if i.isalpha():                                                                                          

            w2.append(alphaNumber.get(i))                                                                        

                                                                                                                 
    count = 0                                                                                                    
    for i in w1:                                                                                                 
        if len(w2) > count:
            if i > w2[count]:                                                                                    

                return True                                                                                      

            elif i < w2[count]:                                                                                  

                return False                                                                                     

        else:                                                                                                    
            return True                                                                                          

        count += 1                                                                                               
    return False

def swap(list, index1, index2):                                                                                  

    x = list[index1]                                                                                             

    list[index1] = list[index2]                                                                                  

    list[index2] = x                                                                                             

                                                                                                                 

def partition(words, first, last):                                                                               

    pivot = words[last]                                                                                          

    mark = words[first]                                                                                          

    i_mark = first                                                                                               

    count = first                                                                                                

                                                                                                                 

    while True:                                                                                                  

        if comesAfter(pivot, mark):                                                                              

            i_mark += 1                                                                                          
            mark = words[i_mark]                                                                                 

        else:                                                                                                    

            break                                                                                                

                                                                                                                 

    count = i_mark + 1