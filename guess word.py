import random
words = ["rat", "mouse", "coat", "closet", "door"]

random_word = random.choice(words)
length = len(random_word)

print("Guess the word!")
print("There are", length, "letters in the word you have 5 tries!")

tries = 0
while tries < 5:
    guess = input("Enter your guess: ")
    if guess == random_word:
        print("Yes")
        tries = tries + 8
    
    else: 
        print("No")
        tries += 1
        
    if tries == 5:
        print("You have run out of tries!")
 
    
    