import tkinter as tk
import random
from tkinter.font import BOLD
import csv

#21F03 Group 9
#Ayman Khan 1006313 - MainInterface() [lines 12-232]
#Ryan Wang 1005923 - Game Idea, Curating questions in csv file, assign_questions [73-113]
#Lee Le Xuan 1006029 - Answer verification and answer popup lines [166-206]
#He Haohua - MainMenu() [lines 253 - 272]


#tkinter is a GUI library which is what help us to see the game itself

class MainInterface():
    def __init__(self,master):
        self.master = master
        self.canvas  = tk.Canvas(self.master,bg="orange",height=600,width=600)

        self.left_button_text = str()
        self.right_button_text = str()

        #creating background and triangle
        self.points = [0,0,200,300,200,600,400,600,400,300,600,0,400,0,300,150,200,0] #to draw the background
        self.canvas.create_polygon(self.points, outline='white',fill='black', width=2) #part of creating the background (the y shape, black road)
        self.circle = self.canvas.create_oval([290,440,310,460],fill='white')
        self.canvas.pack() #declares postion of widgets with respect to one another on the same window

        #creating buttons on left and right
        self.left_button = tk.Button(self.master,text=self.left_button_text ,command = lambda : [self.move_left(),self.disable_button("disabled")] ) #creates left button
        self.right_button = tk.Button(self.master,text=self.right_button_text ,command = lambda: [self.move_right(),self.disable_button("disabled")] ) #creates right button
        self.left_button.place(x=175,y=150) #places a button on the respective coordinates
        self.right_button.place(x=375,y=150) #places a button on the respective coordinates
        
        #creating the score text on the screen
        self.score = 0
        self.points_text = tk.Label(self.master,text="Points:",font = ("Courier New",20),bg="orange") #the different font and format of the text of the score
        self.points_text.place(x=40,y=525)

        self.points_label = tk.Label(self.master,text=self.score,font = ("Courier New",30),bg="orange") #what is the label?
        self.points_label.place(x=55,y=550)

        #this creates the diamonds that function as hearts or lives for us
        self.diamond_1_pts = [500,550,480,530,490,520,510,520,520,530,500,550]
        self.diamond_2_pts = [500,510,480,490,490,480,510,480,520,490,500,510]
        self.diamond_3_pts = [500,470,480,450,490,440,510,440,520,450,500,470]
        self.diamond_1 = self.canvas.create_polygon(self.diamond_1_pts,fill="light blue")
        self.diamond_2 = self.canvas.create_polygon(self.diamond_2_pts,fill="light blue")
        self.diamond_3 = self.canvas.create_polygon(self.diamond_3_pts,fill="light blue")
        self.canvas.pack()

        self.questions = {} #initialise a dictionary
        with open('good_stuff.csv') as f:
            questions_list = csv.reader(f) #store as a linked list - a collection of nodes that have the information (list) and the reference to the next node.
            for i in questions_list: #loop throough each node
                self.questions[i[0]] = i[1:] #store question as key, answers as value
                #the answer is in the form of a list, 0th element is the correct answer

        self.assign_question()

        self.wrong_answers = 0

        #WIDGETS HAVE BEEN CREATED :)

    #we need to disable the button as the pointer is moving as if we don't do this we can press the button while the button moves causing chaos
    #s can be either 'normal' or 'disabled'
    def disable_button(self,s):
        self.left_button.config(state=s)
        self.right_button.config(state=s)
        pass
        

    def assign_question(self): 
        questions = list(self.questions.keys()) #forms a list of the keys (ie the questions)
        if questions == []: #win when the user have answered all the questions - questions list is empty

            #displaying a message when the user wins. - creates a popup
            win = tk.Toplevel(self.master,bg="Yellow")
            win.title("WIN!")
            win.protocol("WM_DELETE_WINDOW", self.disabled)

            #assigns the labels to be displayed in the popoup
            label1 = tk.Label(win,text="YOU WON!",bg="Yellow",font = ("Courier New",20),anchor="center")
            label2 = tk.Label(win,text="Your final score was: ",bg="Yellow",font = ("Courier New",20),anchor="center")
            label3 = tk.Label(win,text=self.score,bg="Yellow",font = ("Courier New",20),anchor="center")
            button1 = tk.Button(win,text="End Game",command = lambda: [win.destroy(),self.master.destroy()])

            #positioning the lables using the grid method
            label1.grid(row=0,column=0,padx=10,pady=10)
            label2.grid(row=1,column=0,padx=10,pady=0)
            label3.grid(row=2,column=0,padx=10,pady=10)
            button1.grid(row=3,column=0,padx=10,pady=10)
        else:
            
            #choosing a question at random from the "questions" list.
            self.random_question = questions[random.randrange(len(questions))]
            #displaying the question.
            self.question_window = tk.Toplevel(self.master)
            self.question_window.resizable(0,0)
            self.question_window.protocol("WM_DELETE_WINDOW", self.disabled)
            self.label = tk.Label(self.question_window,text=self.random_question,font = ("Courier New",18),anchor = "center",bg="orange")
            self.label.grid(row=0,column=0,padx=10,pady=10)

            #randomly assigns 0 and 1 to 2 variables. The text on the labels references these variables to assign either the 0th or the 1st element of the list that has the answer to the question
            choice1 = random.randint(0,1)
            if choice1 == 0:
                choice2 = 1
            else:
                choice2 = 0
            self.left_button_text = self.questions[self.random_question][choice1]
            self.right_button_text = self.questions[self.random_question][choice2]
            self.left_button.config(text = self.left_button_text )
            self.right_button.config(text = self.right_button_text)


    def move_left(self):
        self.question_window.destroy() #clears the question from the screen
        self.answer = self.left_button_text #assigning the chosen answer as the left button text (answer that the user selected)
        y_end = 285
        coords = self.canvas.coords(self.circle)
        x,y = coords[0],coords[1]

        #moving the pointer straight until it reaches the turning point then moving it diagonally
        if y > y_end:
            self.canvas.move(self.circle,0,-5)
            self.master.update()
            self.canvas.after(50,self.move_left)
        else:
            if y > 150 or x > 275:
                self.canvas.move(self.circle,-5,-5)
                self.master.update()
                self.canvas.after(50,self.move_left)
            else:
                self.popup()

    def move_right(self):
        self.question_window.destroy() #clears the question from the screen
        self.answer = self.right_button_text #assigning the chosen answer as the right button text (answer that the user selected)
        y_end = 285
        coords = self.canvas.coords(self.circle)
        x,y = coords[0],coords[1]

        #moving the pointer straight until it reaches the turning point then moving it diagonally
        if y > y_end:
            self.canvas.move(self.circle,0,-5)
            self.master.update()
            self.canvas.after(50,self.move_right)
        else:
            if y > 150 or x < 325:
                self.canvas.move(self.circle,5,-5)
                self.master.update()
                self.canvas.after(50,self.move_right)
            else:
                self.popup()
    
    def check_ans(self):
        #check if answer is the 0th element of the question - correct answer is in the 0th element of the list
        if self.answer == self.questions[self.random_question][0]:
            return True
        else:
            return False

    #we use this function to disable the close button on the popup windows to ensure the user does not bypass some of the code
    def disabled(self):
        pass

    def popup(self):
        #this popup function is a new window that shows whether the user got the correct or wrong answer.

        self.pop = tk.Toplevel(self.master)
        self.pop.title("Results")
        self.pop.protocol("WM_DELETE_WINDOW", self.disabled) #this is to disable the close button on a window (the x close button on the top)

        if self.check_ans():
            #correct answer adds 10 to the score.
            self.score += 10
            self.points_label.config(text=self.score)

            #correct answer message.
            self.pop.config(bg="Yellow")
            self.pop_label = tk.Label(self.pop, text = "Your answer is correct!", bg = "Yellow", fg = "Black", font = ("Courier New",20, BOLD),anchor="center")
        else: 
            #wrong answer message
            self.pop.config(bg="Red")
            self.pop_label = tk.Label(self.pop, text = "Your answer is incorrect!", bg = "Red", fg = "Black", font = ("Courier New", 20, BOLD),anchor="center")

            self.wrong_answers += 1
            if self.wrong_answers == 1:
                self.canvas.delete(self.diamond_3) #if this is the first time getting a wrong answer, only one diamond is lost
            elif self.wrong_answers == 2:
                self.canvas.delete(self.diamond_2) #if it is the second time getting a wrong answer, player loses 2 diamonds

            else:
                self.canvas.delete(self.diamond_1) #third time - lost last life = game over :(
                
                #displaying game over window
                self.final_popup = tk.Toplevel(self.master,bg='red')
                self.final_popup.title("sadness :<") #name of the window that pops up (along the window border)
                self.final_popup.protocol("WM_DELETE_WINDOW", self.disabled)
                game_over = tk.Label(self.final_popup,font = ("Courier New",20, BOLD),anchor="center",text="GAME OVER!") #display the game over message
                main_line = tk.Label(self.final_popup,font = ("Courier New",16),anchor="center",text="Your final Score is:") #displaying the final score of the user
                score_line = tk.Label(self.final_popup,font = ("Courier New",20),anchor="center",text=self.score)
                game_over.grid(row=0,column=0,padx=10,pady=10)
                main_line.grid(row=1,column=0,padx=10,pady=10)
                score_line.grid(row=2,column=0,padx=10,pady=10)
                exit_button = tk.Button(self.final_popup,text="Exit",command=lambda:self.master.destroy())
                exit_button.grid(row=3,column=0,padx=10,pady=10)
                
        #this is for the correct / wrong answer window, to position the labels
        self.pop_label.grid(row=0,column=0,columnspan=2,padx=10,pady=10)

        self.ok = tk.Button(self.pop, text = "Ok", font = ("Arial", 11), bg = "White", fg = "Black", command = lambda: self.resume_game("Ok"))
        self.ok.grid(row=1,column=0,padx=10,pady=10)

        quit = tk.Button(self.pop, text = "Quit", font = ("Arial", 11), bg = "White", fg = "Black", command = lambda: self.resume_game("Quit"))
        quit.grid(row=1,column=1,padx=10,pady=10)
    
    #this will resume the game after the popup message for right or wrong answer, provided last life is not over
    def resume_game(self,choice):
        if choice == "Ok" and self.wrong_answers<3:
            self.disable_button('normal')
            self.pop.destroy()
            self.reset() #put the pointer circle back to its original position
            del self.questions[self.random_question] #deletes the question that has already been asked so that it does not repeat
            self.assign_question()
        elif choice == "Quit":
            self.pop.destroy()
            self.master.destroy()
        else:
            self.pop.destroy()

    def reset(self):
        #put the pointer circle back to its original position
        self.canvas.coords(self.circle,[290,440,310,460])
        pass


        
