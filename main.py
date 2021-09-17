from capitals import states


# //Create main functions 

def main():
    setup_game()
    play_game()

#// create a global variables states(list), capitals(dictionary),correct(int), incorrect(int),
#// used(list)
def setup_game():
    global states, capitals, correct, incorrect, used
    correct = 0
    incorrect = 0
    used = [False] * 50
# Call setup_state_list function & setup_capitals_dictionary function 
    states = setup_state_list()
    capitals = setup_capitals_dictionary()
    print ("GA SEI-712 PYTHON STATE/CAPITAL QUIZ HOMEWORK LAB")



def play_game():
    global correct, incorrect, used
    guess = ""
    while guess.lower() !="quit" :
        idx = random.randint(0, len(states)-1)
    while used[idx]:
        idx = random.randint(0, len(states)-1)
    used[idx] = True
    allTrue = True
    for i in range(0,50):
        if used[i] == False:
            allTrue = False
    if  allTrue:
            used = [False] *50 #Resetting used to all false
    state = states[idx]
    capital = capitals[state]
    guess = input("What is the Capital of " + state.upper() + "? (enter 'quit' to end): " )

    if guess.lower() == "quit":
        print("THANKS FOR PLAYING... you got {0} of {1} correct.\n".format(correct, (correct + incorrect)))
        
    elif guess.lower() == capital.lower():
        print("That is CORRECT! {0} is the capital of {1}.".format(capital, state))
        correct += 1
    else:
        print("SORRY...The capital of {0} is {1}".format(capital, state))
        incorrect += 1

    print ("YOUR SCORE: you have gotten {0} of {1} correct.\n".format(correct, (correct, incorrect)))



    # idx = 2
    # state = states [idx]
    # capital = capitals[state]
    # print ("The Capital of {0} is {1}." .format (state, capital) )

def setup_state_list():
    return states["name"]

def setup_capitals_dictionary():
    return states["name", "capital"]

main()






