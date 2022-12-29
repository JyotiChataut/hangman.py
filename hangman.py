import random
word_list=["mango","banana","apple"]
chosen_word=random.choice(word_list)
word_length=len(chosen_word)
lives=6

print(f'(the solution is {chosen_word}')

#create blanks
display=[]
for _ in range(word_length):
     display += "_"


end_of_game=False
while not end_of_game:
     guess=input("Guess a letter: ").lower()
     print(guess)
     for position in range(word_length):
         letter=chosen_word[position]
     
         if letter==guess:
             display[position]=letter
     if guess not in chosen_word:
        lives-=1
        if lives==0:
            end_of_game=True
            print("You Lose")
     print(f"{''.join(display)}")
 
     if "_" not in display:
        end_of_game=True
        print("You Win")
    
    