import tkinter as tk
from tkinter import font

root = tk.Tk()
root.title("Tic Tac Toe")

currentTern = "x"

def checkWin():
    #row 1
    g00 = gameState[0][0].cget('text')
    g01 = gameState[0][1].cget('text')
    g02 = gameState[0][2].cget('text')
    #row 2
    g10 = gameState[1][0].cget('text')
    g11 = gameState[1][1].cget('text')
    g12 = gameState[1][2].cget('text')
    #row 2
    g20 = gameState[2][0].cget('text')
    g21 = gameState[2][1].cget('text')
    g22 = gameState[2][2].cget('text')


    #case 1
    if g00 == g01 == g02 != " ":
        return True
    #case 2
    if g10 == g11 == g12 != " ":
        return True
    #case 3
    if g20 == g21 == g22 != " ":
        return True
    #case 4
    if g00 == g10 == g20 != " ":
        return True
    #case 5
    if g01 == g11 == g21 != " ":
        return True
    #case 6
    if g02 == g12 == g22 != " ":
        return True
     #case 7
    if g00 == g11 == g22 != " ":
        return True
    #case 8
    if g02 == g11 == g20 != " ":
        return True
    

    return False

  

def makemove(row, column):
    global currentTern
    if gameState [row][column].cget ('text') == " ":
        gameState[row][column].config(text = currentTern)
    if checkWin():
        gameMassageLevel.config(text=f"{currentTern} Won!!!")
        return
    if(currentTern== "o"):
        currentTern= "x"
    else:
        currentTern= "o"
    gameMassageLevel.config(text= f"Turn for- {currentTern}")

def makeButton(row, column):
    button = tk.Button(root, text=" ", font=font.Font(size=24), padx=10, pady=10, command= lambda:makemove(row, column))
    button.grid(row=row, column=column)
    return button

gameState=[
    [makeButton(0,0),makeButton(0,1),makeButton(0,2)],
    [makeButton(1,0),makeButton(1,1),makeButton(1,2)],
    [makeButton(2,0),makeButton(2,1),makeButton(2,2)],
]
gameMassageLevel = tk.Label(root, text="Turn for -x", background= "pink",font=font.Font(size=24))
gameMassageLevel.grid(row=3, column=0, columnspan=3)
root.mainloop()