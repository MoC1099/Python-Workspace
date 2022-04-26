# This is teh guessing game where user will keep on guessing the word
# user will have 3 chances to guess the word
#if user get the word, they win else lose

correct_word = True
secret_word = "Saad"

i = 0;

# The while statment on video
# while guess != secret_word and not(out_of_guesses:
while (i<=2):
    Guess = input("Guess the word")
    if Guess == secret_word:
        print("You got it")
        break
    elif Guess != secret_word:
        print("Try Again")
        i += 1
else:
    print("you Lost")





