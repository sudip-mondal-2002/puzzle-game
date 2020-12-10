from tkinter import Button,Tk
import random
global startend,wordlist
charlist=[['x', 'x', 'x', 'x', 'x', 'g', 'x', 'x', 'l', 'x'],
          ['x', 'r', 'x', 'x', 'p', 'x', 'o', 'l', 'x', 'x'],
          ['x', 'e', 'x', 'x', 'l', 'x', 'u', 'o', 'x', 'x'],
          ['x', 'w', 'x', 'x', 'e', 'p', 'x', 'x', 'd', 'x'],
          ['x', 'o', 'x', 'x', 'a', 'x', 'x', 'x', 'x', 'x'],
          ['x', 't', 'x', 'x', 's', 'n', 'i', 'c', 'e', 'x'],
          ['x', 'x', 'x', 'x', 'a', 'h', 'x', 'x', 'x', 'x'],
          ['k', 'o', 'o', 'c', 'n', 'x', 'g', 'x', 'x', 'x'],
          ['x', 'x', 'x', 'x', 't', 'x', 'x', 'i', 'x', 'x'],
          ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'h', 'x']]
for i in charlist:
    for j in range(10):
        if i[j]=='x':
            i[j]=chr(random.randint(97,122))
x=open('words.txt','r')
wordlist=[i[:-1] for i in x.readlines()]
startend=None
def check(but):
    global startend,wordlist
    if startend==None:
        startend=but
        but['bg']="green"
    else:
        x=butpos[startend]
        y=butpos[but]
        startend=None
        s=''
        if x[0]==y[0]:
            t=x[0]
            temp=[]
            if x[1]<y[1]:
                for i in range(y[1]-x[1]+1):
                    s+=str(posbut[t,x[1]+i]['text'])
                    temp.append(posbut[t,x[1]+i])
            if x[1]>y[1]:
                for i in range(x[1]-y[1]+1):
                    s+=str(posbut[t,x[1]-i]['text'])
                    temp.append(posbut[t,x[1]-i])
        if x[1]==y[1]:
            t=x[1]
            temp=[]
            if x[0]<y[0]:
                for i in range(y[0]-x[0]+1):
                    s+=str(posbut[x[0]+i,t]['text'])
                    temp.append(posbut[x[0]+i,t])
            if x[0]>y[0]:
                for i in range(x[0]-y[0]+1):
                    s+=str(posbut[x[0]-i,t]['text'])
                    temp.append(posbut[x[0]-i,t])
        elif x[1]-y[1]==x[0]-y[0] or x[1]-y[1]==y[0]-x[0]:
            temp=[]
            if x[1]<y[1] and x[0]<y[0]:
                for i in range(y[0]-x[0]+1):
                    s+=str(posbut[x[0]+i,x[1]+i]['text'])
                    temp.append(posbut[x[0]+i,x[1]+i])
            elif x[1]<y[1] and x[0]>y[0]:
                for i in range(y[1]-x[1]+1):
                    s+=str(posbut[x[0]-i,x[1]+i]['text'])
                    temp.append(posbut[x[0]-i,x[1]+i])
            elif x[1]>y[1] and x[0]<y[0]:
                for i in range(y[0]-x[0]+1):
                    s+=str(posbut[x[0]+i,x[1]-i]['text'])
                    temp.append(posbut[x[0]+i,x[1]-i])
            elif x[1]>y[1] and x[0]>y[0]:
                for i in range(x[1]-y[1]+1):
                    s+=str(posbut[x[0]-i,x[1]-i]['text'])
                    temp.append(posbut[x[0]-i,x[1]-i])

        if s not in wordlist:
            posbut[tuple(x)]['bg']="powder blue"
        else:
            for i in temp:
                i['bg']='green'
                
                    
                
