#made by Ayman Khan
#instagram.com/aymanxkhan
#twitter.com/isntkhani


import tkinter as tk
from tkinter import simpledialog

root = tk.Tk()
root.title("Tic Tac Toe")

player1=simpledialog.askstring(title='Player1',prompt='Player1 enter your name: ')
player2=simpledialog.askstring(title='Player2',prompt='Player2 enter your name: ')

p1=0
p2=1


O='O'
X='X'

def disableButton(buttons):
	buttons.configure(state='disabled')

def activateButton(buttons):
	buttons.configure(state='active')

def clicked(buttons):
	global p1
	if p1==0:
		buttons['text'] = "X"
		p1=1
		disableButton(buttons)
	else:
		buttons['text'] = "O"
		p1=0
		disableButton(buttons)
	checkX()
	checkO()

def refresh():
	global l,winner
	for i in l:
		i['text'] = " "
		activateButton(i)
	winner['text'] = ' '

def win1():
	global l,winner
	for i in l:
		disableButton(i)
	winner=tk.Label(root,text=player1+" has won!", height='4',width='12')
	winner.grid(row=0,column=2)

def win2():
	global l,winner
	for i in l:
		disableButton(i)
	winner=tk.Label(root,text=player2+" has won!", height='4',width='12')
	winner.grid(row=0,column=2)
	

def checkX():
	global button1,button2,button4,button3,button5,button6,button7,button8,button9,l
	if button1['text'] == X and button5['text'] == X and button9['text'] == X: #diag 1
		win1()
	elif button3['text'] == X and button5['text'] == X and button7['text'] == X: #diag 2
		win1()
	elif button1['text'] == X and button2['text'] == X and button3['text'] == X: #row 1
		win1()
	elif button4['text'] == X and button5['text'] == X and button6['text'] == X: #row2
		win1()
	elif button7['text'] == X and button8['text'] == X and button9['text'] == X: #row 3
		win1()
	elif button1['text'] == X and button4['text'] == X and button7['text'] == X: #col 1
		win1()
	elif button2['text'] == X and button5['text'] == X and button8['text'] == X: #col 2
		win1()
	elif button3['text'] == X and button6['text'] == X and button9['text'] == X: #col 3
		win1()

def checkO():
	global button1,button2,button4,button3,button5,button6,button7,button8,button9,l
	if button1['text'] == O and button5['text'] == O and button9['text'] == O: #diag 1
		win2()
	elif button3['text'] == O and button5['text'] == O and button7['text'] == O: #diag 2
		win2()
	elif button1['text'] == O and button2['text'] == O and button3['text'] == O: #row 1
		win2()
	elif button4['text'] == O and button5['text'] == O and button6['text'] == O: #row2
		win2()
	elif button7['text'] == O and button8['text'] == O and button9['text'] == O: #row 3
		win2()
	elif button1['text'] == O and button4['text'] == O and button7['text'] == O: #col 1
		win2()
	elif button2['text'] == O and button5['text'] == O and button8['text'] == O: #col 3
		win2()
	elif button3['text'] == O and button6['text'] == O and button9['text'] == O: #col 4
		win2()


		
button1 = tk.Button(root, text='',height='4',width='8', command= lambda: clicked(button1))
button1.grid(row=1,column=1)

button2 = tk.Button(root, text='',height='4',width='8', command= lambda: clicked(button2))
button2.grid(row=1,column=2)

button3 = tk.Button(root, text='',height='4',width='8', command= lambda: clicked(button3))
button3.grid(row=1, column=3)

button4 = tk.Button(root, text='',height='4',width='8', command= lambda: clicked(button4))
button4.grid(row=2,column=1)

button5 = tk.Button(root, text='',height='4',width='8', command= lambda: clicked(button5))
button5.grid(row=2,column=2)

button6 = tk. Button(root, text='',height='4',width='8', command= lambda: clicked(button6))
button6.grid(row=2,column=3)

button7 = tk. Button(root, text='',height='4',width='8', command= lambda: clicked(button7))
button7.grid(row=3,column=1)

button8 = tk. Button(root, text='',height='4',width='8', command= lambda: clicked(button8))
button8.grid(row=3,column=2)

button9 = tk. Button(root, text='',height='4',width='8', command= lambda: clicked(button9))
button9.grid(row=3,column=3)

restart = tk.Button(root, text="Restart",height='2',width='8',command= lambda: refresh())
restart.grid(row=4, column=2)

l=[button1,button2,button3,button4,button5,button6,button7,button8,button9]