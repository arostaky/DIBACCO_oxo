import maya.cmds as cmds
cmds.file(f=True, new=True)
# 1 build 3x3 tic tac toe (oxo):
TTT = [[0,0,0],[0,0,0],[0,0,0]]
print(TTT)

# Petit test de jeu
# Joueur 1 = 1
# Joueur 2 = 2
TTT[1][2]= 1
TTT[2][2] = 2
print (TTT)

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
#x = (pos[0] + pos[3] + pos[6]+ pos[9])/4.0
#y = (pos[1] + pos[4] + pos[7]+ pos[10])/4.0
#z = (pos[2] + pos[5] + pos[8]+ pos[11])/4.0
#---------------
# small move test:
playerA = cmds.polyCube()
cmds.move( x[0], 0, z[0] )
playerB = cmds.polyCylinder(r=0.5, h=0.01)
cmds.move( x[1], 0, z[1] )

