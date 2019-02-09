# Tyler Moore, Ian Riley
# Python implementation of stable matching problem
# Homework 1 Starter Code
# CS 2123 last modified 1/14/19

# Tom Sommers, Dina Binmansour, Eric Schnelker - 1/18/19
# Completion of starter code for Gale Shapley implementation
"""
_____________
PSEUDOCODE:
_____________
INITIALIZE S to empty matching.
WHILE (some man m is unmatched and hasn't proposed to every woman)
  WHILE (c, the index of some woman on m's list to whom m has not yet proposed to [where i is initialized to 0), is less than the length of m's preference list)
      IF (w is unmatched)
        Add pair m–w to matching S.
      ELSE IF (w prefers m to her current partner m')
        Remove pair m'–w from matching S.
        Add pair m–w to matching S.
      ELSE
        w rejects m.
        increment w by one
RETURN stable matching S.
"""


def gs(men, women, pref):
    matchedPairs = {}  # initialize dictionary to keep track of pairs
    s = []  # Tuples to contain pairs
    q = []

    print()
    print()
    print("The pairing games have begun... Place your bets on the order in which pairs of contestants will survive.")
    print("...")
    print("What's that...?")
    print("This isn't a death match...? ")
    print("... What the hell are you paying me for, then?")
    print("Oh?")
    print("They're placing bets on who will be succesfully paired and married? ")
    print("So it IS a death match! Alright, then.")
    print("Ready. ")
    print("Set.")
    print("BEGIN!!!")
    print()

    for m in men:
        q.append(m) #queue to keep track of unpaired men - this fills the queue
    while q: #while men in the queue
        m = q.pop(0) #pops off first man in queue
        for w in pref[m]: #iterates through the women in the current man's pref list
            if w not in matchedPairs:
                matchedPairs[w] = m
                print("Pairing " + m + " with " + w + ". Adding the happy couple to matched pairs. They have won the round.")
                #prints to keep track of where the program is and what it's doing
                break
            elif pref[w].index(m) < pref[w].index(matchedPairs.get(w)):
                mrDumped = matchedPairs.get(w) #if in this elif, the previous pair is broken, and mrdumped is the man from that pair
                print(mrDumped + " is a horrible person and was dumped by " + w + ". Adding him back to the queue and pairing " + w + " with " + m)
                #prints to keep track of where the program is and what it's doing
                matchedPairs[w] = m #new pair
                q.append(mrDumped) #adds the main from previous pair back to queue to resend him through pairing
                break
            print(m + " is hopeless and was rejected by " + w + ". Moving on to the next woman on his target... I mean, um... preference list.")
            #prints to keep track of where the program is and what it's doing
    for w in women:
        s.append((matchedPairs.get(w), w))
        #gives output as tuples
    return s


def gs_block(men, women, pref, blocked):
    print()
    print()
    print("The pairing games have again begun their run, although this time there's a twist! Forbidden matches! Place your bets on the order in which pairs of contestants will survive, keeping in mind the matches that are not allowed!")
    print()

    matchedPairs = {}  # initialize dictionary to keep track of pairs
    s = []  # Tuples to contain pairs
    q = []
    locked = set()

    for pair in blocked: #makes it so we iterate over the men in blocked first and if they're paired they get locked.
        if pair[0] not in q: #adds men in blocked to queue
            q.append(pair[0])
        locked.add(pair[0]) #makes it so if these men have a successful pair, they can't be dumped
    for m in men: #adds rest of men to queue
        if m not in q:
            q.append(m)
    while q:
        m = q.pop(0) #pops off first man in list
        for w in pref[m]:
            if (m, w) in blocked:
                print(m + " is hopeless and was rejected by " + w + " because, although " + m + " was not paired, his pairing with " + w + " was forbidden. Moving on to the next woman on his target... I mean, um... preference list.")
                #prints to keep track of where the program is and what it's doing
                continue
            if w not in matchedPairs:
                matchedPairs[w] = m
                print("Pairing " + m + " with " + w + ". Adding the happy couple to matched pairs. They have won the round.")
                #prints to keep track of where the program is and what it's doing
                break
            elif pref[w].index(m) < pref[w].index(matchedPairs.get(w)) and matchedPairs.get(w) not in locked:
                mrDumped = matchedPairs.get(w) #if in this elif, the previous pair is broken, and mrdumped is the man from that pair
                print(mrDumped + " is a horrible person and was dumped by " + w + ". Adding him back to the queue and pairing " + w + " with " + m)
                #prints to keep track of where the program is and what it's doing
                matchedPairs[w] = m #new pair
                q.append(mrDumped) #adds the main from previous pair back to queue to resend him through pairing
                break
            else:
                print(m + " is hopeless and was rejected by " + w + " because, although " + m + " was not paired, his pairing with " + w + " was forbidden. Moving on to the next woman on his target... I mean, um... preference list.")
                #prints to keep track of where the program is and what it's doing
                continue
    for w in women:
        s.append((matchedPairs.get(w), w))
        #gives output as tuples
    return s