tk=Tk()
button00=Button(tk,text=charlist[0][0],bg="powder blue",height=1,width=3,command=lambda:check(button00))
button01=Button(tk,text=charlist[0][1],bg="powder blue",height=1,width=3,command=lambda:check(button01))
button02=Button(tk,text=charlist[0][2],bg="powder blue",height=1,width=3,command=lambda:check(button02))
button03=Button(tk,text=charlist[0][3],bg="powder blue",height=1,width=3,command=lambda:check(button03))
button04=Button(tk,text=charlist[0][4],bg="powder blue",height=1,width=3,command=lambda:check(button04))
button05=Button(tk,text=charlist[0][5],bg="powder blue",height=1,width=3,command=lambda:check(button05))
button06=Button(tk,text=charlist[0][6],bg="powder blue",height=1,width=3,command=lambda:check(button06))
button07=Button(tk,text=charlist[0][7],bg="powder blue",height=1,width=3,command=lambda:check(button07))
button08=Button(tk,text=charlist[0][8],bg="powder blue",height=1,width=3,command=lambda:check(button08))
button09=Button(tk,text=charlist[0][9],bg="powder blue",height=1,width=3,command=lambda:check(button09))
button10=Button(tk,text=charlist[1][0],bg="powder blue",height=1,width=3,command=lambda:check(button10))
button11=Button(tk,text=charlist[1][1],bg="powder blue",height=1,width=3,command=lambda:check(button11))
button12=Button(tk,text=charlist[1][2],bg="powder blue",height=1,width=3,command=lambda:check(button12))
button13=Button(tk,text=charlist[1][3],bg="powder blue",height=1,width=3,command=lambda:check(button13))
button14=Button(tk,text=charlist[1][4],bg="powder blue",height=1,width=3,command=lambda:check(button14))
button15=Button(tk,text=charlist[1][5],bg="powder blue",height=1,width=3,command=lambda:check(button15))
button16=Button(tk,text=charlist[1][6],bg="powder blue",height=1,width=3,command=lambda:check(button16))
button17=Button(tk,text=charlist[1][7],bg="powder blue",height=1,width=3,command=lambda:check(button17))
button18=Button(tk,text=charlist[1][8],bg="powder blue",height=1,width=3,command=lambda:check(button18))
button19=Button(tk,text=charlist[1][9],bg="powder blue",height=1,width=3,command=lambda:check(button19))
button20=Button(tk,text=charlist[2][0],bg="powder blue",height=1,width=3,command=lambda:check(button20))
button21=Button(tk,text=charlist[2][1],bg="powder blue",height=1,width=3,command=lambda:check(button21))
button22=Button(tk,text=charlist[2][2],bg="powder blue",height=1,width=3,command=lambda:check(button22))
button23=Button(tk,text=charlist[2][3],bg="powder blue",height=1,width=3,command=lambda:check(button23))
button24=Button(tk,text=charlist[2][4],bg="powder blue",height=1,width=3,command=lambda:check(button24))
button25=Button(tk,text=charlist[2][5],bg="powder blue",height=1,width=3,command=lambda:check(button25))
button26=Button(tk,text=charlist[2][6],bg="powder blue",height=1,width=3,command=lambda:check(button26))
button27=Button(tk,text=charlist[2][7],bg="powder blue",height=1,width=3,command=lambda:check(button27))
button28=Button(tk,text=charlist[2][8],bg="powder blue",height=1,width=3,command=lambda:check(button28))
button29=Button(tk,text=charlist[2][9],bg="powder blue",height=1,width=3,command=lambda:check(button29))
button30=Button(tk,text=charlist[3][0],bg="powder blue",height=1,width=3,command=lambda:check(button30))
button31=Button(tk,text=charlist[3][1],bg="powder blue",height=1,width=3,command=lambda:check(button31))
button32=Button(tk,text=charlist[3][2],bg="powder blue",height=1,width=3,command=lambda:check(button32))
button33=Button(tk,text=charlist[3][3],bg="powder blue",height=1,width=3,command=lambda:check(button33))
button34=Button(tk,text=charlist[3][4],bg="powder blue",height=1,width=3,command=lambda:check(button34))
button35=Button(tk,text=charlist[3][5],bg="powder blue",height=1,width=3,command=lambda:check(button35))
button36=Button(tk,text=charlist[3][6],bg="powder blue",height=1,width=3,command=lambda:check(button36))
button37=Button(tk,text=charlist[3][7],bg="powder blue",height=1,width=3,command=lambda:check(button37))
button38=Button(tk,text=charlist[3][8],bg="powder blue",height=1,width=3,command=lambda:check(button38))
button39=Button(tk,text=charlist[3][9],bg="powder blue",height=1,width=3,command=lambda:check(button39))
button40=Button(tk,text=charlist[4][0],bg="powder blue",height=1,width=3,command=lambda:check(button40))
button41=Button(tk,text=charlist[4][1],bg="powder blue",height=1,width=3,command=lambda:check(button41))
button42=Button(tk,text=charlist[4][2],bg="powder blue",height=1,width=3,command=lambda:check(button42))
button43=Button(tk,text=charlist[4][3],bg="powder blue",height=1,width=3,command=lambda:check(button43))
button44=Button(tk,text=charlist[4][4],bg="powder blue",height=1,width=3,command=lambda:check(button44))
button45=Button(tk,text=charlist[4][5],bg="powder blue",height=1,width=3,command=lambda:check(button45))
button46=Button(tk,text=charlist[4][6],bg="powder blue",height=1,width=3,command=lambda:check(button46))
button47=Button(tk,text=charlist[4][7],bg="powder blue",height=1,width=3,command=lambda:check(button47))
button48=Button(tk,text=charlist[4][8],bg="powder blue",height=1,width=3,command=lambda:check(button48))
button49=Button(tk,text=charlist[4][9],bg="powder blue",height=1,width=3,command=lambda:check(button49))
button50=Button(tk,text=charlist[5][0],bg="powder blue",height=1,width=3,command=lambda:check(button50))
button51=Button(tk,text=charlist[5][1],bg="powder blue",height=1,width=3,command=lambda:check(button51))
button52=Button(tk,text=charlist[5][2],bg="powder blue",height=1,width=3,command=lambda:check(button52))
button53=Button(tk,text=charlist[5][3],bg="powder blue",height=1,width=3,command=lambda:check(button53))
button54=Button(tk,text=charlist[5][4],bg="powder blue",height=1,width=3,command=lambda:check(button54))
button55=Button(tk,text=charlist[5][5],bg="powder blue",height=1,width=3,command=lambda:check(button55))
button56=Button(tk,text=charlist[5][6],bg="powder blue",height=1,width=3,command=lambda:check(button56))
button57=Button(tk,text=charlist[5][7],bg="powder blue",height=1,width=3,command=lambda:check(button57))
button58=Button(tk,text=charlist[5][8],bg="powder blue",height=1,width=3,command=lambda:check(button58))
button59=Button(tk,text=charlist[5][9],bg="powder blue",height=1,width=3,command=lambda:check(button59))
button60=Button(tk,text=charlist[6][0],bg="powder blue",height=1,width=3,command=lambda:check(button60))
button61=Button(tk,text=charlist[6][1],bg="powder blue",height=1,width=3,command=lambda:check(button61))
button62=Button(tk,text=charlist[6][2],bg="powder blue",height=1,width=3,command=lambda:check(button62))
button63=Button(tk,text=charlist[6][3],bg="powder blue",height=1,width=3,command=lambda:check(button63))
button64=Button(tk,text=charlist[6][4],bg="powder blue",height=1,width=3,command=lambda:check(button64))
button65=Button(tk,text=charlist[6][5],bg="powder blue",height=1,width=3,command=lambda:check(button65))
button66=Button(tk,text=charlist[6][6],bg="powder blue",height=1,width=3,command=lambda:check(button66))
button67=Button(tk,text=charlist[6][7],bg="powder blue",height=1,width=3,command=lambda:check(button67))
button68=Button(tk,text=charlist[6][8],bg="powder blue",height=1,width=3,command=lambda:check(button68))
button69=Button(tk,text=charlist[6][9],bg="powder blue",height=1,width=3,command=lambda:check(button69))
button70=Button(tk,text=charlist[7][0],bg="powder blue",height=1,width=3,command=lambda:check(button70))
button71=Button(tk,text=charlist[7][1],bg="powder blue",height=1,width=3,command=lambda:check(button71))
button72=Button(tk,text=charlist[7][2],bg="powder blue",height=1,width=3,command=lambda:check(button72))
button73=Button(tk,text=charlist[7][3],bg="powder blue",height=1,width=3,command=lambda:check(button73))
button74=Button(tk,text=charlist[7][4],bg="powder blue",height=1,width=3,command=lambda:check(button74))
button75=Button(tk,text=charlist[7][5],bg="powder blue",height=1,width=3,command=lambda:check(button75))
button76=Button(tk,text=charlist[7][6],bg="powder blue",height=1,width=3,command=lambda:check(button76))
button77=Button(tk,text=charlist[7][7],bg="powder blue",height=1,width=3,command=lambda:check(button77))
button78=Button(tk,text=charlist[7][8],bg="powder blue",height=1,width=3,command=lambda:check(button78))
button79=Button(tk,text=charlist[7][9],bg="powder blue",height=1,width=3,command=lambda:check(button79))
button80=Button(tk,text=charlist[8][0],bg="powder blue",height=1,width=3,command=lambda:check(button80))
button81=Button(tk,text=charlist[8][1],bg="powder blue",height=1,width=3,command=lambda:check(button81))
button82=Button(tk,text=charlist[8][2],bg="powder blue",height=1,width=3,command=lambda:check(button82))
button83=Button(tk,text=charlist[8][3],bg="powder blue",height=1,width=3,command=lambda:check(button83))
button84=Button(tk,text=charlist[8][4],bg="powder blue",height=1,width=3,command=lambda:check(button84))
button85=Button(tk,text=charlist[8][5],bg="powder blue",height=1,width=3,command=lambda:check(button85))
button86=Button(tk,text=charlist[8][6],bg="powder blue",height=1,width=3,command=lambda:check(button86))
button87=Button(tk,text=charlist[8][7],bg="powder blue",height=1,width=3,command=lambda:check(button87))
button88=Button(tk,text=charlist[8][8],bg="powder blue",height=1,width=3,command=lambda:check(button88))
button89=Button(tk,text=charlist[8][9],bg="powder blue",height=1,width=3,command=lambda:check(button89))
button90=Button(tk,text=charlist[9][0],bg="powder blue",height=1,width=3,command=lambda:check(button90))
button91=Button(tk,text=charlist[9][1],bg="powder blue",height=1,width=3,command=lambda:check(button91))
button92=Button(tk,text=charlist[9][2],bg="powder blue",height=1,width=3,command=lambda:check(button92))
button93=Button(tk,text=charlist[9][3],bg="powder blue",height=1,width=3,command=lambda:check(button93))
button94=Button(tk,text=charlist[9][4],bg="powder blue",height=1,width=3,command=lambda:check(button94))
button95=Button(tk,text=charlist[9][5],bg="powder blue",height=1,width=3,command=lambda:check(button95))
button96=Button(tk,text=charlist[9][6],bg="powder blue",height=1,width=3,command=lambda:check(button96))
button97=Button(tk,text=charlist[9][7],bg="powder blue",height=1,width=3,command=lambda:check(button97))
button98=Button(tk,text=charlist[9][8],bg="powder blue",height=1,width=3,command=lambda:check(button98))
button99=Button(tk,text=charlist[9][9],bg="powder blue",height=1,width=3,command=lambda:check(button99))
button00.grid(row=0,column=0)
button01.grid(row=0,column=1)
button02.grid(row=0,column=2)
button03.grid(row=0,column=3)
button04.grid(row=0,column=4)
button05.grid(row=0,column=5)
button06.grid(row=0,column=6)
button07.grid(row=0,column=7)
button08.grid(row=0,column=8)
button09.grid(row=0,column=9)
button10.grid(row=1,column=0)
button11.grid(row=1,column=1)
button12.grid(row=1,column=2)
button13.grid(row=1,column=3)
button14.grid(row=1,column=4)
button15.grid(row=1,column=5)
button16.grid(row=1,column=6)
button17.grid(row=1,column=7)
button18.grid(row=1,column=8)
button19.grid(row=1,column=9)
button20.grid(row=2,column=0)
button21.grid(row=2,column=1)
button22.grid(row=2,column=2)
button23.grid(row=2,column=3)
button24.grid(row=2,column=4)
button25.grid(row=2,column=5)
button26.grid(row=2,column=6)
button27.grid(row=2,column=7)
button28.grid(row=2,column=8)
button29.grid(row=2,column=9)
button30.grid(row=3,column=0)
button31.grid(row=3,column=1)
button32.grid(row=3,column=2)
button33.grid(row=3,column=3)
button34.grid(row=3,column=4)
button35.grid(row=3,column=5)
button36.grid(row=3,column=6)
button37.grid(row=3,column=7)
button38.grid(row=3,column=8)
button39.grid(row=3,column=9)
button40.grid(row=4,column=0)
button41.grid(row=4,column=1)
button42.grid(row=4,column=2)
button43.grid(row=4,column=3)
button44.grid(row=4,column=4)
button45.grid(row=4,column=5)
button46.grid(row=4,column=6)
button47.grid(row=4,column=7)
button48.grid(row=4,column=8)
button49.grid(row=4,column=9)
button50.grid(row=5,column=0)
button51.grid(row=5,column=1)
button52.grid(row=5,column=2)
button53.grid(row=5,column=3)
button54.grid(row=5,column=4)
button55.grid(row=5,column=5)
button56.grid(row=5,column=6)
button57.grid(row=5,column=7)
button58.grid(row=5,column=8)
button59.grid(row=5,column=9)
button60.grid(row=6,column=0)
button61.grid(row=6,column=1)
button62.grid(row=6,column=2)
button63.grid(row=6,column=3)
button64.grid(row=6,column=4)
button65.grid(row=6,column=5)
button66.grid(row=6,column=6)
button67.grid(row=6,column=7)
button68.grid(row=6,column=8)
button69.grid(row=6,column=9)
button70.grid(row=7,column=0)
button71.grid(row=7,column=1)
button72.grid(row=7,column=2)
button73.grid(row=7,column=3)
button74.grid(row=7,column=4)
button75.grid(row=7,column=5)
button76.grid(row=7,column=6)
button77.grid(row=7,column=7)
button78.grid(row=7,column=8)
button79.grid(row=7,column=9)
button80.grid(row=8,column=0)
button81.grid(row=8,column=1)
button82.grid(row=8,column=2)
button83.grid(row=8,column=3)
button84.grid(row=8,column=4)
button85.grid(row=8,column=5)
button86.grid(row=8,column=6)
button87.grid(row=8,column=7)
button88.grid(row=8,column=8)
button89.grid(row=8,column=9)
button90.grid(row=9,column=0)
button91.grid(row=9,column=1)
button92.grid(row=9,column=2)
button93.grid(row=9,column=3)
button94.grid(row=9,column=4)
button95.grid(row=9,column=5)
button96.grid(row=9,column=6)
button97.grid(row=9,column=7)
button98.grid(row=9,column=8)
button99.grid(row=9,column=9)
butpos={button00:[0,0],button01:[0,1],button02:[0,2],button03:[0,3],button04:[0,4],button05:[0,5],button06:[0,6],button07:[0,7],button08:[0,8],button09:[0,9],
        button10:[1,0],button11:[1,1],button12:[1,2],button13:[1,3],button14:[1,4],button15:[1,5],button16:[1,6],button17:[1,7],button18:[1,8],button19:[1,9],
        button20:[2,0],button21:[2,1],button22:[2,2],button23:[2,3],button24:[2,4],button25:[2,5],button26:[2,6],button27:[2,7],button28:[2,8],button29:[2,9],
        button30:[3,0],button31:[3,1],button32:[3,2],button33:[3,3],button34:[3,4],button35:[3,5],button36:[3,6],button37:[3,7],button38:[3,8],button39:[3,9],
        button40:[4,0],button41:[4,1],button42:[4,2],button43:[4,3],button44:[4,4],button45:[4,5],button46:[4,6],button47:[4,7],button48:[4,8],button49:[4,9],
        button50:[5,0],button51:[5,1],button52:[5,2],button53:[5,3],button54:[5,4],button55:[5,5],button56:[5,6],button57:[5,7],button58:[5,8],button59:[5,9],
        button60:[6,0],button61:[6,1],button62:[6,2],button63:[6,3],button64:[6,4],button65:[6,5],button66:[6,6],button67:[6,7],button68:[6,8],button69:[6,9],
        button70:[7,0],button71:[7,1],button72:[7,2],button73:[7,3],button74:[7,4],button75:[7,5],button76:[7,6],button77:[7,7],button78:[7,8],button79:[7,9],
        button80:[8,0],button81:[8,1],button82:[8,2],button83:[8,3],button84:[8,4],button85:[8,5],button86:[8,6],button87:[8,7],button88:[8,8],button89:[8,9],
        button90:[9,0],button91:[9,1],button92:[9,2],button93:[9,3],button94:[9,4],button95:[9,5],button96:[9,6],button97:[9,7],button98:[9,8],button99:[9,9]}