class MainMenu():
    def __init__(self,master):
        self.master = master
        self.master.config(bg='orange')
        header = tk.Label(self.master,text="I'm Bored",font = ("Courier New",30, BOLD),anchor="center",bg="orange")
        subhead = tk.Label(self.master,text="A game made by Bored People for Bored People.",font = ("Courier New",15, BOLD),anchor="center",bg="orange")
        subhead2 = tk.Label(self.master,text="Select the correct option to help Bob the Ball find his way!",font = ("Courier New",15, BOLD),anchor="center",bg="orange")
        subhead3 = tk.Label(self.master,text="A correct answer gives you 10 points but a wrong answer will make Bob lose one of his diamonds!",font = ("Courier New",15, BOLD),anchor="center",bg="orange")
        subhead4 = tk.Label(self.master,text="If he loses all 3 of his diamonds, the game will be over and you may suffer boredom forever!",font = ("Courier New",15, BOLD),anchor="center",bg="orange")
        subhead5 = tk.Label(self.master,text="Your challenge, should you choose to accept it, is to help bob find his way and as a reward you cure your boredom",font = ("Courier New",15, BOLD),anchor="center",bg="orange")

        play = tk.Button(self.master,text="Play",command= lambda:self.play())

        header.grid(row=0,column=0,columnspan=2,padx=10,pady=10)
        subhead.grid(row=1,column=0,columnspan=2,padx=10,pady=10)
        subhead2.grid(row=2,column=0,columnspan=2,padx=10,pady=10)
        subhead3.grid(row=3,column=0,columnspan=2,padx=10,pady=10)
        subhead4.grid(row=4,column=0,columnspan=2,padx=10,pady=10)
        subhead5.grid(row=5,column=0,columnspan=2,padx=10,pady=10)
        play.grid(row=6,column=0,columnspan=2,padx=10,pady=10)
    
    def play(self):
        self.master.destroy()

        
if __name__ == '__main__':
    mainmenu = tk.Tk()
    mainmenu.resizable(0,0)
    mainmenu.title("Main Menu")

    MainMenu(mainmenu)

    mainmenu.mainloop()

    root = tk.Tk() #initialises the tkinter library and creates a tk object
    root.resizable(0,0) #cannot resize the window
    root.title("Boring Game") #gives the window a title

    MainInterface(root) #calls the init function of the class MainInterface (initialzes the class)

    root.mainloop() #loop through the tk object and all the widgets over and over in order to keep th43 e widgets on screen