import random

rolls = 100000
finals = [0 for x in range(40)]
CC = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2]
random.shuffle(CC)
CH = [0,0,0,0,0,0,1,2,3,4,5,6,7,8,9,10]
random.shuffle(CH)
place = 0
last2 = [(1,2),(3,4)]
roll = (0,0)
sides = 4

for i in range(rolls):
    random.seed()
    roll = (random.randint(1,sides),random.randint(1,sides))
    place = (place + sum(roll)) % 40
    #special conditions
    #3 doubles in a row
    if roll[0] == roll[1] and last2[0][0] == last2[0][1] and last2[1][0] == last2[1][1]:
        place = 10 #jail
    #G2J
    elif place == 30:
        place = 10
    #Community Chest
    elif place == 2 or place == 17 or place == 33:
        card = CC[0]
        #put card at bottom of deck
        for j in range(len(CC) - 1):
            CC[j] = CC[j+1]
        CC[len(CC) - 1] = card
        #advance to GO
        if card == 1:
            place = 0
        #go to jail
        elif card == 2:
            place = 10
        #else keep current place
    #chance cards
    elif place == 36 or place == 22 or place == 7:
        card = CH[0]
        #put card at bottom of deck
        for j in range(len(CH) - 1):
            CH[j] = CH[j+1]
        CH[len(CH) - 1] = card
        #advance to GO
        if card == 1:
            place = 0
        #go to jail
        elif card == 2:
            place = 10
        #go to C1
        elif card == 3:
            place = 11
        #go to H2
        elif card == 4:
            place = 39
        #go to E3
        elif card == 5:
            place = 24
        #go to R1
        elif card == 6:
            place == 5
        #go to next R
        elif card == 7 or card == 8:
            tmp = 35
            if place < 25:
                tmp = 25
                if place < 15:
                    tmp = 15
                    if place < 5 or place >= 35:
                        tmp = 5
            place = tmp
        #go to next U
        elif card == 9:
            tmp = 28
            if place < 12 or place >= 28:
                tmp = 12
            place = tmp
        #go back 3
        elif card == 10:
            place = (place - 3) % 40
    finals[place]+=1
    #shift rolls over
    last2[0] = last2[1]
    last2[1] = roll

print finals
m = max(finals)
print "ocurrences: %d, probability: %f, square: %d" % (m, float(m)/rolls, finals.index(m))
finals[finals.index(m)]=0
m = max(finals)
print "ocurrences: %d, probability: %f, square: %d" % (m, float(m)/rolls, finals.index(m))
finals[finals.index(m)]=0
m = max(finals)
print "ocurrences: %d, probability: %f, square: %d" % (m, float(m)/rolls, finals.index(m))