posbut={(0,0):button00,(0,1):button01,(0,2):button02,(0,3):button03,(0,4):button04,(0,5):button05,(0,6):button06,(0,7):button07,(0,8):button08,(0,9):button09,
        (1,0):button10,(1,1):button11,(1,2):button12,(1,3):button13,(1,4):button14,(1,5):button15,(1,6):button16,(1,7):button17,(1,8):button18,(1,9):button19,
        (2,0):button20,(2,1):button21,(2,2):button22,(2,3):button23,(2,4):button24,(2,5):button25,(2,6):button26,(2,7):button27,(2,8):button28,(2,9):button29,
        (3,0):button30,(3,1):button31,(3,2):button32,(3,3):button33,(3,4):button34,(3,5):button35,(3,6):button36,(3,7):button37,(3,8):button38,(3,9):button39,
        (4,0):button40,(4,1):button41,(4,2):button42,(4,3):button43,(4,4):button44,(4,5):button45,(4,6):button46,(4,7):button47,(4,8):button48,(4,9):button49,
        (5,0):button50,(5,1):button51,(5,2):button52,(5,3):button53,(5,4):button54,(5,5):button55,(5,6):button56,(5,7):button57,(5,8):button58,(5,9):button59,
        (6,0):button60,(6,1):button61,(6,2):button62,(6,3):button63,(6,4):button64,(6,5):button65,(6,6):button66,(6,7):button67,(6,8):button68,(6,9):button69,
        (7,0):button70,(7,1):button71,(7,2):button72,(7,3):button73,(7,4):button74,(7,5):button75,(7,6):button76,(7,7):button77,(7,8):button78,(7,9):button79,
        (8,0):button80,(8,1):button81,(8,2):button82,(8,3):button83,(8,4):button84,(8,5):button85,(8,6):button86,(8,7):button87,(8,8):button88,(8,9):button89,
        (9,0):button90,(9,1):button91,(9,2):button92,(9,3):button93,(9,4):button94,(9,5):button95,(9,6):button96,(9,7):button97,(9,8):button98,(9,9):button99,}


