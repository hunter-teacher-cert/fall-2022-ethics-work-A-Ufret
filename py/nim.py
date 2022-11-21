# FILENAME: nim.py
# First Last: Ashley Ufret
# CSCI 77800 Fall 2022
# collaborators: 
# consulted: 

class Nim(object):
   
    @classmethod
    def main(cls, args):
  \
        stones = 12
        stonesTaken = int()
        # declaring this...user will give value
        input = Scanner(System.in_)
        # loop until game ends
        while stones > 0:
            # prompt user input
            print ("There are " + stones + " stones in the pile.  How many would you like to take? You may take 1, 2, or 3 stones")
            stonesTaken = input.nextInt()
            # calculate number of stones remaining, print
            stones = stones - stonesTaken
            print ("You took " + stonesTaken + ". There are now " + stones + " stones left in the pile. ")
            # check for win
            if stones == 0:
                print ("You took the last stone! You won!")
            else:
                # machine turn
                if stones > 3:
                    stonesTaken = random.nextInt(3) + 1
                else:
                    stonesTaken = 3
                # calculate number of stones remaining, print
                stones = stones - stonesTaken
                print ("The machine took " + stonesTaken + " stones. There are now " + stones + " stones left in the pile. ")
                # check win
                if stones == 0:
                    print ("The machine took the last stone! You lost!")
