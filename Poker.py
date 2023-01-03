def printMenu(): 
    print("Menu")
    print("1. Show first 13 cards")
    print("2. Shuffle and show first 13 cards") 
    print("3. Play 2 card poker")
    print("4. Stack the deck and show first 13 cards") 
    print("5. Exit")
    return

def cardRanking(P1C1Val, P1C1Suit, P1C2Val, P1C2Suit,
                P2C1Val, P2C1Suit, P2C2Val, P2C2Suit):
    
    # determine rank of Player 1 Card 1 value
    if P1C1Val == '2':
        P1C1valRank = 1
    elif P1C1Val == '3':
        P1C1valRank = 2
    elif P1C1Val == '4':
        P1C1valRank = 3
    elif P1C1Val == '5':
        P1C1valRank = 4
    elif P1C1Val == '6':
        P1C1valRank = 5
    elif P1C1Val == '7':
        P1C1valRank = 6
    elif P1C1Val == '8':
        P1C1valRank = 7
    elif P1C1Val == '9':
        P1C1valRank = 8
    elif P1C1Val == '10':
        P1C1valRank = 9
    elif P1C1Val == 'J':
        P1C1valRank = 10
    elif P1C1Val == 'Q':
        P1C1valRank = 11
    elif P1C1Val == 'K':
        P1C1valRank = 12
    elif P1C1Val == 'A':
        P1C1valRank = 13

    # determine rank of Player 1 Card 1 suit
    if P1C1Suit == 'C':
        P1C1suitRank = 1
    elif P1C1Suit == 'D':
        P1C1suitRank = 2
    elif P1C1Suit == 'H':
        P1C1suitRank = 3
    elif P1C1Suit == 'S':
        P1C1suitRank = 4

    # determine rank of Player 1 Card 2 value
    if P1C2Val == '2':
        P1C2valRank = 1
    elif P1C2Val == '3':
        P1C2valRank = 2
    elif P1C2Val == '4':
        P1C2valRank = 3
    elif P1C2Val == '5':
        P1C2valRank = 4
    elif P1C2Val == '6':
        P1C2valRank = 5
    elif P1C2Val == '7':
        P1C2valRank = 6
    elif P1C2Val == '8':
        P1C2valRank = 7
    elif P1C2Val == '9':
        P1C2valRank = 8
    elif P1C2Val == '10':
        P1C2valRank = 9
    elif P1C2Val == 'J':
        P1C2valRank = 10
    elif P1C2Val == 'Q':
        P1C2valRank = 11
    elif P1C2Val == 'K':
        P1C2valRank = 12
    elif P1C2Val == 'A':
        P1C2valRank = 13

    # determine rank of Player 1 Card 2 suit
    if P1C2Suit == 'C':
        P1C2suitRank = 1
    elif P1C2Suit == 'D':
        P1C2suitRank = 2
    elif P1C2Suit == 'H':
        P1C2suitRank = 3
    elif P1C2Suit == 'S':
        P1C2suitRank = 4

    # determine rank of Player 2 Card 1 value
    if P2C1Val == '2':
        P2C1valRank = 1
    elif P2C1Val == '3':
        P2C1valRank = 2
    elif P2C1Val == '4':
        P2C1valRank = 3
    elif P2C1Val == '5':
        P2C1valRank = 4
    elif P2C1Val == '6':
        P2C1valRank = 5
    elif P2C1Val == '7':
        P2C1valRank = 6
    elif P2C1Val == '8':
        P2C1valRank = 7
    elif P2C1Val == '9':
        P2C1valRank = 8
    elif P2C1Val == '10':
        P2C1valRank = 9
    elif P2C1Val == 'J':
        P2C1valRank = 10
    elif P2C1Val == 'Q':
        P2C1valRank = 11
    elif P2C1Val == 'K':
        P2C1valRank = 12
    elif P2C1Val == 'A':
        P2C1valRank = 13

    # determine rank of Player 2 Card 1 suit
    if P2C1Suit == 'C':
        P2C1suitRank = 1
    elif P2C1Suit == 'D':
        P2C1suitRank = 2
    elif P2C1Suit == 'H':
        P2C1suitRank = 3
    elif P2C1Suit == 'S':
        P2C1suitRank = 4

    # determine rank of Player 2 Card 2 value
    if P2C2Val == '2':
        P2C2valRank = 1
    elif P2C2Val == '3':
        P2C2valRank = 2
    elif P2C2Val == '4':
        P2C2valRank = 3
    elif P2C2Val == '5':
        P2C2valRank = 4
    elif P2C2Val == '6':
        P2C2valRank = 5
    elif P2C2Val == '7':
        P2C2valRank = 6
    elif P2C2Val == '8':
        P2C2valRank = 7
    elif P2C2Val == '9':
        P2C2valRank = 8
    elif P2C2Val == '10':
        P2C2valRank = 9
    elif P2C2Val == 'J':
        P2C2valRank = 10
    elif P2C2Val == 'Q':
        P2C2valRank = 11
    elif P2C2Val == 'K':
        P2C2valRank = 12
    elif P2C2Val == 'A':
        P2C2valRank = 13
    
    # determine rank of Player 2 Card 1 suit
    if P2C2Suit == 'C':
        P2C2suitRank = 1
    elif P2C2Suit == 'D':
        P2C2suitRank = 2
    elif P2C2Suit == 'H':
        P2C2suitRank = 3
    elif P2C2Suit == 'S':
        P2C2suitRank = 4
    

    # determine the more valuable card of Player 1
    if P1C1valRank > P1C2valRank:
        P1mainValRank = P1C1valRank
        P1FightingCard = P1C1valRank + P1C1suitRank
        
    elif P1C2valRank > P1C1valRank:
        P1mainValRank = P1C2valRank
        P1FightingCard = P1C2valRank + P1C2suitRank

    else:
        P1mainValRank = P1C2valRank
        if P1C1suitRank > P1C2suitRank:
            P1FightingCard = P1C1valRank + P1C1suitRank
        else:
            P1FightingCard = P1C2valRank + P1C2suitRank

    # determine the more valuable card of Player 2
    if P2C1valRank > P2C2valRank:
        P2mainValRank = P2C1valRank
        P2FightingCard = P2C1valRank + P2C1suitRank

    elif P2C2valRank > P2C1valRank:
        P2mainValRank = P2C2valRank
        P2FightingCard = P2C2valRank + P2C2suitRank

    else:
        P2mainValRank = P2C2valRank
        if P2C1suitRank > P2C2suitRank:
            P2FightingCard = P2C1valRank + P2C1suitRank
        else:
            P2FightingCard = P2C2valRank + P2C2suitRank
        

    # determine who wins
    if P1C1valRank == P1C2valRank and P2C1valRank != P2C2valRank :
        print("P1 wins")
    elif P1C1valRank != P1C2valRank and P2C1valRank == P2C2valRank :
        print("P2 wins")
    elif P1mainValRank == P2mainValRank:
        if P1FightingCard > P2FightingCard:
            print("P1 wins")
        else:
            print("P2 wins")
    
    elif P1mainValRank > P2mainValRank:
        print("P1 wins")
    else:
        print("P2 wins")
    
    return 

