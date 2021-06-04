import tkinter as tk

main = tk.Tk()
main.title("Calculator")
main.resizable(0,0)

number1 = 0
number2 = 0
# OPERATOR KEY CODE
# 1 = +
# 2 = -
# 3 = *
# 4 = /

numDict = {"number":0,"opkey":0}
opkey = 0

entry = tk.Entry(main, width=40,borderwidth=5)
entry.grid(row=0,column=0, columnspan=4, padx=5, pady=5)

def buttonPressed(no):
    a = entry.get()
    b = len(a)
    entry.insert(b,str(no))

def insertIn(number):
    s = str(number)
    s = s.strip()
    entry.insert(0,s)

def operator(xyz):
    global numDict
    number = entry.get()
    entry.delete(0,len(str(number)))
    if xyz == "+":
        numDict = {"number":number,"opkey":1}
    elif xyz == "-":
        numDict = {"number":number,"opkey":2}
    elif xyz == "*":
        numDict = {"number":number,"opkey":3}
    elif xyz == "/":
        numDict = {"number":number,"opkey":4}
    elif xyz == "=":
        if numDict['opkey'] == 1:
            answer = int(number) + int(numDict['number'])
            insertIn(answer)
        elif numDict['opkey'] == 2:
            answer = int(number) - int(numDict['number'])
            insertIn(answer)
        elif numDict['opkey'] == 3:
            answer = int(number) * int(numDict['number'])
            insertIn(answer)
        elif numDict['opkey'] == 4:
            answer = int(number) / int(numDict['number'])
            insertIn(answer)


button7 = tk.Button(main,text="7",width = 5, padx=5, pady=5, command = lambda:buttonPressed(7))
button7.grid(row=1,column=0)

button8 = tk.Button(main,text="8",width = 5, padx=5, pady=5, command = lambda:buttonPressed(8))
button8.grid(row=1,column=1)

button9 = tk.Button(main,text="9",width = 5, padx=5, pady=5, command = lambda:buttonPressed(9))
button9.grid(row=1,column=2)

addButton = tk.Button(main,text="x",width = 5, padx=5, pady=5,command = lambda: operator("*"))
addButton.grid(row=1,column=3)

button4 = tk.Button(main,text="4",width = 5, padx=5, pady=5, command = lambda:buttonPressed(4))
button4.grid(row=2,column=0)

button5 = tk.Button(main,text="5",width = 5, padx=5, pady=5, command = lambda:buttonPressed(5))
button5.grid(row=2,column=1)

button6 = tk.Button(main,text="6",width = 5, padx=5, pady=5, command = lambda:buttonPressed(6))
button6.grid(row=2,column=2)

subButton = tk.Button(main,text="-",width = 5, padx=5, pady=5,command = lambda: operator("-"))
subButton.grid(row=2,column=3)

button1 = tk.Button(main,text="1",width = 5, padx=5, pady=5, command = lambda:buttonPressed(1))
button1.grid(row=3,column=0)

button2 = tk.Button(main,text="2",width = 5, padx=5, pady=5, command = lambda:buttonPressed(2))
button2.grid(row=3,column=1)

button3 = tk.Button(main,text="3",width = 5, padx=5, pady=5, command = lambda:buttonPressed(3))
button3.grid(row=3,column=2)

addButton = tk.Button(main,text="+",width = 5, padx=5, pady=5,command = lambda: operator("+"))
addButton.grid(row=3,column=3)

button0 = tk.Button(main,text="0",width = 16, padx=5, pady=5, command = lambda:buttonPressed(3))
button0.grid(row=4,column=0,columnspan=2)

decimalButton = tk.Button(main,text=".",width = 5, padx=5, pady=5)
decimalButton.grid(row=4,column=2)

equalButton = tk.Button(main,text="=",width = 5, padx=5, pady=5,command = lambda: operator("="))
equalButton.grid(row=4,column=3)

main.mainloop()