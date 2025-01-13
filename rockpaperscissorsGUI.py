from tkinter import Tk, Frame, Label, Button
import random

class RockPaperScissors:
    def __init__(self, root=None):
        self.__pc_options = ["Paper", "Rock", "Scissors"]
        self.initiate()

    @classmethod
    def play(cls):
        pass

    @classmethod
    def initiate(cls):        
        root = Tk()
        root.title("Rock Paper Scissors")
        root.geometry("225x250")
        cls.widget = Frame(root)
        cls.widget.pack()
        cls.result = Label(root, text="Result: ")
        cls.result.pack()
        cls.result = 0
        cls.pc_label = Label(root, text="PC: " + str(cls.result))
        cls.user_label = Label(root, text="User: " + str(cls.result))
        cls.pc_label.pack()
        cls.user_label.pack()
        cls.button_widget = Frame(root)
        cls.paper_btn = Button(cls.button_widget, padx=20)
        cls.paper_btn["text"] = "Paper"
        cls.rock_btn = Button(cls.button_widget, padx=20)
        cls.rock_btn["text"] = "Rock"
        cls.scissors_btn = Button(cls.button_widget, padx=20)
        cls.scissors_btn["text"] = "Scissors"
        cls.button_widget.pack(side="bottom")
        cls.paper_btn.pack(side="left")
        cls.rock_btn.pack(side="left")
        cls.scissors_btn.pack(side="left")
        root.mainloop()

RockPaperScissors.initiate()