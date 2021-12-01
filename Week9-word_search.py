# Dominic Pergola
# CSCI 102 - Section B
# Week 9
# Reference: none
# Time ~ 30 min

#read contents
f = open('dictionary.txt')
contents = f.readlines()
f.close()

#take inputs
print("Enter the length of the words to find:")
word_len = int(input("LENGTH> "))
print("Enter the seed to use:")
seed = input("SEED> ")

#random
import random
random.seed(seed)

#add words of specified length to a list
word_list = []
total = 0
for word in contents:
    if len(word) == word_len + 1:
        total += 1
        word_list.append(word)

#if there are any words of the right length, give ouputs and choose a random one
if total >= 1:
    
    ran_word = word_list[random.randint(0, len(word_list) - 1)]

    print(f"The number of words with length {word_len} is:")
    print(f"OUTPUT {total}")
    print(f"Here is one random word with length {word_len}:")
    print(f"OUTPUT {ran_word}")

#if no words of right length, report that
else:
    print(f"The number of words with length {word_len} is:")
    print("OUTPUT 0")
    print(f"There are no words of length {word_len} in the dictionary.")
    print("OUTPUT None")
