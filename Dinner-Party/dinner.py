import time
import os


password = "10010"
upass = ""

while upass != password:
    upass = input("What's the password? ")
    if upass != password:
        print("Incorrect password.")

print("Correct Password! Let's start the game (;")

# Start Game

wordstr = "Happy Birthday!"
word = list(wordstr)
uncovered = []
limbs = 0

i = 0
while i < len(word):
    if word[i] != " ":
        uncovered.append("_")
    else:
        uncovered.append(" ")
    
    i += 1

def render(limbs):
    if limbs == 0:
        print("   ____  ")
        print("  /    | ")
        print(" |     Ô ")
        print(" |       ")
        print(" |       ")
        print("__________")
    elif limbs == 1:
        print("   ____  ")
        print("  /    | ")
        print(" |     0 ")
        print(" |       ")
        print(" |       ")
        print("__________")
    elif limbs == 2:
        print("   ____  ")
        print("  /    | ")
        print(" |     0 ")
        print(" |     | ")
        print(" |       ")
        print("__________")
    elif limbs == 3:
        print("   ____  ")
        print("  /    | ")
        print(" |     0 ")
        print(" |     | ")
        print(" |    /  ")
        print("__________")
    elif limbs == 4:
        print("   ____  ")
        print("  /    | ")
        print(" |     0 ")
        print(" |     | ")
        print(" |    / | ")
        print("__________")
    elif limbs == 5:
        print("   ____  ")
        print("  /    | ")
        print(" |     0 ")
        print(" |    /| ")
        print(" |    / | ")
        print("__________")
    elif limbs == 6:
        print("   ____  ")
        print("  /    | ")
        print(" |     0 ")
        print(" |    /|l")
        print(" |    / |")
        print("__________")
        time.sleep(0.1)
        print("He gay??")
        time.sleep(1)
        os.system('clear')
        time.sleep(1)
    
    print("\nWord so far: ")

    output = ""
    for l in uncovered:
        output += l + " "
    
    print(output)

# Round Method

def round(limbs):
    render(limbs)

    move = "null"
    while len(move) > 1 or len(move) < 1:
        move = input("Choose a letter! ")
        if len(move) > 1 or len(move) < 1:
            print("Please choose a letter.")
    
    if move in word:
        print("Congratulations! " + move + " is a letter in the word(s).")

        for l in word:
            if l == move:
                uncovered[word.index(l)] = l
                word[word.index(l)] = "_"
    else:
        print("Sorry! " + move + " is not a letter in the word(s).")
        limbs += 1
    
    round(limbs)


round(limbs) # Start the game!