import random

print("***Welcome to the Guessing Game***")
print("You get 10 guesses")

randNum = random.randint(1,100)

userNum = None

guess = 10
guesses = 0

while(randNum!=userNum):
    userNum = int(input("Enter your guess: "))
    guess -= 1
    guesses += 1

    if userNum == randNum:
        print("You guessed it right!")
        
        print(f"You guessed it in {guesses} guesses")
        
        
    elif guess == 0:
        print("You have no more guesses left")
    
        break


    else:
        if userNum > randNum:
            print("Its wrong, the number is lower than this.")    
        else:
            print("Its wrong, the number is higher than this")
        
        
        
        
with open ("high_score.txt","r") as f:
   high_score = int(f.read())

if (guesses < high_score):
       with open ("high_score.txt","w") as f:
        f.write(str(guesses))


    


