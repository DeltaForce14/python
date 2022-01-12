
# HANGMAN GAME

import random
import hangman_words
import hangman_stages

#STEP ONE:  Pick random word

hangman_word = random.choice(hangman_words.word_list)
#print(hangman_word)

# STEP TWO: Print "-" instead of letters

display = []

#print a new line 
print("\n")    

for letter in range(0, len(hangman_word)):
    display.append(" _ ")
print(display)
    #print a new line 
print("\n")    
 

# STEP THREE: Check if picked letter in included in hangman word, if not take life away
          
# number of wrong tries
count = 7

while count > 0:
    picked_letter = input("Pick a letter: ").lower()
    for position in range (len(hangman_word)):
        if picked_letter == hangman_word[position]:
            display[position] = picked_letter  
    if picked_letter not in display:   
        count -= 1  
        print(hangman_stages.stages[count])
    print(display)    
    if count == 0:
        print("GAME OVER")     
    if " _ " not in display:
        print("\n")   
        print("YOU WIN")   
        break 
    




    