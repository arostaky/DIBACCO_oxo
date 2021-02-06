import maya.cmds as cmds
from functools import partial
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
#playerA = cmds.polyCube()
# cmds.move( x[0], 0, z[0] )
#playerB = cmds.polyCylinder(r=0.7, h=0.01)
# cmds.move( x[1], 0, z[1] )

def playerAmove(pos):
     cmds.polyCube()
     cmds.move( x[pos], 0, z[pos] )
     changeLabel()
def changeLabel(*_):
    cmds.nodeIconButton(btnAlignX, e= True, image1='polyPlanProjLarge.png')
winName = 'OXO'
backgroundColor = [40.0/255.0,35.0/255.0,39.0/255.0]
winWidth = 600 # set a target width and reference this when you specify width
if cmds.window(winName, exists=True):
    cmds.deleteUI(winName)
cmds.window(winName, width=winWidth, title='OXO', h=200,  bgc=(backgroundColor), tlb=True)
#reference to the main columnLayout
mainCL = cmds.columnLayout() 
mainRLWidth = [winWidth*0.4, winWidth*0.8]
mainRL = cmds.rowLayout(w=winWidth, numberOfColumns=2, columnWidth2=mainRLWidth, rowAttach=(2, 'top', 0))

cmds.columnLayout(w=mainRLWidth[0]) # create a columnLayout under the first row of mainRL
cmds.text(label='Player A', font='boldLabelFont')
cmds.text(label='')
#btnAlignX = cmds.button(label='X', c='playerAmove(1)')
btnAlignX = cmds.nodeIconButton( style='iconOnly', c=changeLabel, image1='sphere.png' )
# cmds.button(label='runFirst', width=mainRLWidth[1]*0.95, height=70, c='buildVariables()')
# cmds.iconTextButton(style='iconAndTextVertical', image1=sc + '/icons/2x/comode.png', label=' Comode',width=mainRLWidth[1]*0.5, c=lambda:comode())
cmds.setParent('..') # this will exit the rowLayout back to the mainRL, same as cmds.setParent(mainRL)

cmds.columnLayout(width=mainRLWidth[1]) # start another vertical layout
check1 = cmds.checkBox(label='One')
check2 = cmds.checkBox(label='Two')
check3 = cmds.checkBox(label='Three')
cmds.showWindow() 