def gs_tie(men, women, preftie):
    matchedPairs = {}  # initialize dictionary to keep track of pairs
    s = []  # Tuples to contain pairs
    q = []
    men_paired = [] #Gives a way to track men paired so they don't get paired twice - better explanation below

    print()
    print()
    print("The final pairing games have now begun, and, you guessed it, there's a new twist replacing the last one. Preference ties! Place your bets on the order in which pairs of contestants will survive, keeping in mind that some contestants preferences for others are equal!")

    for m in men:
        q.append(m) #queue to keep track of unpaired men - this fills the queue
        
    while q: #while men in the queue
        m = q.pop(0) #pops off first man in queue
        for i in range(len(preftie[m])): #Goes over the list of sets that corresponds to the key of the current man's name in the dictionary preftie
            for w in preftie[m][i]: #Goes over the women in each set in the list
                if m in men_paired: #Ran into an issue where whenever a man was paired and we would break, we couldn't break out
                                    #of the initial for loop, so each man would try to pair with each woman. This prevents paired men
                                    #from being paired again, as initial gale-shapley didn't account for a second for loop.
                    break
                if w not in matchedPairs:
                    matchedPairs[w] = m
                    men_paired.append(m)
                    print("Pairing " + m + " with " + w + ". Adding the happy couple to matched pairs. They have won the round.")
                    #prints to keep track of where the program is and what it's doing
                    break
                else:
                    indexCurrentGuy = int() #initialize
                    indexOG = int() #initialize
                    for i in range(len(preftie[w])): #Goes over the list of sets that corresponds to the key of the current woman's name in the dictionary preftie
                        if m in preftie[w][i]: #Checks to see if the current man is in the ith set in the list of sets for w.
                            indexCurrentGuy = i #if he is, his index is now i
                        elif matchedPairs[w] in preftie[w][i]: #Checks to see if the current man is in the ith set in the list of sets for w.
                            indexOG = i #if he is, his index is now i
                        elif m in preftie[w][i] and matchedPairs[w] in preftie[w][i]: #A woman can't dump her man for a man she likes equally.
                            print("Both in same preference level. Breaking...")
                            break
                    if indexCurrentGuy < indexOG: #compares the indices like in initial gale-shapley. Less than is used because a lower index is 
                                              #better than a higher index in this scenario
                        mrDumped = matchedPairs.get(w) #if in this elif, the previous pair is broken, and mrdumped is the man from that pair
                        men_paired.remove(mrDumped)
                        print(mrDumped + " is a horrible person and was dumped by " + w + ". Adding him back to the queue and pairing " + w + " with " + m)
                        #prints to keep track of where the program is and what it's doing
                        matchedPairs[w] = m #new pair
                        men_paired.append(m)
                        q.append(mrDumped) #adds the main from previous pair back to queue to resend him through pairing
                        break
                    print(m + " is hopeless and was rejected by " + w + ". Moving on to the next woman on his target... I mean, um... preference list.")

            #prints to keep track of where the program is and what it's doing
    for w in women:
        s.append((matchedPairs.get(w), w))
        #gives output as tuples
    return s

if __name__ == "__main__":
    # input data
    the_men = ['xavier', 'yancey', 'zeus']
    the_women = ['amy', 'bertha', 'clare']

    the_pref = {
        'xavier': ['amy', 'bertha', 'clare'],
        'yancey': ['bertha', 'amy', 'clare'],
        'zeus': ['amy', 'bertha', 'clare'],
        'amy': ['yancey', 'xavier', 'zeus'],
        'bertha': ['xavier', 'yancey', 'zeus'],
        'clare': ['xavier', 'yancey', 'zeus']
    }

    the_preftie = {
        'xavier': [{'bertha'}, {'amy'}, {'clare'}],
        'yancey': [{'amy', 'bertha'}, {'clare'}],
        'zeus': [{'amy'}, {'bertha', 'clare'}],
        'amy': [{'zeus', 'xavier', 'yancey'}],
        'bertha': [{'zeus'}, {'xavier'}, {'yancey'}],
        'clare': [{'xavier', 'yancey'}, {'zeus'}]
    }

    blocked = {
        ('xavier', 'clare'),
        ('zeus', 'clare'),
        ('zeus', 'amy')
    }

    match = gs(the_men, the_women, the_pref)
    print(match)

    match_block = gs_block(the_men, the_women, the_pref, blocked)
    print(match_block)

    match_tie = gs_tie(the_men, the_women, the_preftie)
    print(match_tie)