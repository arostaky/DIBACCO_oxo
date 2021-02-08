import maya.cmds as cmds
cmds.file(f=True, new=True)
sc = cmds.internalVar(userScriptDir=True)
# 1 build 3x3 tic tac toe (oxo):
TTT = [[0,0,0],[0,0,0],[0,0,0]]
# print(TTT)

# # Petit test de jeu
# # Joueur 1 = 1
# # Joueur 2 = 2
# TTT[1][2]= 1
# TTT[2][2] = 2
# print (TTT)
pA = True
board = cmds.polyPlane( sx=3, sy=3, w=9, h=9, n="board")
# get board coords:
    
cmds.select('board')
nf = cmds.polyEvaluate(f=True)
print('nf: ' + str(nf))
Liste = []

for i in range(0,nf):
    Liste.append('board.f['+str(i)+']')
    #pos = cmds.xform(Liste[i],q=True,t= True, ws=True)

#fill the list of positions for X and Z:
x = []
z = []

for i in range(len(Liste)):
    pos = cmds.xform(Liste[i],q=True,t= True, ws=True)
    x.append((pos[0] + pos[3] + pos[6]+ pos[9])/4.0)
    z.append((pos[2] + pos[5] + pos[8]+ pos[11])/4.0)

#pos = cmds.xform(Liste[0],q=True,t= True, ws=True)
print(x[0])
print(z[0])
#--------------
someTrick = 0

def playerMove(pos):
     #print(pA)
     global someTrick
     someTrick = pos
     if pA == True:
        playerOne(pos)
     else:
        playerTwo(pos)

def playerOne(pos):
    if checkWin(1) == False and checkCanPlay(pos) == True:
        printTable(pos, 1)
        cmds.polyCube()
        cmds.move( x[pos], 0, z[pos] )
        changeLabelpA()
        global pA
        pA = False
    else:
        print('player Two wins')

def playerTwo(pos):
    if checkWin(2) == False and checkCanPlay(pos) == True:
        printTable(pos, 2)
        cmds.polyCylinder(r=0.5, h=0.5)
        cmds.move( x[pos], 0, z[pos] )
        changeLabelpB()
        global pA
        pA = True
    else:
        print('player One wins')


def printTable(pos, player):
    #break numbers into table:\
    print('pos: '+str(pos))
    global TTT
    if pos == 0 : TTT[0][0] = player
    elif pos == 1 : TTT[0][1] = player
    elif pos == 2 : TTT[0][2] = player
    elif pos == 3 : TTT[1][0] = player
    elif pos == 4 : TTT[1][1] = player
    elif pos == 5 : TTT[1][2] = player
    elif pos == 6 : TTT[2][0] = player
    elif pos == 7 : TTT[2][1] = player
    elif pos == 8 : TTT[2][2] = player
    else:
        print('cannot play')
    print(TTT)


def checkCanPlay(pos):
    if pos == 0 and TTT[0][0] == 0:return True
    elif pos == 1 and TTT[0][1] == 0:return True
    elif pos == 2 and TTT[0][2] == 0: return True
    elif pos == 3 and TTT[1][0] == 0:return  True
    elif pos == 4 and TTT[1][1] == 0:return True
    elif pos == 5 and TTT[1][2] == 0:return True
    elif pos == 6 and TTT[2][0] == 0:return True
    elif pos == 7 and TTT[2][1] == 0:return True
    elif pos == 8 and TTT[2][2] == 0:return True
    else: return False

def checkWin(player):
    if TTT[0][0] == player and TTT[0][1] == player and TTT[0][2] == player:return True
    elif  TTT[1][0] == player and TTT[1][1] == player and TTT[1][2] == player:return True
    elif  TTT[2][0] == player and TTT[2][1] == player and TTT[2][2] == player:return True
    elif  TTT[0][0] == player and TTT[1][0] == player and TTT[2][0] == player:return True
    elif  TTT[0][1] == player and TTT[1][1] == player and TTT[2][1] == player:return True
    elif  TTT[0][2] == player and TTT[1][2] == player and TTT[2][2] == player:return True
    elif  TTT[0][0] == player and TTT[1][1] == player and TTT[2][2] == player:return True
    elif  TTT[0][2] == player and TTT[1][1] == player and TTT[2][0] == player:return True
    else: return False

#---------------------------------------------------------------------------------------
def changeLabelpA(*_):
    cmds.text(playerLabel, label='Player One', font='boldLabelFont', e=True)
    cmds.nodeIconButton(btnAlign[someTrick], e= True, image1=sc +'/DIBACCO_oxo/X.png')
def changeLabelpB(*_):
    cmds.text(playerLabel, label='Player Two', font='boldLabelFont', e=True)
    cmds.nodeIconButton(btnAlign[someTrick], e= True, image1=sc +'/DIBACCO_oxo/0.png')
#---------------------------------------------------------------------------------------
winName = 'OXO'
backgroundColor = [40.0/255.0,35.0/255.0,39.0/255.0]
winWidth = 600 # set a target width and reference this when you specify width
if cmds.window(winName, exists=True):
    cmds.deleteUI(winName)
cmds.window(winName, width=winWidth, title='OXO', h=600,  bgc=(backgroundColor), tlb=True)
#reference to the main columnLayout
mainCL = cmds.columnLayout() 
mainRLWidth = [winWidth*0.5, winWidth*0.5]
playerLabel = cmds.text(label='Player One', font='boldLabelFont')
cmds.text(label='')
cmds.gridLayout( numberOfColumns=3, cellWidthHeight=(256, 256) )
btnAlign = []
for i in range(9):
    btnAlign.append(cmds.nodeIconButton( style='iconOnly', c='playerMove('+str(i)+')', image1=sc +'/DIBACCO_oxo/empty.png' ))
cmds.showWindow()