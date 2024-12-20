import time
import os
import random


password = "stardust girl"
upass = ""

while upass != password:
    upass = input("What's the password? ") # Make advanced-looking lock setup with print statements
    if upass != password:
        print("Incorrect password.")

time.sleep(1)

print("Correct Password! Let's start the game (;")

time.sleep(2)

os.system('clear')

def prints(toprint):

    for char in toprint:
        print(char, end="", flush=True)
        time.sleep(0.07)

    
    print("")

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
    os.system('clear')
    if limbs == 0:
        prints("   ____  ")
        prints("  /    | ")
        prints(" |     Ô ")
        prints(" |       ")
        prints(" |       ")
        prints("__________")
    elif limbs == 1:
        prints("   ____  ")
        prints("  /    | ")
        prints(" |     0 ")
        prints(" |       ")
        prints(" |       ")
        prints("__________")
    elif limbs == 2:
        prints("   ____  ")
        prints("  /    | ")
        prints(" |     0 ")
        prints(" |     | ")
        prints(" |       ")
        prints("__________")
    elif limbs == 3:
        prints("   ____  ")
        prints("  /    | ")
        prints(" |     0 ")
        prints(" |     | ")
        prints(" |    /  ")
        prints("__________")
    elif limbs == 4:
        prints("   ____  ")
        prints("  /    | ")
        prints(" |     0 ")
        prints(" |     | ")
        prints(" |    / | ")
        prints("__________")
    elif limbs == 5:
        prints("   ____  ")
        prints("  /    | ")
        prints(" |     0 ")
        prints(" |    /| ")
        prints(" |    / | ")
        prints("__________")
    elif limbs == 6:
        prints("   ____  ")
        prints("  /    | ")
        prints(" |     0 ")
        prints(" |    /|l")
        prints(" |    / |")
        prints("__________")
        time.sleep(0.1)
        prints("He gay??")
        time.sleep(1)
        os.system('clear')
        time.sleep(1)
        return
    
    prints("\nWord so far: ")

    output = ""
    for l in uncovered:
        output += l + " "
    
    prints(output)

# Game End

def success():
    os.system('clear')
    i = 0

    messagestr = "Congratulations on 20 amazing years, Stardust Girl!"
    message = list(messagestr)

    # Fancy Number Thing (S1)
    while i < 100:

        output = ""
        j = 0

        m = 0
        k = (100 - i - j) / 2
        while m < k:
            output += " "
            m += 1
            
        while j < i:

            if random.randint(0, 100) < 1 and len(message) > 0:
                output += "\033[1m" + message[0] + "\033[0m"
                message.pop(0)
            else:
                output += str(random.randint(0, 1))

            j += 1
        prints(output)
        time.sleep(0.05)

        i += 1
    
    # Fancy Number Thing (S2)
    while len(message) > 0:
        output = ""
        j = 0

        # Randomly choose if this is a row that will contain a point


        while j < 100:
            if random.randint(0, 50) < 1:
                output += message[0]
                message.pop(0)
            else:
                output += str(random.randint(0, 1))
            
            j += 1
        prints(output)
        time.sleep(0.05)

        i += 1
    


#success()
# Round Method

def round(limbs):
    render(limbs)

    if limbs == 6:
        return

    move = "null"
    while len(move) > 1 or len(move) < 1:
        prints("Choose a letter! ")
        move = input("")
        if len(move) > 1 or len(move) < 1:
            prints("Please choose a letter.")
    
    if move in word or move.upper() in word or move.lower() in word:
        prints("Congratulations! " + move + " is a letter in the word(s).")

        for l in word:
            if l == move or l.lower() == move or l.upper() == move:
                uncovered[word.index(l)] = l
                word[word.index(l)] = "_"

                if "_" not in uncovered:
                    success()
                    return
    else:
        prints("Sorry! " + move + " is not a letter in the word(s).")
        limbs += 1
    
    round(limbs)


round(limbs) # Start the game!