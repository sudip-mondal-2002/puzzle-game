from tkinter import Button,Entry,Tk
l=[]
def entryfile(e):
    s=e.get()
    e.delete(0,"end")
    l.append(s+'\n')
def writetofile(t):
    t.destroy()
    file=open('words.txt',mode='w')
    file.writelines(l)
    file.close()
tk=Tk()
inputentry=Entry(tk,width=24)
inputbutton=Button(tk,text='ok',width=20,command=lambda:(entryfile(inputentry)))
donebutton=Button(tk,text='done',width=20,command=lambda:(writetofile(tk)))
inputentry.pack()
inputbutton.pack()
donebutton.pack()