def isValidInput(s):
    if s == '1' or s == '2' or s == '3' or s == '4' or s == '5':
        return True
    return False

def findSameCard(deck, newcard):
    sameCards = []
    ctr = 0
    while ctr < len(deck):
        if deck[ctr] == newcard:
            sameCards.append(ctr)
        if ctr == len(deck)-1:
            break
        ctr += 1

    return sameCards


suits = ['C', 'D', 'H', 'S']
value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
deck = []

for s in suits:
    for v in value:
        card = []
        card.append(v)
        card.append(s)
        deck.append(card)


i = 0
while True:
    printMenu()
    s = str(input())
    
    if (isValidInput(s) == False):
        print("Invalid input")
        
    if s == '1':

        ctr = 0

        if len(deck) >= len(value):
            while ctr < len(value):
                if ctr < len(value) - 1:
                    print('-'.join(deck[ctr]), end = ",")
                else:
                    print('-'.join(deck[ctr]))
                ctr += 1

        else:
            while ctr < len(deck):
                if ctr < len(deck) - 1:
                    print('-'.join(deck[ctr]), end = ",")
                else:
                    print('-'.join(deck[ctr]))
                ctr += 1


    elif s == '2':

        mid = int(len(deck) / 2)
        topHalf = 0
        bottomHalf = mid 

        tempDeck = []

        ctr = 0
        while ctr < len(deck):
            tempDeck.append(deck[ctr])
            ctr += 1
       
        ctr = 0
        while ctr < int(len(deck)):
            if ctr % 2 == 0:
                deck[ctr] = tempDeck[bottomHalf]
                bottomHalf += 1
            else:
                deck[ctr] = tempDeck[topHalf]
                topHalf += 1
            ctr += 1
        
        ctr = 0
        if len(deck) >= len(value):
            while ctr < len(value):
                if ctr < len(value) - 1:
                    print('-'.join(deck[ctr]), end = ",")
                else:
                    print('-'.join(deck[ctr]))
                ctr += 1

        else:
            while ctr < len(deck):
                if ctr < len(deck) - 1:
                    print('-'.join(deck[ctr]), end = ",")
                else:
                    print('-'.join(deck[ctr]))
                ctr += 1

    elif s == '3':

        c1 = 0 #card1
        c2 = 1 #card2
        c3 = 2 #card3
        c4 = 3 #card4
        v = 0  #value
        s = 1  #suit
        
        P1 = '-'.join(deck[0]), '-'.join(deck[2])
        P2 = '-'.join(deck[1]), '-'.join(deck[3])
        print("P1 cards:", ','.join(P1))
        print("P2 cards:", ','.join(P2))

        cardRanking(deck[c1][v], deck[c1][s], deck[c3][v], deck[c3][s], deck[c2][v], deck[c2][s], deck[c4][v], deck[c4][s])
        del deck[0:4]

  
    elif s == '4':
     
        newCards = str(input())
        newCards += ','
        
        c1 = []
        c2 = []
        c3 = []
        c4 = []

        ctr = 0
        while True:
            c1.append(newCards[ctr])
            if newCards[ctr+1] == ',':
                break
            ctr += 1

        ctr += 2
        while True:
            c2.append(newCards[ctr])
            if newCards[ctr+1] == ',':
                break
            ctr += 1

        ctr += 2
        while True:
            c3.append(newCards[ctr])
            if newCards[ctr+1] == ',':
                break
            ctr += 1

        ctr += 2
        while True:
            c4.append(newCards[ctr])
            if newCards[ctr+1] == ',':
                break
            ctr += 1
        

        # if the card value is 10, adjust the way we access the list
        if len(c1) == 4:
            c1.append("10")
            c1.append(c1[3])
            del c1[0:4]
        else:
            c1.append(c1[0])
            c1.append(c1[2])
            del c1[0:3]


        if len(c2) == 4:
            c2.append("10")
            c2.append(c2[3])
            del c2[0:4]
        else:
            c2.append(c2[0])
            c2.append(c2[2])
            del c2[0:3]


        if len(c3) == 4:
            c3.append("10")
            c3.append(c3[3])
            del c3[0:4]
        else:
            c3.append(c3[0])
            c3.append(c3[2])
            del c3[0:3]


        if len(c4) == 4:
            c4.append("10")
            c4.append(c4[3])
            del c4[0:4]
        else:
            c4.append(c4[0])
            c4.append(c4[2])
            del c4[0:3]
        

        found1 = findSameCard(deck, c1)

        ctr = 0
        if len(found1) > 0:
            while ctr < len(found1):
                del deck[found1[ctr]]
                ctr += 1

        found2 = findSameCard(deck, c2)

        ctr = 0
        if len(found2) > 0:
            while ctr < len(found2):
                del deck[found2[ctr]]
                ctr += 1

        found3 = findSameCard(deck, c3)

        ctr = 0
        if len(found3) > 0:
            while ctr < len(found3):
                del deck[found3[ctr]]
                ctr += 1

        found4 = findSameCard(deck, c4)

        ctr = 0
        if len(found4) > 0:
            while ctr < len(found4):
                del deck[found4[ctr]]
                ctr += 1
        

        insertNum = 1
        deck.insert(0, c1)
        if not c2 == c1:
            deck.insert(insertNum, c2)
            insertNum += 1
        if not c3 == c1 and not c3 == c2:
            deck.insert(insertNum, c3)
            insertNum += 1
        if not c4 == c1 and not c4 == c3 and not c4 == c2:
            deck.insert(insertNum, c4)
            insertNum += 1
        
        ctr = 0
        if len(deck) >= len(value):
            while ctr < len(value):
                if ctr < len(value) - 1:
                    print('-'.join(deck[ctr]), end = ",")
                else:
                    print('-'.join(deck[ctr]))
                ctr += 1
        else:
            while ctr < len(deck):
                if ctr < len(deck) - 1:
                    print('-'.join(deck[ctr]), end = ",")
                else:
                    print('-'.join(deck[ctr]))
                ctr += 1
                
    elif s == '5':
        break
        
    if isValidInput(s) == True:
        i += 1