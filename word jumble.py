import random
words = ["rat", "mouse", "coat", "closet", "door"]

random_word = random.choice(words)
shuffled_word = ''.join(random.sample(random_word, len(random_word)))
caps_word = shuffled_word.upper()

print("Welcome to Word Jumble")
print("Guess the jumbled word")


tries = 0
while tries < 3:
    print(caps_word)
    guess = input("Enter your guess: ")
    if guess == random_word:
        print("You guessed correct!")
        tries = tries + 8
        
    else:
        print("You guessed wrong, try again")
        tries = tries + 1
        
    if tries == 3:
        print("You have run out of guesses! The word was", random_word)
    
    
