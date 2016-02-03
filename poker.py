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

#Default behavior is to generate the 5 cars starting with an empty hand
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
def scoreHand(hand):

    #Test for a flush
    flush = False
    straight = False
    suites = [i[1] for i in hand] #Take the suites from the cards

    # If equal to one, there are no different suites.
    if len(set(suites)) == 1:
        flush = True
        print('Hand is a flush')

    #Test for a straight
    values = [i[0] for i in hand] #Create a new list to score values
    values = sorted(values, key=cardvalue.index) #Use order of cardvalues
    acelow = list(cardvalue[0:4]) + ['A'] #Need to check acelow to 5
    if values in cardvalue or values in acelow:
        straight = True
        print('Straight found')
    
    print('Done scoring')

    return


if __name__== '__main__':

    hand = generateHand()
    print('Your hand is: ', hand)
    hand = replaceHand(hand)
    scoreHand(hand)
