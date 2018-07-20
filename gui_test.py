from tkinter import *

class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.quit_button = Button(
            frame, text="QUIT", fg="red", command=frame.quit
            )
        
        self.quit_button.pack(side=LEFT)

        self.hi_button = Button(frame, text="Hello", command=self.say_hi)
        self.hi_button.pack(side=LEFT)

        self.e = Entry(master)
        self.e.pack()

    def say_hi(self):
        print("hi there, everyone!")

root = Tk()

app = App(root)

root.mainloop()
root.destroy()
