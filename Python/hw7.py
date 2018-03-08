
# Morgan Shively
# Homework 8

from tkinter import *
import random

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
        self.num=random.randrange(0,10)




    def create_widgets(self):
        self.lbl = Label(self, text="Enter your Guess:")
        self.lbl.grid()
        self.ent1=Entry(self)
        self.ent1.grid()
        self.bttn1 = Button(self, text = "Enter",command=self.userGuess)
        self.bttn1.grid()

    def userGuess(self):
        if int(self.ent1.get()) == self.num:
            self.lbl["text"]="Congratulations, you got it!"
        self.ent1.delete(0, END)



# main
root = Tk()
root.title("Game")
#root.geometry("400x200")
root.resizable(width = FALSE, height = FALSE)

app = Application(root)
root.mainloop()










#additional Problem

from tkinter import *

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        
        self.lbl = Label(self, text="What would you like delievered")
        self.lbl.grid(row=0,column=0,sticky=W)
        self.lb2 =Label(self,text="Options")
        self.lb2.grid(row=1,column=1,sticky=N)
        self.lb3= Label(self,text="Delivery Method:")
        self.lb3.grid(row=3,column=0,sticky=W)
        self.lb4=Label(self,text="AddOns:")
        self.lb4.grid(row=3,column=2,sticky=W)
        self.bttn1 = Button(self, text = "Confirm Delivery",command =self.Total_Cost)
        self.bttn1.grid(row=7,column=1)
        self.text=Text(self, width=80,height=20,wrap=WORD)
        self.text.grid(row=8, columnspan = 4)
        self.ent1 = Entry(self)
        self.ent1.grid(row=0,column=1,columnspan=2)
        self.delivery = StringVar()
        self.delivery.set("drone")
        Radiobutton(self,text = "Flying Drone ($10)", variable = self.delivery,value = "drone").grid(row = 4, column = 0, sticky = W)
        Radiobutton(self,text = "Self Driving Car ($20)", variable = self.delivery,value = "car").grid(row = 5, column = 0, sticky = W)
        Radiobutton(self,text = "Giant Robot ($1000)", variable = self.delivery,value = "robot").grid(row = 6, column = 0, sticky = W)

        self.addon = BooleanVar()
        self.addon2 = BooleanVar()
        self.addon3 = BooleanVar()

        Checkbutton(self,text = "Express Delivery (+$30)", variable = self.addon).grid(row = 4, column = 2, sticky = W)
        Checkbutton(self,text = "Mostly Not Broken (+$20)", variable = self.addon2).grid(row = 5, column = 2, sticky = W)
        Checkbutton(self,text = "With a Smile (+$1)", variable = self.addon3).grid(row = 6, column = 2, sticky = W)

    def Total_Cost(self):
        message ="You selectd to have a " + self.ent1.get()
        

    
        message+= " delivered by " + self.delivery.get()
        number=0

        if self.delivery.get()=="drone":
            number+=10
        if self.delivery.get()=="car":
            number+=20
        if self.delivery.get()=="robot":
            number+=1000
            

        if self.addon.get():
            number+=30
            message+= " with express delivery."
        if self.addon2.get():
            number+=20
            message+= " with mostly not broken."
        if self.addon3.get():
            number+=1
            message+= " with a smile."
        else:
            message+= " with no options."


        message+=" Your total delivery fee comes to: " +str(number)
        
        
        self.text.insert(0.0, message)

# main
root = Tk()
root.title("Robot Delivery")
root.geometry("600x300")
root.resizable(width = TRUE, height = TRUE)

app = Application(root)
root.mainloop()
