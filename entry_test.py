from tkinter import *

master = Tk()

first_name = Label(master, text="Enter first name").pack(side=TOP)

first_name = Entry(master, width=20)
first_name.pack()
first_name.focus_set()

last_name = Label(master, text="Enter last name").pack(side=TOP)

last_name = Entry(master, width=20)
last_name.pack()

def callback():
    print("{}, {}".format(last_name.get(), first_name.get()))
    output = Label(master, text="{}, {}".format(last_name.get(), first_name.get())).pack(side=BOTTOM)
    

b = Button(master, text="format", width=10, command=callback)
b.pack()

mainloop()

# def makeentry(parent, caption, width=None, **options):
#     Label(parent, text=caption).pack(side=LEFT)
#     entry = Entry(parent, **options)
#     if width:
#         entry.config(width=width)
#     entry.pack(side=LEFT)
#     return entry

# user = makeentry(login, "User name:", 10)
# password = makeentry(login, "Password:", 10, show="*")

# content = StringVar()
# entry = Entry(login, text=caption, textvariable=content)

# text = content.get()
# content.set(text)