#!/usr/bin/env python3

import sys #couldnt find a use case , too lazy to delete

#representation of a tic-tac-toe board
theboard={
    'top-l':"",'top-mid':"",'top-r':"",
    'mid-l':'','mid-mid':'','mid-r':'',
    'dwn-l':'','dwn-mid':'','dwn-r':''
}

def printboard(board):
    '''
     function to print the state of the game after each play

     '''

    print(theboard['top-l']+"\t|"+theboard['top-mid']+"\t|"+theboard["top-r"])
    print("-----------------------------")
    print(theboard['mid-l']+"\t|"+theboard['mid-mid']+"\t|"+theboard['mid-r'])
    print("-----------------------------")
    print(theboard['dwn-l']+"\t|"+theboard['dwn-mid']+"\t|"+theboard['dwn-r'])
    print("-----------------------------")


printboard(theboard)


def instruction():
    print("\n < == >instructions< == >")
    print("\"top-l\", \"top-mid\", \"top-r\" for top left, middle, or right "\
    "position")

    print("\"mid-l\", \"mid-mid\", \"mid-r\" to fill the middle "\
    "positions respectively")

    print("\"dwn-r\", \"ndwn-mid\", \"dwn-l\" to fill the bottomd "\
    "boards" )

    print("\n  < == >tips< == >")
    print("\"mid-l\" means the middle left board and \"dwn-l\" means the "\
    "downmost-left board\n")


instruction()


printboard(theboard)

def check_win_x(theboard):
    #this is a very terrible line of code , i know
    if((theboard['top-l']=="x" and theboard['top-r']=='x' and theboard['top-mid']=='x') or \
    (theboard['mid-l']=='x' and theboard['mid-mid']=='x' and theboard['mid-r']=='x') or \
    (theboard['dwn-r']=='x' and theboard['dwn-l']=='x' and theboard['dwn-mid']=='x') or \
    (theboard['top-l']=='x' and theboard['mid-l']=='x' and theboard['dwn-l']=='x') or \
    (theboard['top-mid']=='x' and theboard['mid-mid']=='x' and theboard['dwn-mid']=='x') or \
    (theboard['top-r']=='x' and theboard['mid-r']=='x' and theboard['dwn-r']=='x') or \
    (theboard['top-r']=='x' and theboard['mid-mid']=='x' and theboard['dwn-l']=='x') or \
    (theboard['top-l']=='x' and theboard['mid-mid']=='x' and theboard['dwn-r']=='x')):
      print("playerX is the winner")
      return True




def check_win_o(theboard):
    #another  of the terrible code above
    if((theboard['top-l']=="o" and theboard['top-r']=='o' and theboard['top-mid']=='o') or \
      (theboard['mid-l']=='o' and theboard['mid-mid']=='o' and theboard['mid-r']=='o') or \
      (theboard['dwn-r']=='o' and theboard['dwn-l']=='o' and theboard['dwn-mid']=='o') or \
      (theboard['top-l']=='o' and theboard['mid-l']=='o' and theboard['dwn-l']=='o') or \
      (theboard['top-mid']=='o' and theboard['mid-mid']=='o' and theboard['dwn-mid']=='o') or \
      (theboard['top-r']=='o' and theboard['mid-r']=='o' and theboard['dwn-r']=='o') or \
      (theboard['top-r']=='o' and theboard['mid-mid']=='o' and theboard['dwn-l']=='o') or \
      (theboard['top-l']=='o' and theboard['mid-mid']=='o' and theboard['dwn-r']=='o')):
        print("playerO is the winner")
        return True


print()

def no_more_moves(theboard):
    if "" not in theboard.values():

        return True
    return False
while(True):


   try:
       #check if any move is till possible else end the game
    if(no_more_moves(theboard)):
        break




    xturn= input("playerX  enter your position : ")

    if(theboard[xturn]!=''):  #reject input if the location is not empy
       print("**************************************\n")
       print("you can overide an already played box")
       print("****************")
       printboard(theboard)
       contin
    theboard[xturn]="x" #set the location entered to X

    printboard(theboard)

    #check for possible moves , if none end the game

    if(no_more_moves(theboard)):
        print("\n!!no more move possible, game ended in a DRAW")
        break


    if(check_win_x(theboard)):
       break

    Oturn=input("playerO enter your position : ")

    if(theboard[Oturn]!=''):
       print("**************************************\n")
       print("you can overide an already played box")
       print("this will cause x to play ahead of you")
       print("****************")
       printboard(theboard)


    theboard[Oturn]='o' #set the location to "o" as enterd by player0

    printboard(theboard)

    if(check_win_o(theboard)):
       print("\n!!no more move possible, game ended in a DRAW")
       break

    #handle wrong location error
   except KeyError:
       print("wrong location")
       print("read instruction\n")

       instruction()
