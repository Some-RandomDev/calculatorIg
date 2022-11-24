import tkinter
import tkinter.messagebox
import bohotKhatarnakHai
win = tkinter.Tk()
inp = ''
win.title('Caclculator... thingy i guess')

tkinter.Grid.rowconfigure(win,0,weight=1)
tkinter.Grid.rowconfigure(win,4,weight=1)
tkinter.Grid.rowconfigure(win,1,weight=1)
tkinter.Grid.rowconfigure(win,2,weight=1)
tkinter.Grid.rowconfigure(win,3,weight=1)
tkinter.Grid.rowconfigure(win,4,weight=1)
tkinter.Grid.rowconfigure(win,5,weight=1)
tkinter.Grid.columnconfigure(win,0,weight=1)
tkinter.Grid.columnconfigure(win,1,weight=1)
tkinter.Grid.columnconfigure(win,2,weight=1)
tkinter.Grid.columnconfigure(win,3,weight=1)


inputScreen = tkinter.Label(win, text = '', justify = tkinter.RIGHT)
inputScreen.grid(column= 0, columnspan= 4)
outputScreen = tkinter.Label(win, text = '', fg='#afafaf', justify = tkinter.RIGHT)
outputScreen.grid(row=1, columnspan= 4)
def inpt(char):
    global inp
    try:
        inp = str(int(inp))
    except:
        inp = str(inp)
    inp += str(char)
    inputScreen['text'] = inp
    outputScreen['fg'] = '#afafaf'
    try:
        outputScreen['text'] = bohotKhatarnakHai.Calc(inp)
    except:
        outputScreen['text'] = ''

def clear():
    global inp
    inp = ''
    inputScreen['text'] = inp

def enter():
    try:
        global inp
        inp = bohotKhatarnakHai.Calc(inp)
        inputScreen['text'] = inp
        outputScreen['text'] = ''
    except (ZeroDivisionError):
        tkinter.messagebox.showerror('Lol', 'Can\'t really divide by zero now can you')
    except (ValueError):
        tkinter.messagebox.showerror('Whoops', 'Looks like you forgot a number there')

    
b1 = tkinter.Button(win, text = '1',bg = 'WHITE', relief = tkinter.FLAT, activebackground = 'YELLOW',command=lambda:inpt('1')).grid(row = 2,column = 0,sticky = 'NSEW')
b2 = tkinter.Button(win, text = '2',bg = 'WHITE', relief = tkinter.FLAT, activebackground = 'YELLOW',command=lambda:inpt('2')).grid(row = 2,column = 1,sticky = 'NSEW')
b3 = tkinter.Button(win, text = '3',bg = 'WHITE', relief = tkinter.FLAT, activebackground = 'YELLOW',command=lambda:inpt('3')).grid(row = 2,column = 2,sticky = 'NSEW')
bA = tkinter.Button(win, text = '+',bg = 'WHITE', relief = tkinter.FLAT, activebackground = 'YELLOW',command=lambda:inpt('+')).grid(row = 2,column = 3,sticky = 'NSEW')
b4 = tkinter.Button(win, text = '4',bg = 'WHITE', relief = tkinter.FLAT, activebackground = 'YELLOW',command=lambda:inpt('4')).grid(row = 3,column = 0,sticky = 'NSEW')
b5 = tkinter.Button(win, text = '5',bg = 'WHITE', relief = tkinter.FLAT, activebackground = 'YELLOW',command=lambda:inpt('5')).grid(row = 3,column = 1,sticky = 'NSEW')
b6 = tkinter.Button(win, text = '6',bg = 'WHITE', relief = tkinter.FLAT, activebackground = 'YELLOW',command=lambda:inpt('6')).grid(row = 3,column = 2,sticky = 'NSEW')
bS = tkinter.Button(win, text = '-',bg = 'WHITE', relief = tkinter.FLAT, activebackground = 'YELLOW',command=lambda:inpt('-')).grid(row = 3,column = 3,sticky = 'NSEW')
b7 = tkinter.Button(win, text = '7',bg = 'WHITE', relief = tkinter.FLAT, activebackground = 'YELLOW',command=lambda:inpt('7')).grid(row = 4,column = 0,sticky = 'NSEW')
b8 = tkinter.Button(win, text = '8',bg = 'WHITE', relief = tkinter.FLAT, activebackground = 'YELLOW',command=lambda:inpt('8')).grid(row = 4,column = 1,sticky = 'NSEW')
b9 = tkinter.Button(win, text = '9',bg = 'WHITE', relief = tkinter.FLAT, activebackground = 'YELLOW',command=lambda:inpt('9')).grid(row = 4,column = 2,sticky = 'NSEW')
bM = tkinter.Button(win, text = '*',bg = 'WHITE', relief = tkinter.FLAT, activebackground = 'YELLOW',command=lambda:inpt('*')).grid(row = 4,column = 3,sticky = 'NSEW')
bC = tkinter.Button(win, text = 'C',bg = 'ORANGE', relief = tkinter.FLAT, activebackground = 'RED', command=clear).grid(row = 5,column = 0,sticky = 'NSEW')
b0 = tkinter.Button(win, text = '0',bg = 'WHITE', relief = tkinter.FLAT, activebackground = 'YELLOW',command=lambda:inpt('0')).grid(row = 5,column = 1,sticky = 'NSEW')
bE = tkinter.Button(win, text = '=',bg = 'WHITE', relief = tkinter.FLAT, activebackground = 'YELLOW',command=enter).grid(row = 5,column = 2,sticky = 'NSEW')
bS = tkinter.Button(win, text = '/',bg = 'WHITE', relief = tkinter.FLAT, activebackground = 'YELLOW',command=lambda:inpt('/')).grid(row = 5,column = 3,sticky = 'NSEW')
win.mainloop()
