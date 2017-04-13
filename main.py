import sys
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
print("instructions: enter top-r,top-mid ,top-l for right,middle and left position to fill the board")
print("instructions: enter mid-l , mid-mid, mid-r  to fill the middle positions respectively")
print("instructions: enter dwn-r ndwn-mid, dwn-l to fill the bottomd boards" )
print("tips: mid-l means the middle left board and dwn-l means the downmost-letf board")
printboard(theboard)

def check_win_x(theboard):
    #this is a very terrible line of code , i know
     if((theboard['top-l']=="x" and theboard['top-r']=='x' and theboard['top-mid']=='x') or (theboard['mid-l']=='x' and theboard['mid-mid']=='x' and theboard['mid-r']=='x') or (theboard['dwn-r']=='x' and theboard['dwn-l']=='x' and theboard['dwn-mid']=='x') or (theboard['top-l']=='x' and theboard['mid-l']=='x' and theboard['dwn-l']=='x') or (theboard['top-mid']=='x' and theboard['mid-mid']=='x' and theboard['dwn-mid']=='x') or(theboard['top-r']=='x' and theboard['mid-r']=='x' and theboard['dwn-r']=='x') or(theboard['top-r']=='x' and theboard['mid-mid']=='x' and theboard['dwn-l']=='x') or (theboard['top-l']=='x' and theboard['mid-mid']=='x' and theboard['dwn-r']=='x')):
       print("playerX is the winner")
       return True
        



def check_win_o(theboard):
     if((theboard['top-l']=="o" and theboard['top-r']=='o' and theboard['top-mid']=='o') or (theboard['mid-l']=='o' and theboard['mid-mid']=='o' and theboard['mid-r']=='o') or (theboard['dwn-r']=='o' and theboard['dwn-l']=='o' and theboard['dwn-mid']=='o') or (theboard['top-l']=='o' and theboard['mid-l']=='o' and theboard['dwn-l']=='o') or (theboard['top-mid']=='o' and theboard['mid-mid']=='o' and theboard['dwn-mid']=='o') or(theboard['top-r']=='o' and theboard['mid-r']=='o' and theboard['dwn-r']=='o') or(theboard['top-r']=='o' and theboard['mid-mid']=='o' and theboard['dwn-l']=='o') or (theboard['top-l']=='o' and theboard['mid-mid']=='o' and theboard['dwn-r']=='o')):
       print("playerO is the winner")
       return True
        
    
print()
while(True):
   xturn= input("playerX  enter your position : ")
   theboard[xturn]="x"
   printboard(theboard)
   if(check_win_x(theboard)):
       break
   Oturn=input("playerO enter your position : ")
   theboard[Oturn]='o'
   printboard(theboard)
   if(check_win_o(theboard)):
       break
   #check for winning states 
  