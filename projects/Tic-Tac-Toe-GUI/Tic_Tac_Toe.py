# tictactoe Game
# -----------------
from tkinter import *
from tkinter import messagebox

count = 0
root = Tk()  # root = root or window or any name
root.geometry("286x300")
root.title("Tic-Tac-Toe")
bx1 = "1"
bx2 = "2"
bx3 = "3"
bx4 = "4"
bx5 = "5"
bx6 = "6"
bx7 = "7"
bx8 = "8"
bx9 = "9"

a = Label(root, text=" X-O Game \n @TanCodes", bg="light blue",
          justify="center").grid(row=3, column=1, sticky=S)
b1 = Button(root, text=" ", bg="ivory2", command=lambda: t(1))
b1.grid(row='0', column="0", ipadx='40', ipady='30')
b2 = Button(root, text=" ", bg="ivory2", command=lambda: t(2))
b2.grid(row='0', column="1", ipadx='40', ipady='30')
b3 = Button(root, text=" ", bg="ivory2", command=lambda: t(3))
b3.grid(row='0', column="2", ipadx='40', ipady='30')

b4 = Button(root, text=" ", bg="ivory2", command=lambda: t(4))
b4.grid(row='1', column="0", ipadx='40', ipady='30')
b5 = Button(root, text=" ", bg="ivory2", command=lambda: t(5))
b5.grid(row='1', column="1", ipadx='40', ipady='30')
b6 = Button(root, text=" ", bg="ivory2", command=lambda: t(6))
b6.grid(row='1', column="2", ipadx='40', ipady='30')

b7 = Button(root, text=" ", bg="ivory2", command=lambda: t(7))
b7.grid(row='2', column="0", ipadx='40', ipady='30')
b8 = Button(root, text=" ", bg="ivory2", command=lambda: t(8))
b8.grid(row='2', column="1", ipadx='40', ipady='30')
b9 = Button(root, text=" ", bg="ivory2", command=lambda: t(9))
b9.grid(row='2', column="2", ipadx='40', ipady='30')

player = 1


def t(box):
    global player
    global count
    global bx1, bx2, bx3, bx4, bx5, bx6, bx7, bx8, bx9

    count = count + 1

    if box == 1 and player == 1:
        b1.config(text="O")
        b1.configure(state=DISABLED)
        player = 2
        bx1 = "O"
    elif box == 1 and player == 2:
        b1.config(text="X")
        b1.configure(state=DISABLED)
        player = 1
        bx1 = "X"
    elif box == 2 and player == 1:
        b2.config(text="O")
        b2.configure(state=DISABLED)
        player = 2
        bx2 = "O"
    elif box == 2 and player == 2:
        b2.config(text="X")
        b2.configure(state=DISABLED)
        player = 1
        bx2 = "X"
    elif box == 3 and player == 1:
        b3.config(text="O")
        b3.configure(state=DISABLED)
        player = 2
        bx3 = "O"
    elif box == 3 and player == 2:
        b3.config(text="X")
        b3.configure(state=DISABLED)
        player = 1
        bx3 = "X"
    elif box == 4 and player == 1:
        b4.config(text="O")
        b4.configure(state=DISABLED)
        player = 2
        bx4 = "O"
    elif box == 4 and player == 2:
        b4.config(text="X")
        b4.configure(state=DISABLED)
        player = 1
        bx4 = "X"
    elif box == 5 and player == 1:
        b5.config(text="O")
        b5.configure(state=DISABLED)
        player = 2
        bx5 = "O"
    elif box == 5 and player == 2:
        b5.config(text="X")
        b5.configure(state=DISABLED)
        player = 1
        bx5 = "X"
    elif box == 6 and player == 1:
        b6.config(text="O")
        b6.configure(state=DISABLED)
        player = 2
        bx6 = "O"
    elif box == 6 and player == 2:
        b6.config(text="X")
        b6.configure(state=DISABLED)
        player = 1
        bx6 = "X"
    elif box == 7 and player == 1:
        b7.config(text="O")
        b7.configure(state=DISABLED)
        player = 2
        bx7 = "O"
    elif box == 7 and player == 2:
        b7.config(text="X")
        b7.configure(state=DISABLED)
        player = 1
        bx7 = "X"
    elif box == 8 and player == 1:
        b8.config(text="O")
        b8.configure(state=DISABLED)
        player = 2
        bx8 = "O"
    elif box == 8 and player == 2:
        b8.config(text="X")
        b8.configure(state=DISABLED)
        player = 1
        bx8 = "X"
    elif box == 9 and player == 1:
        b9.config(text="O")
        b9.configure(state=DISABLED)
        player = 2
        bx9 = "O"
    elif box == 9 and player == 2:
        b9.config(text="X")
        b9.configure(state=DISABLED)
        player = 1
        bx9 = "X"
    #######################################

    if bx1 == bx2 == bx3 == "X" or bx4 == bx5 == bx6 == "X" or bx7 == bx8 == bx9 == "X" or bx1 == bx5 == bx9 == "X" or bx3 == bx5 == bx7 == "X" or bx1 == bx4 == bx7 == "X" or bx2 == bx5 == bx8 == "X" or bx3 == bx6 == bx9 == "X":
        player = "X"
        messagebox._show("Game end  ", "Player " + player + "  Won")
        exit(0)

    if bx1 == bx2 == bx3 == "O" or bx4 == bx5 == bx6 == "O" or bx7 == bx8 == bx9 == "O" or bx1 == bx5 == bx9 == "O" or bx3 == bx5 == bx7 == "O" or bx1 == bx4 == bx7 == "O" or bx2 == bx5 == bx8 == "O" or bx3 == bx6 == bx9 == "O":
        player = "O"
        messagebox._show("Game end  ", "Player " + player + "   Won")
        exit(0)

    if count == 9:
        messagebox._show("Game end", "DRAW- Try Again")
        exit(0)


root.resizable(0, 0)
root.mainloop()
