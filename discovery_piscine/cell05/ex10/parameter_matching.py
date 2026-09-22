import sys

if len(sys.argv) == 2:
    target_word = sys.argv[1]
    user_word = input("What was the parameter? ")
    
    if user_word == target_word:
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")