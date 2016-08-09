#Uploading to github

import random #For picking a random card

#Create a list of card values and suites
cardvalue = list(range(2, 11))
cardvalue = [str(i) for i in cardvalue]
cardvalue = cardvalue + ['J' , 'Q', 'K','A'] #Number and face cards
cardvalue = tuple(cardvalue)
cardsuite = ['H', 'D', 'C','S'] #Hearts, Diamonds, Clubs, Spades
cardsuite = tuple(cardsuite)
#Cards are made into tuples to try and make read only

#Default behavior is to generate the 5 cards starting with an empty hand
#Can also be used to fill up a hand if there are missing cards
def generateHand(hand =[], repcards=[]):
    while len(hand) < 5:
        value = random.choice(cardvalue) #Picks one from array
        suite = random.choice(cardsuite) #Picks one from array
        card = [value, suite]
        
        if card in hand or card in repcards:
            print(card , 'either in hand or replaced')
            continue
        
        else:
            hand.append(card)
    
    return hand

#Need to ask user how many cards to replace
#Deletes items to be replaced and generates hand again
def replaceHand(hand):
    
    repcards = [] #Keep track of cards to replace to avoid same cards

    #Loop for user input and validation on number of cards
    while True:
        repnum = input('Enter number of cards to replace:')
        try:
            repnum = int(repnum)
        except ValueError:
            print('Please enter a valid number between 0 and 5')
            continue
        if 0 <= repnum <= 5:
            break
        else:
            print('Number not between 0 and 5')
 
    print('Number validated: ', repnum)
    
    #Loop to replace each card
    while repnum > 0:
        print('Enter card to replace:')
        cardrep = input()
        cardrep = cardrep.split(' ')
        cardrep = [i.upper() for i in cardrep]

        #Replace card if found
        if cardrep in hand:
            print(cardrep, 'replaced')
            repcards.append(cardrep)
            hand.remove(cardrep)
            repnum -= 1

        else:
            print('Card', cardrep, 'not found')
    
    #Done with finding cards, update hand
    hand = generateHand(hand, repcards)
    print('Your new hand is:', hand)

    return hand

#Score hand, return points and name for hand
#I should make a list of all possible hands and see if accurate or any cause a crash.
#TODO Should I simply print the resulting hand? Maybe I should do a score based thing.
#	  Would make it easier to compare hands later. There's problem 54 on project Euler 
#     that I want to solve.
#TODO Add a script to add a text file with different cards and try out the function.
def scoreHand(hand):

    #Test for a flush
    flush = False
    straight = False
    suites = [i[1] for i in hand] #Take the suites from the cards

    #If equal to one, there are no different suites.
    if len(set(suites)) == 1:
        flush = True
        print('Hand is a flush')

    #Test for a straight
    values = (i[0] for i in hand) #Create a new list to score values
    values = sorted(values, key=cardvalue.index) #Use order of cardvalues
    acelow = list(cardvalue[0:4]) + ['A'] #Need to check acelow to 5


    #If substring of string already in order, hand is a straight.
    #Need to convert to string and remove the [] that comes from being a set (this looks ugly)
    
    if str(values).strip('[]') in str(cardvalue).strip('[]') or str(values).strip('[]') in str(acelow).strip('[]'):
        straight = True
        print('Straight found')

    else:
        print('No straight')


    #If Set is a straight no card matched. No reason to check next section of program.
    #TODO Add scoring here for straight, flush, and straight flush.


        

    #Hand should be sorted. Matches should be next to each other.
    #Currently 5 cards, no issues like unexisting three pair, or multiples of one card.
    #Would have to reconsider if adding holdem features or multiple cards.
	#How would I find the best possible 5 card hand out of the combinations?

	#2d array Groups of (a, b), a describes the card matched, b describes how many matches.
    #Initialize, matches. No more than 2 sets matching due to 5 cards.
    matches = [[0 for j in range(2)] for i in range(2)]

    #Weird quick fix. Check how to start at 0.
    #Scared of trying to access array[-1]
    #If it stays at -1 no matches. Could call it a feature lol.
    k = -1

    for i in range(0,4):
        if (values[i] == values[i+1]): #Found a match
            #Matched previous number
            if(values[i] == matches[k][0]):
                matches[k][1] += 1 #Increase count
        
            #New card match, next slot for matches
            else:
                k += 1 #Next Slot
                matches[k][0] = values[i] #Save number
                matches[k][1] += 1 #Increase count


    print(matches) # Double check how many matched.
    #TODO Add scoring here for pair, threes, fours, two pair, fullhouse, high card.

        
    
    
    print('Done scoring')

    return


if __name__== '__main__':

    hand = generateHand()
    print('Your hand is: ', hand)
    hand = replaceHand(hand)
    scoreHand(hand)
