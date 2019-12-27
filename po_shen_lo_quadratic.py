#!/usr/bin/python3

"""
This is an implementation of Professor Po Shen Loh's method of solving quadratics, in Python
This doesn't need any libraries :)


Dr Bob would be really proud because I put docstrings in my programs now :> lol
"""

def squareroooooooot(num):
    """
    Does what it says except without the ooooooo
    """
    return (num ** 0.5)

#good vibes coding because it's christmas :)
print("This only works if your quadratic is in standard form ax^2 + bx + c")

def main():
    #I'm talking to a girl on Tinder while coding this, jeez this is hard lol
    a = int(input('Please enter the value of A:')) #idon't even know why we ask for this A, 
    b = int(input('Please enter the value of B:')) #from the video this is the main thing that we use to solve, (x - _ ) , x(- _ )
    c = int(input('Please enter the value of C:'))
    #a = 2
    #b = -4
    #c = -5
    
    if a != 1:
        b = b /a
        c = c/ a

    print("A:{0}, B:{1}, C{2}".format(a, b, c))

    x = ( b / 2 ) ** 2 # -u2 = C #all becomes postive because it's squared eitherways. multiplied by itself)
    # 8 /2 = 4 squared is 16
    #(4 -u)(4 + u)

    roit_hand = c
    left_hand = x
    #16-u^2=18
    #this is okay from here

    #multiply by negative one for u to be positive
    roit_hand *= -1
    left_hand *= -1
    #-16+u^2=-18
    #this looks so noob
    #transfer left to right, so 
    if left_hand < 0: #is negative
        roit_hand = (abs(left_hand ) + roit_hand)
    else: #if still postive
        roit_hand = roit_hand - left_hand

    if type(squareroooooooot(roit_hand)) is complex:
        #proceed with the answer
        roit_hand = (str(abs(roit_hand)) + 'j')
        left_hand = (b/2) * -1
        print('({0}+sqrt({1})) ({0}-sqrt({1}))'.format(left_hand, roit_hand))
    else:
        left_hand = (b/2) * -1
        #print(left_hand)
        #print(roit_hand)
        roit_hand = roit_hand ** 0.5 #get the sqrt
        #print(roit_hand)
        
        #print(left_hand - roit_hand)
        #print(left_hand + roit_hand)
        print("Solution where right hand side is negative {0}".format(left_hand - roit_hand))
        print("Solution where right hand side is positive {0}".format(left_hand + roit_hand))


while True:
    main()