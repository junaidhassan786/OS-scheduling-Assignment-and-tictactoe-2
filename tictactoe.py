c=[['1','2','3'],['4','5','6'],['7','8','9']]
def showBoard(c):
    print(c[0][0]+' | '+c[0][1]+ ' | ' + c[0][2])
    print(c[1][0]+' | '+c[1][1]+ ' | ' + c[1][2])
    print(c[2][0]+' | '+c[2][1]+ ' | ' + c[2][2])

def win_lose(p1,p2,b):
    bl=True
    s="none"
    for i in range(0,3): #rowwise checking
        c1=0
        c2=0
        for j in range(0,3):
            if c[i][j] == p1:
                c1=c1+1
            if c[i][j] == p2:
                c2=c2+1
        if c1==3:
            s="player1 wins"
            #print(s)
            b=False
        elif c2==3:
            s="player2 wins"
            #print(s)
            b=False
    for i in range(0,3): #columnwise checking
        c1=0
        c2=0
        for j in range(0,3):
            if c[j][i] == p1:
                c1=c1+1
            if c[j][i] == p2:
                c2=c2+1
        if c1==3:
            s="player1 wins"
            #print(s)
            b=False
        elif c2==3:
            s="player2 wins"
            #print(s)
            b=False
    c1=0
    c2=0
    for i in range(0,3):# L to R diagnol check
        if c[i][i] == p1:
            c1=c1+1
        if c[i][i] == p2:
            c2=c2+1
    if c1==3:
        s="player1 wins"
        #print(s)
        b=False
    elif c2==3:
        s="player2 wins"
        #print(s)
        b=False
    # R to L diagnol Check
    if c[0][2]==p1 and c[1][1]==p1 and c[2][0]==p1:
        s="player1 wins"
        #print(s)
        b=False
    elif c[0][2]==p2 and c[1][1]==p2 and c[2][0]==p2:
        s="player2 wins"
        #print(s)
        b=False
    if s=="player1 wins" or s=="player2 wins":
        bl=False
    if(bl):
        d=0
        for i in range(0,3):
            for j in range(0,3):
                if c[i][j] != p1 and c[i][j]!=p2:
                    d=d+1
        if d==1:
            print("Game tie, no winner !!")
            b=False
        else:
            showBoard(c)
    else:
        print(s);
def main():
    showBoard(c)
    choice=raw_input("Player1 enter your choice X or O : ")#raw_input() function is use for taking string as input.
    player1=''
    player2=''
    if choice == 'X' :
        player1='X'
        player2='O'
    else:
        player2='X'
        player1='O'
    print ("Player2 will play with "+player2)
    pos1=0
    pos2=0
    index1=0
    index2=0
    b=True
    while(b):
        pos1=input("Player 1 enter position from 1 to 9 : ")
        pos2=input("Player 2 enter position from 1 to 9 : ")
        if pos1 == pos2 :
            print("Both players enter same position!!")
        else:
            #for player 1
            if pos1 <= 3 :
                index1=pos1-1
                if c[0][index1] == 'X' or  c[0][index1] == 'O' :
                    print("this position is already marked!!")
                else:
                    c[0][index1]=player1;
            if pos1>3 and pos1<=6:
                index1=pos1-4
                if c[1][index1] == 'X' or  c[1][index1] == 'O' :
                    print("this position is already marked!!")
                else:
                    c[1][index1]=player1;
            if pos1>6 and pos1<=9:
                index1=pos1-7
                if c[2][index1] == 'X' or  c[2][index1] == 'O' :
                    print("this position is already marked!!")
                else:
                    c[2][index1]=player1;
            # for player 2
            if pos2 <= 3 :
                index2=pos2-1
                if c[0][index2] == 'X' or  c[0][index2] == 'O' :
                    print("this position is already marked!!")
                else:
                    c[0][index2]=player2;
            if pos2>3 and pos2<=6:
                index2=pos2-4
                if c[1][index2] == 'X' or  c[1][index2] == 'O' :
                    print("this position is already marked!!")
                else:
                    c[1][index2]=player2;
            if pos2>6 and pos2<=9:
                index2=pos2-7
                if c[2][index2] == 'X' or  c[2][index2] == 'O' :
                    print("this position is already marked!!")
                else:
                    c[2][index2]=player2;
        if pos1<1 or pos1>9:
            print("Player1 value is out of range !! ")
        if pos2<1 or pos2>9:
            print("Player2 value is out of range !! ")
        if c[0][0]!='1' and c[0][1]!='2' and c[0][2]!='3' and c[1][0]!='4' and c[1][1]!='5' and c[1][2]!='6' and c[2][0]!='7' and c[2][1]!='8' and c[2][2]!='9' :
            print("\n I am calling \n")
            b=False
        win_lose(player1,player2,b)
main()